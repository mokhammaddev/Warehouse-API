from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from main.models import ProductMaterial, Product, Material, Result
from main.serializers import ProductSerializer, MaterialSerializer, ProductMaterialSerializer, ResultSerializer


class ProductListCreateAPIView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class MaterialListCreateAPIView(ListCreateAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()


class ProductMaterialListCreateAPIView(ListCreateAPIView):
    serializer_class = ProductMaterialSerializer
    queryset = ProductMaterial.objects.all()


class OrderCountListCreateAPIView(ListCreateAPIView):
    serializer_class = ResultSerializer
    queryset = Result.objects.all()

#
# class WarehouseListCreateAPIView(ListCreateAPIView):
#     serializer_class = WarehouseSerializer
#     queryset = Warehouse.objects.all()
#


