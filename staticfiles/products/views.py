from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.urls import reverse

from .models import Product

# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"

class ProductDetailView(DetailView):
    # model = Product
    template_name = "product_detail.html"

    def get(self, request, pk, *args, **kwargs):
        product = get_object_or_404(Product, pk=pk)
        return render(request, self.template_name, {"product": product})
    

class SearchView(ListView):
    model = Product
    template_name = 'searchProduct.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = Product.objects.filter(name__contains=query)
            result = postresult
        else:
            result = None
        return result