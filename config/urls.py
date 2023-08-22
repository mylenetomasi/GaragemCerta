from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from usuario.router import router as usuario_router

from garagem.views import (
    MarcaViewSet,
    CategoriaViewSet,
    CorViewSet,
    AcessorioViewSet,
    VeiculoViewSet,
    ModeloViewSet,
)

router = routers.DefaultRouter()
router.register(r"marcas", MarcaViewSet)
router.register(r"modelos", ModeloViewSet)
router.register(r"categorias", CategoriaViewSet)
router.register(r"cores", CorViewSet)
router.register(r"acessórios", AcessorioViewSet)
router.register(r"veiculos", VeiculoViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(usuario_router.urls)),
    path("", include(router.urls)),
]
