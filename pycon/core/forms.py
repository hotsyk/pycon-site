from django import forms

from django.contrib.auth.models import User
from pycon.core.models import *
from pycon.core.fields import *

class ParticipantRegistrationForm(forms.ModelForm):
    
    first_name = forms.CharField(label="First name")
    last_name = forms.CharField(label="Last name")
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget = forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget = forms.PasswordInput,
                                label="Retype password")
    recaptcha = ReCaptchaField()
    
    class Meta:
        model = ParticipanProfile
        exclude = ('user', 'active', 'verification_code')
        fields = ['first_name', 'last_name', 'email', 'password', 'password2',
                  'country', 
                  'city', 'phone', 'python_level',
                  'python_years', 
                  'tshirt_size', 'pre_party', 'ticket_barcode',
                  'organization', 'occupation', 'twitter_name',
                  'blog', 'linkedin',
                  'facebook', 'recaptcha' ]
        
    def clean_email(self):
        email = self.cleaned_data['email']
        
        if User.objects.filter(email=email).count()>0:
            raise forms.ValidationError('This email is already in use')
        return email

    def clean(self):
        super(ParticipantRegistrationForm, self).clean()
        cleaned_data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2:
            if password != password2:
                raise forms.ValidationError('Passwords don\'t match')
        return cleaned_data   
    
class ProfileUpdateForm(forms.ModelForm):
    
    first_name = forms.CharField(label="First name")
    last_name = forms.CharField(label="Last name")
    
    class Meta:
        model = ParticipanProfile
        exclude = ('user', 'active', 'verification_code')
        fields = ['first_name', 'last_name',
                  'tshirt_size', 'pre_party', 'ticket_barcode',
                  'twitter_name',
                  'blog', 'linkedin',
                  'facebook', ]
        
class CFPSubmissionForm(forms.ModelForm):
    
    class Meta:
        model = CFPProfile
        exclude = ('user', 'inrating')

class FreeParticipantApplyForm(forms.ModelForm):
    
    class Meta:
        model = ParticipanProfile
        fields = ['pykyiv_speaker', 'invited_speaker', 'help_team', 'organizator',
                  'sponsor_participant']
        
        
       