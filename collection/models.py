# don't forget to import this
from django.contrib.auth.models import User
from django.db import models

class Thing(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    # the new line we're adding
    user = models.ForeignKey(User, unique=True, blank=True, null=True, related_name="users")
    
