from django.db import models
from django.conf import settings

class Product(models.Model):
    # Professional Athletic Gear Categories
    CATEGORY_CHOICES = [
        ('Apparel', 'Apparel'),       # Jerseys, Training Gear, Hoodies
        ('Footwear', 'Footwear'),     # Cleats, Running Shoes, Sneakers
        ('Equipment', 'Equipment'),   # Balls, Bats, Rackets, Gym Tools
        ('Accessories', 'Accessories'), # Bottles, Bags, Socks, Protective Gear
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    
    # Updated default to 'Apparel' for a sports store feel
    category = models.CharField(
        max_length=50, 
        choices=CATEGORY_CHOICES, 
        default='Apparel'
    )
    
    # Marks a product with the "PRO CHOICE" badge on the frontend
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.category})"