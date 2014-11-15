from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    ttype = models.CharField(max_length = 200)
    time = models.DateTimeField('date published')
    details = models.TextField()
    link = models.CharField(max_length = 2083)
    user = models.ForeignKey('Use')
    title = models.CharField(max_length = 200)
    image = models.ImageField(null = True)

class Use(User):
    pass
# Create your models here.
