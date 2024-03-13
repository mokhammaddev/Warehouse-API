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
        materials = Material.objects.values_list("count", flat=True).order_by("id")
        material1 = materials[0]
        print("material1-->", material1)
        material2 = materials[1]
        print("material2-->", material2)
        material3 = materials[2]
        print("material3-->", material3)
        material4 = materials[3]
        print("material4-->", material4)
        material5 = materials[4]
        print("material5-->", material5)
        material6 = materials[5]
        print("material6-->", material6)
        print("----------------------")
        product_first = Product.objects.first()
        material_detail = MaterialDetail.objects.filter(material_id=1).values()
        product_qty = validated_data.get('product_qty')
        product_name = validated_data.get('product_name')
        # print(product_first, products)
        # print(product_name, product_qty)
        # print(material_detail[0])
        if product_name == product_first:
            task1 = int(product_qty * 0.8)
            print("initial task1-->", task1)
            if task1 > material1:
                task1 = task1 - material1
                if task1 < material2:
                    material2 = material2 - task1
                    task1 = True
                else:
                    task1 = False
                print("task1-->", task1)
            print("material2-->", material2)
            task2 = int(product_qty * 5)
            print("initial task2-->", task2)
            if task2 > material3:
                task2 = task2 - material3
                if task2 < material4:
                    task2 = material4 - task2
                    task2 = True
                else:
                    task2 = False
                print("task2-->", task2)
            task3 = int(product_qty * 10)
            information.append(task1)
            information.append(task2)
            information.append(task3)
            # print(information)

        instance = Result.objects.create(**validated_data)
        instance.save()
        return instance
