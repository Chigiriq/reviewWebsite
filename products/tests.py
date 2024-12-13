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
            price=10.99,
            image=self.mock_image,  # Adding the image field
        )

    def test_product_list_view(self):
        """Test ProductListView displays the correct template and products."""
        response = self.client.get(reverse("product_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "product_list.html")
        self.assertContains(response, "Test Product 1")
        self.assertContains(response, self.product1.image.url)  # Verify image URL


    # def test_product_detail_view(self):
    #     """Test ProductDetailView displays the correct template and product."""
    #     response = self.client.get(reverse("product_detail", kwargs={"pk": self.product1.pk}))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, "product_detail.html")
    #     self.assertContains(response, self.product1.name)
    #     self.assertContains(response, self.product1.description)
        
    #     # Check that the price with a dollar sign is in the response
    #     self.assertContains(response, f"${self.product1.price:.2f}")

    # def test_product_detail_view_404(self):
    #     """Test ProductDetailView returns 404 for a non-existing product."""
    #     response = self.client.get(reverse("product_detail", kwargs={"pk": 9999}))  # Non-existent product ID
    #     self.assertEqual(response.status_code, 404)

    # def test_search_view(self):
    #     """Test SearchView displays the correct products based on search."""
    #     # Test search with matching results
    #     response = self.client.get(reverse("search") + "?search=Test Product 1")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, "searchProduct.html")
    #     self.assertContains(response, self.product1.name)
    #     self.assertNotContains(response, self.product2.name)

    #     # Test search with no matching results
    #     response = self.client.get(reverse("search") + "?search=Non-existent Product")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, "searchProduct.html")
    #     self.assertContains(response, "No products found.")

    # def test_search_view_no_query(self):
    #     """Test SearchView with no search query."""
    #     response = self.client.get(reverse("search"))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, "searchProduct.html")
    #     # Test if all products are returned when no query is passed
    #     self.assertContains(response, self.product1.name)
    #     self.assertContains(response, self.product2.name)
