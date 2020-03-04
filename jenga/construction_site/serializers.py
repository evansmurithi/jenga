from jenga.common.serializers import CommonSerializer
from jenga.construction_site import models


class SupplierSerializer(CommonSerializer):

    class Meta(CommonSerializer.Meta):
        model = models.Supplier
        fields = ('name', 'address', 'created', 'updated')


class MaterialSerializer(CommonSerializer):

    class Meta(CommonSerializer.Meta):
        model = models.Material
        fields = ('code', 'name', 'unit_of_measurement', 'created', 'updated')


class ConstructionSiteSerializer(CommonSerializer):

    class Meta(CommonSerializer.Meta):
        model = models.ConstructionSite
        fields = ('name', 'location', 'constructor_name', 'created', 'updated')


class DeliverySerializer(CommonSerializer):

    class Meta(CommonSerializer.Meta):
        model = models.Delivery
        fields = (
            'supplier', 'site', 'material', 'quantity', 'delivered_on',
            'created', 'updated'
        )
