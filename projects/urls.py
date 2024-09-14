from rest_framework import routers
from .api import ProjectViewSet
from django.urls import path, include

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = router.urls