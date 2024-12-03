from django.shortcuts import render
from django.views.generic import CreateView, DetailView, TemplateView, UpdateView
from django.urls import reverse_lazy
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CustomUserCreationForm

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

