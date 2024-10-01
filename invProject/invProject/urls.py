"""
URL configuration for invProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # This is a reference to Django’s built-in admin site, which provides an interface to manage your application’s models. By including this, you can access the admin interface for your application at the /admin/ URL.
    path("admin/", admin.site.urls),
    # When a user visits http://yourdomain.com/, Django looks at the urlpatterns list and finds the empty string '', which points to the invApp.urls.
    path('', include('invApp.urls'))
]
