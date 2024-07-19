# listings/views.py
from rest_framework import generics, filters
from .models import Shop, Listing
from .serializers import ShopSerializer, ListingSerializer

class ShopListingsView(generics.ListCreateAPIView):
    serializer_class = ListingSerializer

    def get_queryset(self):
        return Listing.objects.filter(shop_id=self.kwargs['shopId'])

    def perform_create(self, serializer):
        shop = Shop.objects.get(id=self.kwargs['shopId'])
        serializer.save(shop=shop)

class ListingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class ListingSearchView(generics.ListAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'shop__name']
    ordering_fields = ['price', 'created_at']

class ShopCreateView(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
