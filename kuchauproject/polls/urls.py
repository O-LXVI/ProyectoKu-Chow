from django.urls import path
from django.urls import include, path


urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", admin.site.urls)
]