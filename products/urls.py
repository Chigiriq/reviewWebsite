from django.urls import path
from .views import ProductListView

urlpatterns = [
    # path("", ReviewListView.as_view(), name="review_list"),
    # path("<int:pk>/", ReviewDetailView.as_view(), name="review_detail"),
    path("", ProductListView.as_view(), name="product_list"),
    # path()
]