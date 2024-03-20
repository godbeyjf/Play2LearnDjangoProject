from django.conf import settings
from django.db import models

class Score(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    game = models.CharField(max_length=200)
    score = models.IntegerField()

class GameRecord(models.Model):
    GAME_CHOICES = [
        ('MathGame', 'Math Facts Practice'),
        ('AnagramGame', 'Anagram Hunt'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_finished = models.DateTimeField(auto_now_add=True)
    game_type = models.CharField(max_length=200, choices=GAME_CHOICES)
    game_settings = models.JSONField(default=dict)
    final_score = models.IntegerField()
# Create your models here.
