from django.db import models


class Statute(models.Model):
    variable1 = models.FloatField(default=0)
    variable2 = models.FloatField(default=0)
    variable3 = models.FloatField(default=0)
    variable4 = models.FloatField(default=0)
    variable5 = models.FloatField(default=0)
    variable6 = models.FloatField(default=0)


class Product(models.Model):
    product_name = models.CharField(max_length=221)

    def __str__(self):
        return self.product_name


class Material(models.Model):
    name = models.CharField(max_length=221)
    count = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name

    @property
    def get_name(self):
        return self.name

    @property
    def get_price(self):
        return self.price

    @property
    def get_count(self):
        return self.count


class ProductMaterial(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    material_id = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class MaterialDetail(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    charter = models.CharField(max_length=10)

    def __str__(self):
        return self.charter


class Result(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty = models.IntegerField()
