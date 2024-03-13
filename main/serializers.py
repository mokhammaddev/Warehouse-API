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


class ResultSerializer(serializers.ModelSerializer):
    product_materials = serializers.SerializerMethodField(read_only=True)

    def get_product_materials(self, obj):
        product_materials = Material.objects.all()
        serializer = MaterialSerializer(product_materials, many=True)
        return serializer.data

    class Meta:
        model = Result
        fields = ['id', 'product_name', 'product_qty', 'product_materials']
        extra_kwargs = {
            'product_name': {'required': True},
        }

    def create(self, validated_data):
        information = []
        products = Product.objects.all()
        product_first = Product.objects.first()
        material_detail = MaterialDetail.objects.filter(material_id=1).values()
        product_qty = validated_data.get('product_qty')
        product_name = validated_data.get('product_name')
        # print(product_first, products)
        # print(product_name, product_qty)
        # print(material_detail[0])
        if product_name == product_first:
            information.append(int(product_qty * 0.8))
            print(information)

        instance = Result.objects.create(**validated_data)
        instance.save()
        return instance
