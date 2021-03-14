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
    memo = models.TextField(blank=True,null=True)
    priority = models.CharField(
        max_length = 50,
        choices = PRIORITY,
        blank=True,null=True
    )
    duedate = models.DateTimeField(blank=True,null=True)
    article = models.CharField( max_length=100,blank=True,null=True)
    start = models.DateTimeField( blank=True,null=True)
    end = models.DateTimeField( blank=True,null=True)
    company = models.CharField( max_length=100,blank=True,null=True)
    floor = models.CharField( max_length=100,blank=True,null=True)
   
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField('タイトル', max_length=255)

    def __str__(self):
        return self.title

class Reservation(models.Model):
    article = models.CharField( max_length=100,blank=True,null=True)
    start = models.DateTimeField( blank=True,null=True)
    end = models.DateTimeField( blank=True,null=True)
    company = models.CharField( max_length=100,blank=True,null=True)
    floor = models.CharField( max_length=100,blank=True,null=True)

    def __str__(self):
        return self.article

class Reserve(models.Model):
    article = models.CharField( max_length=100,blank=True,null=True)
    start = models.DateTimeField( blank=True,null=True)
    end = models.DateTimeField( blank=True,null=True)
    company = models.CharField( max_length=100,blank=True,null=True)
    floor = models.CharField( max_length=100,blank=True,null=True)

    def __str__(self):
        return self.article
