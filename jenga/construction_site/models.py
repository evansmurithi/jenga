from django.db import models
from django.utils import timezone

from jenga.common.models import AbstractBase


class Supplier(AbstractBase):
    """
    Hold details of suppliers delivering materials at a construction site.
    """
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Material(AbstractBase):
    """
    Hold details of materials to be delivered by a supplier to a construction
    site.
    """
    UNIT_OF_MEASUREMENTS = [
        ('BAGS', 'Bags'),
        ('METRES', 'Metres'),
        ('LITRES', 'Litres'),
    ]

    code = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    unit_of_measurement = models.CharField(
        max_length=255, choices=UNIT_OF_MEASUREMENTS)

    def __str__(self):
        return "{} ({})".format(self.name, self.unit_of_measurement)


class ConstructionSite(AbstractBase):
    """
    Holds details of a construction site.
    """
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    constructor_name = models.CharField(max_length=255)

    def __str__(self):
        return "{} at {}".format(self.name, self.location)


class Delivery(AbstractBase):
    """
    Holds delivery details from supplier to construction site.
    """
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    site = models.ForeignKey(ConstructionSite, on_delete=models.PROTECT)
    material = models.ForeignKey(Material, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    delivered_on = models.DateTimeField(default=timezone.now)

    class Meta(AbstractBase.Meta):
        ordering = ('-delivered_on',)
