from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    content = models.TextField()
