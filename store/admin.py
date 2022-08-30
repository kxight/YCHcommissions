from django.contrib import admin
from .models import Product,Variation,VariationValue, ReviewRating, ProductGallery
import admin_thumbnails

@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    inlines = [ProductGalleryInline]
    

# class VariationAdmin(admin.ModelAdmin):
#     list_display = ('product', 'variation_category', 'variation_value', 'is_active')
#     list_editable = ('is_active',)
#     list_filter = ('product', 'variation_category', 'variation_value')

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'is_active', )
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category',)

# class VariationValueInline(admin.TabularInline):
#     model = VariationValue
#     extra = 1

class VariationValueAdmin(admin.ModelAdmin):
    list_display = ('variation', 'value', 'is_active','create_date',)
    list_editable = ('is_active',)
    list_filter = ('variation',)
    

admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(VariationValue, VariationValueAdmin)
admin.site.register(ReviewRating)
admin.site.register(ProductGallery)
# admin.site.register(VariationValue)