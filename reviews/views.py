from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from .models import Review

class HomePageView(TemplateView):
    template_name = "home.html"

# class ReviewDetailView(View):

class ReviewListView(View):
    model = Review
    template_name = "review_list.html"