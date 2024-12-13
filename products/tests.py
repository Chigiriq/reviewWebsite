from django.test import TestCase
from .models import Product

#--------------Model Tests--------------------
# class ProductModelTests(TestCase):
#     def setUp(self):
#         # Setup a product instance for the tests
#         self.product = Product.objects.create(
#             name="Test Product",
#             price=100,
#             description="This is a test product",
#             image=None
#         )
    
#     def test_product_creation(self):
#         # Test if the product is correctly created
#         self.assertEqual(self.product.name, "Test Product")
#         self.assertEqual(self.product.price, 100)
#         self.assertEqual(self.product.description, "This is a test product")
#         self.assertFalse(self.product.image)  # Updated check for the ImageField
    
#     def test_str_method(self):
#         # Test the __str__ method
#         self.assertEqual(str(self.product), "Test Product")
    
#     def test_get_absolute_url(self):
#         # Update to match the correct URL pattern
#         expected_url = f"/products/{self.product.pk}/"
#         self.assertEqual(self.product.get_absolute_url(), expected_url)
#--------------End Model Tests--------------------
from django.conf import settings
settings.DEBUG = True


from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from .models import Product

class ProductViewsTests(TestCase):

    def setUp(self):
        """Set up test data."""
        # Create a mock image file
        self.mock_image = SimpleUploadedFile(
            "test_image.jpg", b"file_content", content_type="image/jpeg"
        )

        # Create a product with a mock image
        self.product1 = Product.objects.create(
            name="Test Product 1",
            description="A test product.",
            price=10.00,
            image=self.mock_image,  # Adding the image field
        )

    def test_product_list_view(self):
        """Test ProductListView displays the correct template and products."""
        response = self.client.get(reverse("product_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "product_list.html")
        self.assertContains(response, "Test Product 1")
        self.assertContains(response, self.product1.image.url)  # Verify image URL

    def test_product_detail_view_404(self):
        """Test ProductDetailView returns 404 for a non-existing product."""
        response = self.client.get(reverse("product_detail", kwargs={"pk": 9999}))  # Non-existent product ID
        self.assertEqual(response.status_code, 404)
        
    def test_product_detail_view(self):
        """Test that the product detail page renders correctly."""
        response = self.client.get(reverse("product_detail", kwargs={"pk": self.product1.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "product_detail.html")
        self.assertContains(response, "Test Product 1")
        self.assertContains(response, "$10.00")  # Since floatformat:2 is used in the template




