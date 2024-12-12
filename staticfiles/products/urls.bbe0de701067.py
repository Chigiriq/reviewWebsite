from django.urls import path
from .views import ProductListView, ProductDetailView, SearchView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("results/", SearchView.as_view(), name="search"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
