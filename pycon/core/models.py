from django.db import models
from django.contrib.auth.models import User

from sorl.thumbnail.fields import ImageWithThumbnailsField

          
class Page(models.Model):
    
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    
    

class News(models.Model):
    
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    
    short = models.TextField()
    long = models.TextField(blank=True, null=True)
    
    
    
class Speaker(models.Model):
    
    name = models.CharField(max_length=255)
    photo = ImageWithThumbnailsField(upload_to='profiles',
                                     thumbnail={'size': (50, 50)})
    
    bio = models.TextField(blank=True, null=True)       
    email = models.EmailField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    site = models.URLField(blank=True, null=True)
    
    comments = models.TextField(blank=True, null=True)
    
    
class CFPProfile(models.Model):
    
    user = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    
class Country(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=4) 
    
    def __unicode__(self):
        return self.name      
        
class ParticipanProfile(models.Model):
    TSHIRTCHOICES = (('S', 'Small'),
                     ('M', 'Medium'),
                     ('L', 'Large'),
                     ('XL', 'X-Large'))
    PYTHONLEVEL = (('0', 'Novice'),
                   ('1', 'Junior'),
                   ('2', 'Middle'),
                   ('3', 'Experienced'),
                   ('4', 'Master'),
                   ('5', 'Sensei'))
    
    PYTHONYEARS = (('0', "Haven't worked before"),
                   ('1', '<= 1 y.'),
                   ('2', '1-2 y.'),
                   ('3', '2-3 y.'),
                   ('4', '3-5 y.'),
                   ('5', '>5 y.'))
    
    user = models.ForeignKey(User)
    tshirt_size = models.CharField(max_length=1, choices=TSHIRTCHOICES,
                                   help_text='Yes, we all get a t-shirt!')      
    pre_party = models.BooleanField(default=False, 
                                    help_text='Do you intend to attend the pre-conference party on Friday?')
    ticket_barcode = models.CharField(max_length=10, blank=True, null=True,
                                      help_text='Please, enter barcode from your ticket')
    organization = models.CharField(max_length=255, blank=True, null=True,
                                    help_text='The primary organisation that you are a member of.')
    occupation = models.CharField(max_length=255, blank=True, null=True,
                                  help_text="Title of your occupation")    
    country = models.ForeignKey(Country, help_text='Country of residence')
    city = models.CharField(max_length=255, blank=True, null=True,
                            help_text='City of residence')
    
    
    phone = models.CharField(max_length=15, blank=True, null=True,
                              help_text='For notification purposes only. Phone will not be passed to any other organisation or person')
    python_level = models.CharField(max_length=1, choices=PYTHONLEVEL,
                                    help_text='How can you describe your Python level.')
    python_years = models.CharField(max_length=1, choices=PYTHONYEARS,
                                    help_text='How long do you work with Python')
    twitter_name = models.CharField(max_length=105, blank=True, null=True,
                                    help_text='Your Twitter nickname')
    blog = models.URLField(blank=True, null=True,
                                    help_text="Your blog's url")
    linkedin = models.URLField(blank=True, null=True,
                                    help_text="Your LinkedIn's profile's url")
    facebook = models.URLField(blank=True, null=True,
                                    help_text="Your Facebook's profile's url")
    date_of_registration = models.DateTimeField(auto_now_add=True)
    
    active = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=255, blank=True, null=True)
            