from rest_framework import serializers
from main.models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'


class ProductMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMaterial
        fields = '__all__'


class OrderCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderCount
        fields = ['id', 'product_name', 'product_qty']

    def create(self, validated_data):
        materials = Material.objects.all()
        product_qty = validated_data.get('product_qty')
        product_name = validated_data.get('product_name')
        print(product_name, product_qty)
        instance = OrderCount.objects.create(**validated_data)
        instance.save()
        return instance
