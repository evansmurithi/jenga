from rest_framework.routers import SimpleRouter

from jenga.construction_site import views

router = SimpleRouter()

router.register(r'suppliers', views.SupplierViewSet)
router.register(r'materials', views.MaterialViewSet)
router.register(r'construction_sites', views.ConstructionSiteViewSet)
router.register(r'deliveries', views.DeliveryViewSet)

urlpatterns = router.urls
