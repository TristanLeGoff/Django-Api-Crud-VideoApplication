from django.db import models
import datetime
# Create your models here.
class History(models.Model):
    video_link = models.CharField(max_length=200)
    date_field = models.DateTimeField(default=datetime.datetime.now())

class Bookmark(models.Model):
    bookmark_link = models.CharField(max_length=200)