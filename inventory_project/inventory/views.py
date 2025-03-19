from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

@api_view(["POST"])
def add_product(request):
    name = request.data.get("name")
    price = request.data.get("price")
    stock = request.data.get("stock")

    if not name or price is None or stock is None:
        return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        price = float(price)
        stock = int(stock)
    except ValueError:
        return Response({"error": "Invalid data format"}, status=status.HTTP_400_BAD_REQUEST)

    if price < 0:
        return Response({"error": "Price cannot be negative"}, status=status.HTTP_400_BAD_REQUEST)

    product = Product.objects.create(name=name, price=price, stock=stock)
    return Response({"message": "Product added successfully", "product_id": product.id}, status=status.HTTP_201_CREATED)

@api_view(["PUT"])
def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    price = request.data.get("price")
    stock = request.data.get("stock")

    try:
        price = float(price)
        stock = int(stock)
    except ValueError:
        return Response({"error": "Invalid data format"}, status=status.HTTP_400_BAD_REQUEST)

    if price < 0:
        return Response({"error": "Price cannot be negative"}, status=status.HTTP_400_BAD_REQUEST)

    product.price = price
    product.stock = stock
    product.save()
    return Response({"message": "Product updated successfully"}, status=status.HTTP_200_OK)

@api_view(["DELETE"])
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return Response({"message": "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
