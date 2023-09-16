from rest_framework import serializers
from .models import TravelItem, Review

class TravelItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelItem
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['author', 'content', 'created_at']