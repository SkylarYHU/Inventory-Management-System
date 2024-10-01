from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
# Create your views here.

# This Django code defines a set of views for basic CRUD (Create, Read, Update, Delete) operations on Product objects.
# CRUD = create, read, update, delete

# Home View
# Displays the home page of the app


def home_view(request):
    return render(request, 'invApp/home.html')

# Create View


def product_create_view(request):
    # When the view is accessed via GET, the initial form = ProductForm() line creates an empty form instance.
    form = ProductForm()
    # If the request method is POST, it processes the submitted form data.
    if request.method == "POST":
        form = ProductForm(request.POST)
        # If the form is valid, it saves the new product to the database and redirects to the product
        if form.is_valid():
            form.save()
            return redirect('product_list')
        # If the form is invalid, it redisplays the form with error messages.
        return render(request, 'invApp/product_form.html', {"form": form})


# Read View
# Displays a list of all products in the database.
def product_list_view(request):
    # Fetches all Product objects using Product.objects.all().
    products = Product.objects.all()
    # Displays the products in invApp/product_list.html, passing the list of products to the template via the products context variable.
    return render(request, 'invApp/product_list.html', {'products': products})

# Update View
# Handles updating an existing Product.


def product_update_view(request, product_id):
    # It retrieves the product by its product_id.
    product = Product.objects.get(product_id=product_id)
    form = ProductForm(instance=product)
    # If the request method is POST, it processes the submitted form and updates the product if valid.
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            # After a successful update, it redirects to the product list page.
            return redirect("product_list")
    # If the request method is GET, it pre-fills the form with the product's current data using instance=product.
    return render(request, 'invApp/product_form.html', {"form": form})

    # Delete View
    #  Handles the deletion of a Product


def product_delete_view(request, product_id):
    # It retrieves the product by product_id.
    product = Product.objects.get(product_id=product_id)
    # If the request method is POST, it deletes the product from the database and redirects to the product list page.
    if request.method == "POST":
        product.delete()
        return redirect('product_list')
    # If the request method is GET, it asks for confirmation before deleting by rendering the invApp/product_confirm_delete.html template.
    # This means that in the product_confirm_delete.html template, you can access the product variable using the key "product". For example, you could display the product's details by using: <h1>Delete Product: {{ product.name }}</h1>
    return render(request, 'invApp/product_confirm_delete.html', {"product": product})
