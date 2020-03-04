from rest_framework import viewsets

from jenga.construction_site import models, serializers


class SupplierViewSet(viewsets.ModelViewSet):

    queryset = models.Supplier.objects.all()
    serializer_class = serializers.SupplierSerializer


class MaterialViewSet(viewsets.ModelViewSet):

    queryset = models.Material.objects.all()
    serializer_class = serializers.MaterialSerializer


class ConstructionSiteViewSet(viewsets.ModelViewSet):

    queryset = models.ConstructionSite.objects.all()
    serializer_class = serializers.ConstructionSiteSerializer


class DeliveryViewSet(viewsets.ModelViewSet):

    queryset = models.Delivery.objects.all()
    serializer_class = serializers.DeliverySerializer
