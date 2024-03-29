from distutils.command.upload import upload
from email.policy import default
from statistics import mode
from django.db import models
from users.models import Profile
import uuid
# Create your models here.

class Project(models.Model):
    owner =models.ForeignKey(Profile , null=True , blank=True , on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True  , null= True)
    featured_image = models.ImageField(null = True , blank =True , default = 'default.jpg')
    demo_link = models.CharField(max_length=255)
    source_link = models.CharField(max_length=255)
    tags = models.ManyToManyField('Tag',blank=True)
    vote_total = models.IntegerField(default=0, null=True , blank= True)
    vote_ratio=models.IntegerField(default=0,null=True , blank=True)
    created_at= models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4 , unique=True , primary_key=True,editable=False)

    def __str__(self):
        return self.title

class Review(models.Model):
    VOTE_TYPE = (
        ('Up Vote', 'Up Vote'),
        ('Down Vote ', 'Down Vote')
    )
    #owner 
    project = models.ForeignKey(Project , on_delete=models.CASCADE)
    body = models.TextField(blank=True,null=True)
    value = models.CharField(choices=VOTE_TYPE,max_length=50)
    created_at= models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4 , unique=True , primary_key=True,editable=False)

    def __str__(self):
        return self.project
    
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created_at= models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4 , unique=True , primary_key=True,editable=False)
    
    def __str__(self):
        return self.name
