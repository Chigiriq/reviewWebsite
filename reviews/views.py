from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView
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