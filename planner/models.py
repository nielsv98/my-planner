from django.db import models
from django.utils import timezone


class Event(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    description = models.TextField()
    starting_time = models.DateTimeField(
            blank=True, null=True)
    end_time = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.starting_time = timezone.now()
        self.save()

    def __str__(self):
        return self.title
