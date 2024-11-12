from django.urls import path
from .views import HomePageView, ReviewListView

urlpatterns = [
    # path("", HomePageView.as_view(), name="home"),
    # path("<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path("", ReviewListView.as_view(), name="review_list"),
]
