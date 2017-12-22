from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('author', 'id', 'title', 'description', 'day', 'starting_time', 'end_time')
