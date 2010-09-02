from django.contrib import admin
from pycon.core.models import *

def barcode(obj):
    return obj.ticket_barcode != ''
barcode.short_description = 'Barcode'

class ParticipanProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'tshirt_size', 'pre_party',
                    'country', 'city', 'python_level',
                    'python_years', 'active',
                     barcode)
        
        
admin.site.register(Page)
admin.site.register(News)
admin.site.register(Speaker)
admin.site.register(CFPProfile)
admin.site.register(ParticipanProfile, ParticipanProfileAdmin)