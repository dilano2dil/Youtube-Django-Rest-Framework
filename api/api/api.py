from api.models import Product
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ProductSerializer1, ProductSerializer2

# developpement de l'api avec le decorateur @api_view de rest_framework

@api_view(['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def product_api_view(request, pk=None):
    if request.method == 'GET':
        if pk is not None:
            try:
                product = get_object_or_404(Product, pk=pk)
                serializer = ProductSerializer1(product)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Product.DoesNotExist:
                return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        products = Product.objects.all()
        serializer = ProductSerializer1(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = ProductSerializer1(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        if pk is None:
            return Response({'error': 'Product ID is required for update'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            product = get_object_or_404(Product, pk=pk)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer1(product, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        if pk is None:
            return Response({'error': 'Product ID is required for deletion'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            product = get_object_or_404(Product, pk=pk)
            product.delete()
            return Response({'message': 'Product deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        if pk is None:
            return Response({'error': 'Product ID is required for partial update'}, status=status.HTTP_400_BAD_REQUEST)
        product = get_object_or_404(Product, pk=pk)

        serializer = ProductSerializer1(product, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)