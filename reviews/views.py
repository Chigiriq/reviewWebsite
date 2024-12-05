from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView
from django.urls import reverse

from .models import Review
from .forms import CommentForm

class HomePageView(TemplateView):
    template_name = "home.html"

# class ReviewDetailView(View):

class ReviewListView(ListView):
    model = Review
    template_name = "review_list.html"


class CommentGet(DetailView):  # new
    model = Review
    template_name = "review_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

class CommentPost(FormView):  # new
    model = Review
    form_class = CommentForm
    template_name = "review_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        review = self.object
        return reverse("review_detail", kwargs={"pk": review.pk})

class ReviewDetailView(View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)
    
class SearchView(ListView):
    model = Review
    template_name = 'searchReview.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('searchRev')
        if query:
            postresult = Review.objects.filter(title__contains=query) or Review.objects.filter(game__contains=query) or Review.objects.filter(body__contains=query)
            result = postresult
        else:
            result = None
        return result
    
class ReviewCreateView(CreateView):
    model = Review
    template_name = "new_review.html"
    fields = ["title", "author", "body"]
        