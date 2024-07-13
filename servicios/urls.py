#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('crud', views.crud, name='crud'),
    path('servicios/servicios_add/', views.serviciosAdd, name='serviciosAdd'),
    path('servicios_del/<int:pk>', views.servicios_del, name='servicios_del'),
    path('servicios/servicios_findEdit/<int:pk>/', views.servicios_findEdit, name='servicios_findEdit'),
    path('servicios/servicios_update/<int:pk>/', views.serviciosUpdate, name='serviciosUpdate'),
]
