from django import forms
from .models import Product

# Define a Django form based on the Product model.

# This creates a form class (ProductForm) that is a subclass of Django's forms.ModelForm.


class ProductForm(forms.ModelForm):
    # The Meta class contains configuration options for the form.
    class Meta:
        # This specifies that the form is based on the Product model. The form fields will correspond to the fields in the Product model (product_id, name, sku, price, etc.).
        model = Product
        # This tells Django to include all fields from the Product model in the form.
        fields = '__all__'
        labels = {
            "product_id": "Product ID",
            "name": "Name",
            "sku": "SKU",
            "quantity": "Quantity",
            "supplier": "Supplier",
        }

        # Widgets control how the HTML form inputs are rendered.
        widgets = {
            # Specifies that this field will be rendered as an HTML <input> element of type "number", suitable for numeric data.
            "product_id": forms.NumberInput(
                # "class": Adds the Bootstrap CSS class "form-control", which styles the input element according to Bootstrap’s form design.
                attrs={'placeholder': 'e.g. 1', 'class': 'form-control'}),
            "name": forms.TextInput(
                attrs={'placeholder': 'e.g. shirt', 'class': 'form-control'}),
            "sku": forms.TextInput(
                attrs={'placeholder': 'e.g. S12345', 'class': 'form-control'}),
            "quantity": forms.NumberInput(
                attrs={'placeholder': 'e.g. 5', 'class': 'form-control'}),
            "supplier": forms.TextInput(
                attrs={'placeholder': 'e.g. TechSource Ltd. ', 'class': 'form-control'}),
        }
