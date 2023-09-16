from rest_framework import generics
from .models import GreenInitiative
from .serializers import GreenInitiativeSerializer

class GreenInitiativeListCreateView(generics.ListCreateAPIView):
    queryset = GreenInitiative.objects.all()
    serializer_class = GreenInitiativeSerializer

class GreenInitiativeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GreenInitiative.objects.all()
    serializer_class = GreenInitiativeSerializer

