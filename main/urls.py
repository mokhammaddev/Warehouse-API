from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from main.views import ProductListCreateAPIView, MaterialListCreateAPIView, ProductMaterialListCreateAPIView, \
    ResultListCreateAPIView

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view()),
    path('materials/', MaterialListCreateAPIView.as_view()),
    path('products-materials/', ProductMaterialListCreateAPIView.as_view()),
    path('', ResultListCreateAPIView.as_view()),
    # path('warehouses/', WarehouseListCreateAPIView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
