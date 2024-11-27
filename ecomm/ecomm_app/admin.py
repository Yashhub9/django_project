from django.contrib import admin
from .models import product,carts,order
# Register your models here.
class proAdmin(admin.ModelAdmin):
    list_display=['id','name','price','pdetails','cat','is_active']
    list_filter=['cat','is_active']
class cartAdmin(admin.ModelAdmin):
    list_display=['id','uid','pid']
class orderAdmin(admin.ModelAdmin):
    list_display=['id','uid','pid']

admin.site.register(carts,cartAdmin)
admin.site.register(product,proAdmin)
admin.site.register(order,orderAdmin)
