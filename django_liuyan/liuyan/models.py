from django.db import models
# Create your models here.
class Comment(models.Model):
    name=models.CharField(max_length=1024)
    text=models.TextField()
    date_time=models.DateTimeField()