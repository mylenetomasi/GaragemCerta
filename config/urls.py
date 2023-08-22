from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from usuario.router import router as usuario_router
from django.conf import settings
from django.conf.urls.static import static
from uploader.router import router as uploader_router

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
    path("api/media/", include(uploader_router.urls)),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)