from django.db import models

# Create your models here.
class Song(models.Model):
    id = models.CharField(primary_key=True)
    playlist_name = models.CharField()
    playlist_id = models.CharField(null=True)
    name = models.CharField()
    converted = models.BooleanField(default=False)