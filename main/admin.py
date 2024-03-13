from django.contrib import admin
from main.models import *

admin.site.register(Product)
admin.site.register(Material)
admin.site.register(Result)
admin.site.register(MaterialDetail)


# admin.site.register(Statute)
# admin.site.register(ProductMaterial)
# admin.site.register(Warehouse)


# class StatuteAdmin(admin.ModelAdmin):
#     list_display = ('id', 'variable1', 'variable2', 'variable3', 'variable4', 'variable5', 'variable6')
#
#     @admin.display(description='Name')
#     def variable1(self, obj):
#         return obj
#
# admin.site.register(contactEnquiries, StatuteAdmin)