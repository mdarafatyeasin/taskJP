from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class recipe (models.Model):
    title = models.CharField(max_length=100)
    description = models.Model(models.TextField())

    