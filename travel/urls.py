from django.urls import path
from .views import TravelItemListCreateView, TravelItemDetailView
from . import views

urlpatterns = [
    path('items/', TravelItemListCreateView.as_view(), name='item-list-create'),
    path('items/<int:pk>/', TravelItemDetailView.as_view(), name='item-detail'),
    path('travel_item/<int:item_id>/reviews/', views.TravelItemReviewsView.as_view(), name='travel_item_reviews'),
    path('review/<int:review_id>/', views.ReviewDetailView.as_view(), name='review_detail'),
    path('favorites/', views.FavoriteItemListCreateView.as_view(), name='favorite-list-create'),
    path('favorites/<int:pk>/', views.FavoriteItemDetailView.as_view(), name='favorite-detail'),
]