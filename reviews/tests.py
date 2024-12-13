# reviews/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Review
from django.contrib.auth import get_user_model
from django.conf import settings

settings.DEBUG = True

CustomUser = get_user_model()


class ReviewViewsTest(TestCase):

    def setUp(self):
        # Create a CustomUser instance
        self.user = CustomUser.objects.create_user(
            username="testguy",
            email="testguy@example.com",
            password="password123",
            verifiedReviewer=True,
        )
        self.client.login(username="testguy", password="password123")

        self.review = Review.objects.create(
            title="Test Review",
            body="This is a test review description.",
            author=self.user,
        )

    def test_review_create_view(self):
        response = self.client.get(reverse("create_review"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "new_review.html")

    def test_review_detail_view(self):
        response = self.client.get(reverse("review_detail", args=[self.review.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "review_detail.html")
        self.assertTemplateUsed(response, "base.html")

    def test_review_list_view(self):
        response = self.client.get(reverse("review_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "review_list.html")
        self.assertTemplateUsed(response, "base.html")
