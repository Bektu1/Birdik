
from django.urls import path

from . import views

urlpatterns = [
    path('pay/', views.HomePageView.as_view(), name='home'),
]