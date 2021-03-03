from django.db import models
from django.urls import reverse
import datetime

# Create your models here.

PRIORITY = (('danger','high'),('info','normal'),('success','low'))
class TodoModel(models.Model):
    title = models.CharField(max_length=100,blank=True)
    x = models.CharField(max_length=100,blank=True)
    y = models.CharField(max_length=100,blank=True)
    radius = models.CharField(max_length=100,blank=True)
    memo = models.TextField()
    priority = models.CharField(
        max_length = 50,
        choices = PRIORITY
    )
    duedate = models.DateTimeField()
   
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField('タイトル', max_length=255)

    def __str__(self):
        return self.title