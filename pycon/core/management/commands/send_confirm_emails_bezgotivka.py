from django.core.management.base import BaseCommand, CommandError
from django.core.mail import EmailMultiAlternatives
from django.template import RequestContext
from django.template import loader, Context

from pycon.core.models import *


class Command(BaseCommand):

    def handle(self, *args, **options):
        for participant in ParticipanProfile.objects.filter(paid_bezgotivka=True, confirmed_free=True):
            context = {'user': participant.user}
            t = loader.get_template("email-bezgotivka.html")
            text_content = t.render(Context(context))
            subject, from_email, to = 'PyCon Ukraine 2010: Participant confirmation',\
                                'do-not-reply@ua.pycon.org', participant.user.email
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.send()
        