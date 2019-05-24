from django.db import models
from django.utils.timezone import now

# Create your models here.

class Twice(models.Model):
    nations_choice = (
        ('KR', '대한민국'),
        ('JP', '일본'),
        ('TW', '대만')
    )
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    birth = models.DateTimeField(default=now)
    nationality = models.CharField(max_length=5, choices=nations_choice)
    position = models.TextField()

    def __str__(self):
        return self.name

