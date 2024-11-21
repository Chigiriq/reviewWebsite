from django.urls import path
from .views import ProductListView, ProductDetailView, SearchView

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path('results/', SearchView.as_view(), name='search')
]