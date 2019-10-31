from django.db import models
from django.shortcuts import reverse
import datetime


# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=250)
    date = models.DateField(default=datetime.datetime.today())
    location = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('pictureQ:album-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Photo(models.Model):
    album = models.ForeignKey(Album, null=True, blank=True, on_delete=models.CASCADE)
    photo_title = models.CharField(null=True, blank=True, max_length=50)
    photo_desc = models.CharField(null=True, blank=True, max_length=250)
    photo_date = models.DateField(null=True, blank=True, default=datetime.datetime.today())
    photo_location = models.CharField(null=True, blank=True, max_length=50)
    image = models.ImageField(null=True, blank=True)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('pictureQ:photo-detail', kwargs={'pk': self.pk})
