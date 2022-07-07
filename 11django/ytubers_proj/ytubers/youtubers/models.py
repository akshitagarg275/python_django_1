from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Youtuber(models.Model):
    crew_choices = (
        ('solo' , 'solo'),
        ('small_team','SM'),
        ('large_team','large_team')
    )

    camera_choices = (
        ('sony','sony'),
        ('canon','canon'),
        ('fuji','fuji')
    )

    category_choices = (
        ('cooking','cooking'),
        ('tech','tech'),
        ('educational','educational'),
        ('vlog','vlog'),
        ('comedy','comedy')
    )

    name= models.CharField(max_length=250)
    email=models.EmailField()
    city=models.CharField(max_length=200)
    desc=RichTextField()
    video_url=models.CharField(max_length=50)
    price=models.CharField(max_length=10)
    age=models.IntegerField(null=True,blank=True)
    height=models.IntegerField()
    subs_count=models.IntegerField()
    is_featured=models.BooleanField(default=False)
    crew=models.CharField(choices=crew_choices,max_length=100)
    camera_type=models.CharField(choices=camera_choices,max_length=100)
    category=models.CharField(choices=category_choices,max_length=100)
    photo=models.ImageField(upload_to='media/youtubers/%Y/%m/%D')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name