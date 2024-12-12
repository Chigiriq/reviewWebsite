from django.urls import path
from .views import SignUpView, ProfileDetail, apply_verified_reviewer
from . import views


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    # path("login/", LoginView.as_view(), name="login"),
    # path("<int:pk>/", ProfileDetail.as_view(), name = "profile")
    path("profile/", ProfileDetail.as_view(), name="profile"),
    path(
        "apply-verified-reviewer/",
        apply_verified_reviewer,
        name="apply_verified_reviewer",
    ),
    path("profile/<str:username>/", views.user_profile, name="user_profile"),
]
