from django.db import models

# Create your models here.

from embed_video.fields import EmbedVideoField

class tutorial(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    video = EmbedVideoField()  # same like models.URLField()
    
    def  __str__(self):
        return  str(self.title) if  self.title  else  " "
