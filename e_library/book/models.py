from django.db import models
from django.utils import timezone
class Book(models.Model):
    name=models.CharField(max_length=20)
    author=models.CharField(max_length=30)
    price=models.IntegerField(default=0)
    publish_date = models.DateField(default=timezone.now)
# Create your models here.
