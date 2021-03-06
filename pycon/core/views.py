from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.utils import simplejson
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.template import loader, Context
from django.conf import settings 
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import logout

from pycon.core.decorators import render_to
from pycon.core.models import *
from pycon.core.forms import *

import random
from hashlib import sha1
import base64

__all__ = ('index')

@render_to('index.html')
def index(request):
    last_news = News.objects.all().order_by('-created')
    speakers = Speaker.objects.all()
    return {'last_news':last_news, 
            'speakers': speakers}


@render_to('register.html')
def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile')
    if request.method == 'POST':
        form = ParticipantRegistrationForm(request.POST)
        if form.is_valid():
            #create user
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            
            user = User.objects.create_user(username=email,
                                           email=email,
                                           password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            #create profile
            profile = ParticipanProfile.objects.create(
                                                       user=user,
                                                       #tshirt_size=form.cleaned_data['tshirt_size'],
                                                       #pre_party=form.cleaned_data['pre_party'],
                                                       #ticket_barcode=form.cleaned_data['ticket_barcode'].strip(),
                                                       organization=form.cleaned_data['organization'],
                                                       occupation=form.cleaned_data['occupation'],
                                                       country=form.cleaned_data['country'],
                                                       city=form.cleaned_data['city'],
                                                       phone=form.cleaned_data['phone'],
                                                       python_level=form.cleaned_data['python_level'],
                                                       python_years=form.cleaned_data['python_years'],
                                                       twitter_name=form.cleaned_data['twitter_name'],
                                                       blog=form.cleaned_data['blog'],
                                                       linkedin=form.cleaned_data['linkedin'],
                                                       facebook=form.cleaned_data['facebook'],
                                                       kyivpy2=form.cleaned_data['kyivpy2'],
                                                       agree=form.cleaned_data['agree'],
                                                       public=form.cleaned_data['public'],
                                                       )
            profile.verification_code = base64.urlsafe_b64encode(sha1(email+password+str(random.random())+settings.SECRET_KEY).digest())
            profile.save()
            
            #send verification email
            confirm_link = 'http://ua.pycon.org/confirm/%s' % profile.verification_code
            context = {'first_name': first_name,
                       'last_name': last_name,
                       'confirm_link': confirm_link,
                       'barcode': profile.ticket_barcode != ''}
            t = loader.get_template("verification_email_new.txt")
            #t2 = loader.get_template("verification_email.html")
            text_content = t.render(Context(context))
            #html_content = t2.render(Context(context))
            
            subject, from_email, to = 'Confirmation of the registration on the ua.pycon.org site', 'do-not-reply@ua.pycon.org', email
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            #msg.attach_alternative(html_content, "text/html")
            msg.send()
            
            context = {'success': True}
        else:
            context = {'success': False,
                       'errors': True,
                       'participantform': form
                       }
        
    else:
        form = ParticipantRegistrationForm()
        context = {'participantform': form}
    speakers = Speaker.objects.all()
    context['speakers']= speakers
    return context

@render_to('confirm.html')
def confirm(request, code):
    profile = get_object_or_404(ParticipanProfile, verification_code=code)
    profile.active = True
    profile.save()
    speakers = Speaker.objects.all()
    return {'success': True, 'speakers': speakers}

@login_required
@render_to('profile.html')
def profile(request):
    user = request.user
    profile = get_object_or_404(ParticipanProfile, user=user)
    if not profile.active:
       logout(request)
       return {'error': 'You profile haven\'t been activated. Please recheck you email for activation link.'}
   
    if request.method == 'POST':
        profile_form = ProfileUpdateForm(request.POST)
        if profile_form.is_valid():
            profile.user.first_name = profile_form.cleaned_data['first_name']
            profile.user.last_name = profile_form.cleaned_data['last_name']
            profile.user.save()
            #profile.tshirt_size = profile_form.cleaned_data['tshirt_size'] 
            #profile.pre_party = profile_form.cleaned_data['pre_party']
            #profile.ticket_barcode = profile_form.cleaned_data['ticket_barcode']
            profile.twitter_name = profile_form.cleaned_data['twitter_name']
            profile.blog = profile_form.cleaned_data['blog']
            profile.linkedin = profile_form.cleaned_data['linkedin']
            profile.facebook = profile_form.cleaned_data['facebook']
            profile.kyivpy2 = profile_form.cleaned_data['kyivpy2']
            profile.agree = profile_form.cleaned_data['agree']
            profile.public = profile_form.cleaned_data['public']
            profile.save()
    else:
        profile_form = ProfileUpdateForm(initial={'first_name': profile.user.first_name,
                                                 'last_name': profile.user.last_name,
                                                 #'tshirt_size': profile.tshirt_size,
                                                 #'pre_party': profile.pre_party,
                                                 #'ticket_barcode': profile.ticket_barcode,
                                                 'twitter_name': profile.twitter_name,
                                                 'blog': profile.blog,
                                                 'linkedin': profile.linkedin,
                                                 'facebook': profile.facebook,
                                                 'kyivpy2': profile.kyivpy2,
                                                 'agree': profile.agree,
                                                 'public': profile.public,})
    speakers = Speaker.objects.all()
    return {'profileform': profile_form, 'completed': profile.is_profile_completed,
            'speakers': speakers}

@login_required
@render_to('cfp.html')
def cfpsubmission(request):
    return HttpResponseRedirect('/')
    user = request.user
    profile = get_object_or_404(ParticipanProfile, user=user)
    speakers = Speaker.objects.all()
    if not profile.active:
       logout(request)
       return {'error': 'You profile haven\'t been activated. Please recheck you email for activation link.',
               'speakers': speakers}
    
    success = False
    if request.method == 'POST':
        cfp_form = CFPSubmissionForm(request.POST, request.FILES)
        if cfp_form.is_valid():
            cfp = CFPProfile.objects.create(user=user, **cfp_form.cleaned_data)
            cfp.save()
            from django.core.mail import mail_admins
            mail_admins('[PyCON UKRAINE SITE]: User %s (%s %s) submited new CFP' % (profile.user.username, profile.user.first_name, profile.user.last_name),
                        'You can check CFP here http://ua.pycon.org/admin/core/cfpprofile/%d/' %cfp.pk)
            
            success = True
    else:
        cfp_form = CFPSubmissionForm()
    
    return {'cfp_form': cfp_form, 'success': success, 'speakers': speakers}

@login_required
@render_to('freeparticipantapply.html')
def freeparticipantapply(request):
    user = request.user
    profile = get_object_or_404(ParticipanProfile, user=user)
    speakers = Speaker.objects.all()
    if not profile.active:
       logout(request)
       return {'speakers': speakers,
               'error': 'You profile haven\'t been activated. Please recheck you email for activation link.'}
    
    if profile.is_profile_completed:
        return {'speakers': speakers,
                'error': 'You profile already marked as completed. You not need to apply for Free Participant status.'}

    success = False
    if request.method == 'POST':
        applyform = FreeParticipantApplyForm(request.POST)
        if applyform.is_valid():
            profile.pykyiv_speaker = applyform.cleaned_data['pykyiv_speaker']
            profile.invited_speaker = applyform.cleaned_data['invited_speaker']
            profile.help_team = applyform.cleaned_data['help_team']
            profile.organizator = applyform.cleaned_data['organizator']
            profile.sponsor_participant = applyform.cleaned_data['sponsor_participant']
            profile.save()
            from django.core.mail import mail_admins
            mail_admins('[PyCON UKRAINE SITE]: User %s (%s %s) applied for free status' % (profile.user.username, profile.user.first_name, profile.user.last_name),
                        'You can check user\'s application at the http://ua.pycon.org/admin/core/participanprofile/%d/' %profile.pk)
            success = True
    else:
        applyform = FreeParticipantApplyForm()
    
    return {'applyform': applyform, 'success': success, 'speakers': speakers}

@render_to('news_page.html')
def news(request, pk):
    news = get_object_or_404(News, pk=pk)
    speakers = Speaker.objects.all()
    return {'news': news, 'speakers': speakers}


@render_to('talks.html')
def talks(request):
    talks = Talks.objects.all().order_by('-ordering')
    speakers = Speaker.objects.all()
    return {'talks':talks, 
            'speakers': speakers}
