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
    CFP_TYPE_CHOICES = (('L', 'Lightning talk'),
                     ('T', 'Talk'),
                     ('M', 'Master class'),
                     ('U', 'Tutorial'),
                     ('P', 'Pecha Kucha'))

    CFP_LENGTH = (('1', '5 minutes (Lightning talk)'),
                     ('2', '6 minutes 40 seconds (Pecha Kucha)'),
                     ('3', '20 minutes'),
                     ('4', '30 minutes'),
                     ('5', '45 minutes'),
                     ('6', '60 minutes'),
                     )   
    
    CFP_AUDIENCE = (('0', 'Beginners'),
                   ('1', 'Intermediate'),
                   ('2', 'Advanced'),
                   ('3', 'General interest'),                   
                   )     
    
    CFP_CATEGORIES = (('0', 'Web Programming'),
                      ('1', 'UI Programming'), 
                      ('2', 'Python Language'),
                      ('3', 'Alternative Implementations'),
                      ('4', 'Python in Action'),
                      ('5', 'Testing'),
                      ('6', 'Documentation, Tools & Library'),
                      ('7', 'Mobile Computing'),
                      ('8', 'Multimedia'),
                      ('9', 'Community'),
                      ('10', 'Education'),
                      ('11', 'Build, Packaging & Deployment'), 
                      ('12', 'Science'),
                      ('13', 'Databases'),
                      ('14', 'Python 3'),
                      ('15', 'Security'),
                      ('16', 'Games Programming'),
                      ('17', 'Network'),
                      ('18', 'GIS'),
                      ('19', 'Highload'),
                      ('20', 'Other')) 

    user = models.ForeignKey(User)
    title = models.CharField(max_length=255, help_text='Title of your proposed talk')
    type = models.CharField(max_length=1, choices=CFP_TYPE_CHOICES, default='L',
                            help_text="Pecha Kucha format is experimental and decision if it is availble on the PyCon Ukraine will appears on results of the CFP")
    proposed_length = models.CharField(max_length=1, default='0', choices=CFP_LENGTH)
    oneliner = models.CharField(max_length=255, help_text='Description of your CFP in 255 chars')
    target_audience = models.CharField(max_length=1, choices=CFP_AUDIENCE, default='0')
    category = models.CharField(max_length=2, choices=CFP_CATEGORIES, default='20',
                                help_text="Don't worry if your talk fits into multiple categories, just choose one")
    abstract = models.TextField(help_text='Abstract description of your talk.')
    brief_biography = models.TextField(help_text='Tell us about yourself. This is a community conference, so no need to be shy!')
    comments = models.TextField(blank=True, null=True, help_text="Also enter here the name and email of co-presenter if any. Email should be the email he or she used while registration.")
    photo = ImageWithThumbnailsField(help_text="Your photo", upload_to='cfp',
                                     thumbnail={'size': (50, 50)})
    inrating = models.BooleanField(default=True)
    
class Country(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=4) 
    
    def __unicode__(self):
        return self.name      
        
class ParticipanProfile(models.Model):
    TSHIRTCHOICES = (('S', 'Small'),
                     ('M', 'Medium'),
                     ('L', 'Large'),
                     ('X', 'X-Large'))
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
    
    pykyiv_speaker = models.BooleanField("I was the PyCamp Kyiv speaker", default=False)
    pycon_speaker = models.BooleanField("I am the PyCon Ukraine speaker", default=False)
    invited_speaker = models.BooleanField("I am invited speaker", default=False)
    help_team = models.BooleanField("I am member of help team", default=False)
    organizator = models.BooleanField("I am member of organizers team", default=False)
    sponsor_participant = models.BooleanField("I am employee of the PyCon Ukraine sponsor", default=False)
    confirmed_free = models.BooleanField(default=False)
    
    @property
    def is_profile_completed(self):
        return self.ticket_barcode != '' or ((self.pycon_speaker or\
         self.pykyiv_speaker or self.invited_speaker or self.organizator or\
         self.help_team or self.sponsor_participant) and self.confirmed_free)   