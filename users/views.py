from django.shortcuts import render
from django.views.generic import CreateView, DetailView, TemplateView, UpdateView
from django.urls import reverse_lazy
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404


@login_required
def apply_verified_reviewer(request):
    user = request.user
    if user.review_request_status == "Pending":
        messages.warning(request, "Your application is already pending.")
    elif user.review_request_status == "Approved":
        messages.info(request, "You are already a verified reviewer.")
    else:
        user.review_request_status = "Pending"
        user.save()
        messages.success(request, "Your application has been submitted.")
    return redirect("profile")


def user_profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    return render(request, "user_profile.html", {"user": user})


# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class ProfileDetail(LoginRequiredMixin, TemplateView):
    model = CustomUser
    template_name = "profile.html"


class PasswordChangeView(UpdateView):
    model = CustomUser
    template_name = "password_change_view.html"
    fields = ["Old Password", "New Password", "Confirm New Password"]
