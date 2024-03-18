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


class ProductMaterialPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMaterial
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

    def validate(self, attrs):
        information = []
        qty = attrs.get('product_qty')
        name = attrs.get('product_name')
        product_first = Product.objects.first()
        materials = Material.objects.all()
        a = Material.objects.get(id=materials.filter()[1].id).count
        if name == product_first:
            task1 = int(qty * 0.8)
            task2 = int(qty * 5)
            task3 = int(qty * 10)
            information.append(task1)
            information.append(task2)
            information.append(task3)
            # if task1 < Material.objects.get(id=materials.filter()[1].id).count:
            #     Material.objects.create(id=materials.filter()[1].id,
            #                             name=Material.objects.get(id=materials.filter()[1].id).count,
            #                             count=Material.objects.get(id=materials.filter()[1].id).count - task1,
            #                             price=materials.filter()[1].price)
        print(information)
        return attrs

    # def create(self, validated_data):
    #     information = []
    #     qty = validated_data.get('product_qty')
    #     name = validated_data.get('product_name')
    #     product_first = Product.objects.first()
    #     materials = Material.objects.all()
    #     if name == product_first:
    #         task1 = int(qty * 0.8)
    #         task2 = int(qty * 5)
    #         task3 = int(qty * 10)
    #         information.append(task1)
    #         information.append(task2)
    #         information.append(task3)
    #         if task1 < Material.objects.get(id=materials.filter()[1].id).count:
    #             Material.objects.create(id=materials.filter()[1].id,
    #                                     count=Material.objects.get(id=materials.filter()[1].id).count - task1, **validated_data)
    #     return validated_data

    #     products = Product.objects.all()
    #     materials = Material.objects.values_list("count", flat=True).order_by("id")
    #     product_first = Product.objects.first()
    #     material_detail = MaterialDetail.objects.filter(material_id=1).values()
    #     product_qty = validated_data.get('product_qty')
    #     product_name = validated_data.get('product_name')
    #     # print(product_first, products)
    #     # print(product_name, product_qty)
    #     # print(material_detail[0])
    #     if product_name == product_first:
    #         task1 = int(product_qty * 0.8)
    #         task2 = int(product_qty * 5)
    #         task3 = int(product_qty * 10)
    #         information.append(task1)
    #         information.append(task2)
    #         information.append(task3)
    #         # print(information)
    #
    #     instance = Result.objects.create(**validated_data)
    #     instance.save()
    #     return instance
