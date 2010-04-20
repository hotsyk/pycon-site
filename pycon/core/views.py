from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.utils import simplejson
from django.http import HttpResponse
from django.template import RequestContext
from django.template import loader, Context

from pycon.core.decorators import render_to

__all__ = ('index')

@render_to('index.html')
def index(request):
    context = {}
    return context