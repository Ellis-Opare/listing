# listings/urls.py
from django.urls import path
from . import views
from .views import ShopListingsView, ListingDetailView, ListingSearchView, ShopCreateView

urlpatterns = [
    path('shops/<int:shopId>/listings/', ShopListingsView.as_view(), name='shop-listings'),
    path('listings/<int:pk>/', ListingDetailView.as_view(), name='listing-detail'),
    path('listings/search/', ListingSearchView.as_view(), name='listing-search'),
    path('shops/', ShopCreateView.as_view(), name='shop-create'),

]
