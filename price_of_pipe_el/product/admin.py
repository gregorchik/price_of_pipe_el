from django.contrib import admin
from . models import Product
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        import_id_fields = []
        fields = [
            'category',
            'designation',
            'diameter_dn',
            'pressure_pn',
            'material',
            'price',
        ]
        import_id_fields = (
            'category',
            'designation',
            'diameter_dn',
            'pressure_pn',
            'material',
            'price',
        )
        skip_unchanged = False
        report_skipped = True


class ProductAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    resource_classes = [ProductResource]
    list_display = (
        'category',
        'designation',
        'diameter_dn',
        'pressure_pn',
        'material',
        'price',
    )


admin.site.register(Product, ProductAdmin)
