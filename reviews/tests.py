# reviews/tests.py
from django.urls import reverse
from .models import Review
from django.contrib.auth import get_user_model
from django.conf import settings
from .models import Comment
from django.contrib.messages import get_messages
from django.test import TestCase

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


class CommentModelTest(TestCase):
    def setUp(self):
        # Create a user and a review to associate with comments
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpassword"
        )
        self.review = Review.objects.create(
            title="Test Review",
            body="This is a test review body.",
            author=self.user,
        )

    def test_create_comment(self):
        # Test creating a Comment instance
        comment = Comment.objects.create(
            review=self.review,
            comment="This is a test comment.",
            author=self.user,
        )
        self.assertEqual(comment.comment, "This is a test comment.")
        self.assertEqual(comment.review, self.review)
        self.assertEqual(comment.author, self.user)
        self.assertTrue(str(comment) == comment.comment)

    def test_comment_get_absolute_url(self):
        # Test the get_absolute_url method
        comment = Comment.objects.create(
            review=self.review,
            comment="This is a test comment.",
            author=self.user,
        )
        self.assertEqual(comment.get_absolute_url(), "/reviews/")


# --------------End Model Tests--------------------

# --------------View Tests--------------------


class SimpleViewsTest(TestCase):
    def setUp(self):
        # Create a test user and log them in
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.login(username="testuser", password="testpassword")

        # Create a test review
        self.review = Review.objects.create(
            title="Test Review",
            body="This is a test review body.",
            author=self.user,
        )

    def test_apply_verified_reviewer_view(self):
        # Test if the apply_verified_reviewer view works and redirects properly
        response = self.client.get(reverse("apply_verified_reviewer"))
        self.assertEqual(response.status_code, 302)  # Should redirect
