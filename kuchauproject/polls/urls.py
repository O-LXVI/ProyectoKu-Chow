from django.urls import path
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", admin.site.urls),
    path("crud", views.crud, name="crud")
]