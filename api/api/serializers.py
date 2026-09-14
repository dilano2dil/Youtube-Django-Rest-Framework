from api.models import Product
from rest_framework import serializers

class ProductSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']

class ProductSerializer2(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=200)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)