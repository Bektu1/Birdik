from rest_framework import serializers
from .models import GreenInitiative

class GreenInitiativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GreenInitiative
        fields = '__all__'
