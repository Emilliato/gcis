from django.test import TestCase
from .models import Product
# Create your tests here.
class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(p_name="Engine cleaner", p_quantity= 20.0, p_price=2)
        Product.objects.create(p_name="Coolant", p_quantity= 40.0, p_price=2)
    def test_total_quantity(self):
        """Verifies if the total amount is being calulated correctly"""
        coolant = Product.objects.get(p_name="Coolant")

        self.assertAlmostEqual(coolant.calculateTotal(),round(40.00*2,2))
