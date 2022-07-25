from django.db import models
from datetime import datetime
# Create your models here.

class Hiretuber(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    tuber_id = models.IntegerField()
    user_id = models.IntegerField()
    tuber_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.email
