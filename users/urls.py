from django.urls import path
from .views import SignUpView, ProfileDetail

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    #path("<int:pk>/", ProfileDetail.as_view(), name = "profile")
    path('profile/', ProfileDetail.as_view(), name="profile"),
]
