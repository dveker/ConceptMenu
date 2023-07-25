from django.db import models

class Member(models.Model):
  food = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  image = models.ImageField(upload_to='images/')