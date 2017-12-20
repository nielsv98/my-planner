from django.db import models
from django.utils import timezone

class Event(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    description = models.TextField()
    day = models.CharField(default="Monday", max_length=9)
    starting_time = models.CharField(max_length=5)
    end_time = models.CharField(max_length=5)

    def publish(self):
        self.starting_time = timezone.now()
        self.save()

    def __str__(self):
        return self.title
