from django.conf import settings
from django.db import models

class Score(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    game = models.CharField(max_length=200)
    score = models.IntegerField()

# Create your models here.
