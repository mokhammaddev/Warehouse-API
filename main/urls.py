from django.urls import path
from main.views import ProductListCreateAPIView, MaterialListCreateAPIView, ProductMaterialListCreateAPIView

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view()),
    path('materials/', MaterialListCreateAPIView.as_view()),
    path('products-materials/', ProductMaterialListCreateAPIView.as_view()),
    # path('warehouses/', WarehouseListCreateAPIView.as_view()),
]
