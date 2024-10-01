from django.urls import path
from . import views

# The urlpatterns list contains the URL patterns for your application, where each pattern maps a URL path to a specific view.
urlpatterns = [
    # Maps the root URL (/) to the home_view function. name='home' allows you to refer to this URL pattern in templates and redirects.
    # This is the root URL pattern. An empty string means that this pattern will match the homepage (e.g., http://yourdomain.com/).
    path('', views.home_view, name='home'),
    # Maps the URL /create/ to the product_create_view function.
    # This pattern matches the URL http://yourdomain.com/create/.
    path('create/', views.product_create_view, name='product_create'),
    # Maps the URL /list/ to the product_list_view function.
    # This pattern matches the URL http://yourdomain.com/list/.
    path('list/', views.product_list_view, name='product_list'),
    # <int:product_id> captures an integer from the URL and passes it to the view as the product_id argument. This is used to update a specific product.
    # This pattern matches URLs like http://yourdomain.com/update/1/, where 1 is an integer representing the product_id.
    path('update/<int:product_id>/',
         views.product_update_view, name='product_update'),
    # Similar to the update view, this captures an integer product ID from the URL to delete the specified product.
    # 'delete/<int:product_id>/': This pattern matches URLs like http://yourdomain.com/delete/1/.
    path('delete/<int:product_id>/',
         views.product_delete_view, name='product_delete'),
]
