from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.urls import reverse

from .models import Product

# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"