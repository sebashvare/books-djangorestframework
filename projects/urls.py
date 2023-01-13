from rest_framework import routers
from .api import ProjectViewSet

"""
    routers: Este modulo permite crear las peticiones que por defecto se ejecutan en un API REST
    al final lo que hacemos es exportar las url para que las pueda tomar la aplicacion principal
"""


router = routers.DefaultRouter()

router.register("api/projects", ProjectViewSet, "projects")

urlpatterns = router.urls
