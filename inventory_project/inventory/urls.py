"""
URL configuration for inventory_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, product_list, add_product, update_product, delete_product

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # API endpoints
    path('', product_list, name='product-list'),  # HTML page
    path('add-product/', add_product, name='add-product'),  # Add product
    path('update-product/<int:product_id>/', update_product, name='update-product'),  # Update product
    path('delete-product/<int:product_id>/', delete_product, name='delete-product'),  # Delete product
]

