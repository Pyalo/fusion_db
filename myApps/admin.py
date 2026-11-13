from myApps.models import Product
from django.contrib import admin
from django.contrib.auth.models import User

admin.site.site_title="PANDER"
admin.site.site_header="PANDER SHOP"
admin.site.site_title="PANDER ADMINISTRATION"

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'category', 'for_sale')
    search_fields = ('name', 'code', 'category')
    list_filter = ('category', 'for_sale')
    ordering = ('name','-price')