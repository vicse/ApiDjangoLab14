from django.conf.urls import url, include
from rest_framework import routers
from restreact import views

router = routers.DefaultRouter()
router.register(r'productos', views.ProductoViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls))
]
