from django.db import models

# Create your models here.

# Defines a Product in a database


class Product(models.Model):
    # Automatically generates an integer value for each new product.
    # Sets this field as the primary key, meaning it uniquely identifies each record in the table.
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    # A string field for storing the product's Stock Keeping Unit, a unique identifier for each product.
    sku = models.CharField(max_length=50, unique=True)
    price = models.IntegerField()
    supplier = models.CharField(max_length=100)

    # This method defines how the object will be represented as a string, typically when displaying it in the Django admin or shell. In this case, it returns the product's name.
    def __str__(self):
        # eg. When you retrieve and print this product， it shows "laptop".
        return self.name
