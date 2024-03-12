from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=221)
    count = models.IntegerField()


class Material(models.Model):
    name = models.CharField(max_length=221)
    count = models.IntegerField()
    price = models.IntegerField()


class ProductMaterial(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    material_id = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.IntegerField()

#
# class Warehouse(models.Model):
#     material = models.ForeignKey(Material, on_delete=models.CASCADE)
