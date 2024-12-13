from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    FormView,
    CreateView,
)

from django.contrib import messages
from django.urls import reverse
from datetime import datetime
from products.models import Product
from .models import Review
from .forms import CommentForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.db.models import Avg
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def apply_verified_reviewer(request):
    if not request.user.verifiedReviewer:
        request.user.verifiedReviewer = False
        request.user.save()
        messages.success(request, "You are now a verified reviewer!")
    else:
        messages.info(request, "You are already a verified reviewer.")
    return redirect("profile")


@login_required
def profile_view(request):
    return render(request, "profile.html")


# def profile_view(request):
# return render(request, "profile.html", {"user": request.user})


@login_required
def upload_profile_picture(request):
    if request.method == "POST" and request.FILES.get("profile_picture"):
        picture = request.FILES["profile_picture"]
        request.user.profile_picture.save(picture.name, picture)
        messages.success(request, "Profile picture updated successfully!")
    else:
        messages.error(request, "Please upload a valid picture.")
    return redirect("profile")


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.annotate(
            avg_rating=Avg("ratings__average")
        ).order_by("-avg_rating")[:3]
        context["products"] = Product.objects.all()[:4]

        context["latest_reviews"] = Review.objects.order_by("-date")[:5]
        context["current_year"] = datetime.now().year

        return context


# class ReviewDetailView(View):


class ReviewListView(ListView):
    model = Review
    template_name = "review_list.html"


class CommentGet(DetailView):
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

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Review, pk=pk)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.review = self.object
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
    template_name = "searchReview.html"
    context_object_name = "all_search_results"

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get("searchRev")
        if query:
            postresult = (
                Review.objects.filter(title__contains=query)
                or Review.objects.filter(game__contains=query)
                or Review.objects.filter(body__contains=query)
            )
            result = postresult
        else:
            result = None
        return result


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    template_name = "new_review.html"
    fields = ["title", "author", "body", "image"]
    success_url = reverse_lazy("review_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("review_list")


def update_bio(request):
    if request.method == "POST":
        new_bio = request.POST.get("bio")
        if new_bio:
            request.user.bio = new_bio
            request.user.save()
            messages.success(request, "Bio updated successfully!")
        else:
            messages.error(request, "Bio cannot be empty.")
    return redirect("profile")
