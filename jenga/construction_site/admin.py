from django.contrib import admin

from . import models


class DeliveryAdmin(admin.ModelAdmin):
    list_display = (
        'supplier', 'site', 'material', 'quantity', 'delivered_on'
    )


admin.site.register(models.Supplier)
admin.site.register(models.Material)
admin.site.register(models.ConstructionSite)
admin.site.register(models.Delivery, DeliveryAdmin)
