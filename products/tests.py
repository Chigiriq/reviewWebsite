from django.test import TestCase
from .models import Product

#--------------Model Tests--------------------
class ProductModelTests(TestCase):
    def setUp(self):
        # Setup a product instance for the tests
        self.product = Product.objects.create(
            name="Test Product",
            price=100,
            description="This is a test product",
            image=None
        )
    
    def test_product_creation(self):
        # Test if the product is correctly created
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.price, 100)
        self.assertEqual(self.product.description, "This is a test product")
        self.assertFalse(self.product.image)  # Updated check for the ImageField
    
    def test_str_method(self):
        # Test the __str__ method
        self.assertEqual(str(self.product), "Test Product")
    
    def test_get_absolute_url(self):
        # Update to match the correct URL pattern
        expected_url = f"/products/{self.product.pk}/"
        self.assertEqual(self.product.get_absolute_url(), expected_url)
#--------------End Model Tests--------------------
