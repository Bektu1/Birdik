from django.urls import path
from .views import GreenInitiativeListCreateView, GreenInitiativeRetrieveUpdateDestroyView

urlpatterns = [
    path('initiatives/', GreenInitiativeListCreateView.as_view(), name='initiative-list-create'),
    path('initiatives/<int:pk>/', GreenInitiativeRetrieveUpdateDestroyView.as_view(), name='initiative-retrieve-update-destroy'),
]
