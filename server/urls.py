from api import views
from django.urls import include, path
from django.contrib import admin
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'ethblock', views.EthBlockViewSet)
router.register(r'arbblock', views.ArbBlockViewSet)
router.register(r'optblock', views.OptBlockViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
