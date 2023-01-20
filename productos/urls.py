from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()

router.register('api/productos',ProjectViewSet,'productos')

urlpatterns = router.urls