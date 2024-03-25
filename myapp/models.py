from ast import Try
from django.db import models
from django.contrib.auth.models import User
from pytz import timezone

# Create your models here.
class ModelAuthor(models.Model):
    username = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return self.username

class ModelPost(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Post from {} created at {}".format(self.content, self.created)

    class Meta:
        pass
    
    def get_absolute_url(self):
        return '/list/'

class ModelProduct(models.Model):
    name = models.CharField(max_length=200, null=True)
    brand = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)

    def str(self):
        return self.name

    @property
    def imageURL(self):
        try:
           url = self.image.url
        except:
            url = ''
        return url


