from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    """ adding a new field to userprofile"""
    user = models.OneToOneField(User)
    postfolio = models.CharField(blank=True, max_length=25)
    profile_pic = models.ImageField(blank=True, upload_to='profile_pic')

    def __str__(self):
        """ return user name"""
        return self.user.username
