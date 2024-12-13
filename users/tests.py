from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model

#--------------Model Tests--------------------
class CustomUserModelTests(TestCase):
    def setUp(self):
        """Set up a sample user for testing."""
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="securepassword123",
            name="Test User",
            bio="This is a test bio.",
            verifiedReviewer=True,
            review_request_status="Approved",
        )

    def test_custom_user_creation(self):
        """Test if the CustomUser instance is created correctly."""
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.name, "Test User")
        self.assertEqual(self.user.bio, "This is a test bio.")
        self.assertTrue(self.user.verifiedReviewer)
        self.assertEqual(self.user.review_request_status, "Approved")
        self.assertEqual(self.user.profile_picture.name, "images/Blues_logo.jpg")

    def test_default_review_request_status(self):
        """Test the default value of review_request_status."""
        new_user = get_user_model().objects.create_user(
            username="newuser", password="securepassword456", name="New User"
        )
        self.assertEqual(new_user.review_request_status, "Pending")

    def test_update_bio(self):
        """Test updating the bio field."""
        self.user.bio = "Updated bio."
        self.user.save()
        self.assertEqual(self.user.bio, "Updated bio.")

    def test_profile_picture_upload(self):
        """Test custom profile picture upload."""
        self.user.profile_picture = "profile_pictures/test_user.jpg"
        self.user.save()
        self.assertEqual(self.user.profile_picture.name, "profile_pictures/test_user.jpg")

    def test_verified_reviewer_default(self):
        """Test the default value of verifiedReviewer."""
        new_user = get_user_model().objects.create_user(
            username="anotheruser", password="securepassword789", name="Another User"
        )
        self.assertFalse(new_user.verifiedReviewer)
#--------------End Model Tests--------------------
