from pyexpat import model
from rest_framework import serializers
from .models import Events


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Events
        fields=['id','event_name','participent_name','participent_address']
        


