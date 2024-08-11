from rest_framework import serializers

from network.models import NetworkLink, Product
from network.validators import SupplierValidator


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'title', 'model', 'release_date']


class NetworkLinkSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = NetworkLink
        fields = ['id', 'email', 'country', 'city', 'street', 'house_number', 'name',
                  'status', 'debt', 'create_date', 'supplier', 'product']
        read_only_fields = ['debt']
        validators = [SupplierValidator()]
