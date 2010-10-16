from django.contrib import admin
from pycon.core.models import *

def barcode(obj):
    return obj.ticket_barcode != ''
barcode.short_description = 'Barcode'

def is_profile_complete(obj):
    return obj.is_profile_completed
is_profile_complete.short_description = 'Completed'

class ParticipanProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'tshirt_size', 'pre_party',
                    'country', 'city', 'python_level',
                    'python_years', 'active',
                     barcode, is_profile_complete)
        
        
admin.site.register(Page)
admin.site.register(News)
admin.site.register(Speaker)
admin.site.register(CFPProfile)
admin.site.register(ParticipanProfile, ParticipanProfileAdmin)
admin.site.register(Talks)