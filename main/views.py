from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from main.models import ProductMaterial, Product, Material, Result
from main.serializers import ProductSerializer, MaterialSerializer, ProductMaterialSerializer, ResultSerializer, ProductMaterialPostSerializer


class ProductListCreateAPIView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class MaterialListCreateAPIView(ListCreateAPIView):
    queryset = Material.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MaterialSerializer
        return ProductMaterialPostSerializer


class ProductMaterialListCreateAPIView(ListCreateAPIView):
    serializer_class = ProductMaterialSerializer
    queryset = ProductMaterial.objects.all()


class ResultListCreateAPIView(ListCreateAPIView):
    serializer_class = ResultSerializer
    queryset = Result.objects.all()

    # def get_serializer_context(self):
    #     ctx = super().get_serializer_context()
    #     ctx['post_id'] = self.kwargs.get('post_id')
    #     return ctx
    #
    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     post_id = self.kwargs.get('post_id')
    #     qs = qs.filter(post_id=post_id)
    #     return qs

#
# class WarehouseListCreateAPIView(ListCreateAPIView):
#     serializer_class = WarehouseSerializer
#     queryset = Warehouse.objects.all()
#


