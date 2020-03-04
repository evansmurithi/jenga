from django.contrib import admin

from . import models


admin.site.register(models.Supplier)
admin.site.register(models.Material)
admin.site.register(models.ConstructionSite)
admin.site.register(models.Delivery)
