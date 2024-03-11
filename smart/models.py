from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from base64 import b64encode
from django import template



class userData1(models.Model):
    username = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(null=False,unique=True)
    password = models.CharField(max_length=128)
    is_active=models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login=models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return self.username

class pictureModel(models.Model):
    TYPE_CHOICES=[
        ('theme','Theme'),
        ('cradle','Cradle'),
        ('cake','Cake'),
        ('decoration','Decoration'),
        ('entertainment','Entertainment'),
        ('balloons','Balloons'),    
    ]
    pic_name=models.CharField(max_length=50)
    pic=models.FileField(upload_to='pictures/')
    pic_type=models.CharField(max_length=50,choices=TYPE_CHOICES)
    def __str__(self):
        return self.pic_name
    
class HistoryModel(models.Model):
    form_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    theme=models.CharField(max_length=50,null=True)
    cake=models.CharField(max_length=50,null=True)
    cradle=models.CharField(max_length=50,null=True)
    decoration=models.CharField(max_length=50,null=True)
    entertainment=models.CharField(max_length=50,null=True)
    balloons=models.CharField(max_length=50,null=True)
    guest=models.IntegerField()
    date=models.DateField()
    planner=models.CharField(max_length=100,null=True,blank=True)
    booked_on=models.DateTimeField(default=timezone.now)
    status=models.BooleanField(default=True)
    location=models.CharField(max_length=50)
    suggest=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.username 
    

class VolunteerModel(models.Model):
    vname = models.CharField(max_length=100)
    vmobile = models.CharField(max_length=15)
    vemail = models.EmailField(null=False,unique=True)
    address = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    date_joined = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.vname
    
class GalleryModel(models.Model):
    TYPE_CHOICES=[
        ('wedding','Wedding'),
        ('birthday','Birthday'),
        ('anniversary','Anniversary'),
        ('party','Party'),
        ('cradle','Cradle'),   
    ]
    pic=models.FileField(upload_to='pictures/')
    pic_type=models.CharField(max_length=50,choices=TYPE_CHOICES)
    def __str__(self):
        return self.pic_type