from django.db import models

# Create your models here.
class Task(models.Model):
  title=models.CharField(max_length=100)
  desc=models.TextField()

class History(models.Model):
  title=models.CharField(max_length=100)
  desc=models.TextField()