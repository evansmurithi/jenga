from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path


v1_patterns = [
    url(r'^', include(
        ('jenga.construction_site.urls', 'construction_sites'),
        namespace='construction_sites')
    ),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^v1/', include((v1_patterns, 'v1'), namespace='v1')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
