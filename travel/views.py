from rest_framework import generics
from .models import TravelItem, Review, FavoriteItem
from .serializers import TravelItemSerializer, ReviewSerializer, FavoriteItemSerializer
from rest_framework.permissions import IsAuthenticated

class TravelItemListCreateView(generics.ListCreateAPIView):
    queryset = TravelItem.objects.all()
    serializer_class = TravelItemSerializer

class TravelItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TravelItem.objects.all()
    serializer_class = TravelItemSerializer

class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        travel_item_id = self.kwargs['item_id']
        travel_item = TravelItem.objects.get(pk=travel_item_id)
        serializer.save(travel_item=travel_item)

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class TravelItemReviewsView(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        item_id = self.kwargs['item_id']
        return Review.objects.filter(travel_item=item_id)
    

class FavoriteItemListCreateView(generics.ListCreateAPIView):
    queryset = FavoriteItem.objects.all()
    serializer_class = FavoriteItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FavoriteItemDetailView(generics.RetrieveDestroyAPIView):
    queryset = FavoriteItem.objects.all()
    serializer_class = FavoriteItemSerializer
    permission_classes = [IsAuthenticated] 
