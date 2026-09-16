from api.models import Product
from rest_framework import serializers

class ProductSerializer1(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    price_in_dollars = serializers.SerializerMethodField()
    detail_link = serializers.SerializerMethodField()
    link = serializers.HyperlinkedIdentityField(view_name='api:product_api_detail', lookup_field='pk')

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'price_in_dollars', 'detail_link', 'link']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_price_in_dollars(self, obj):
        return obj.price_in_dollars()

    def get_detail_link(self, obj):
        return obj.get_absolute_url()  # Assuming you have a URL pattern for product details

    def validate_name(self, value):
        if "iPhone" in value:
            raise serializers.ValidationError("Unauthorized product in our system")
        return value

    def validate_price(self, value):
        if value > 500:
            raise serializers.ValidationError("The product is too expensive !")
        return value

class ProductSerializer2(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=200)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)