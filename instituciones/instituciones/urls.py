from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('instituciones/docs/', views.factura_list, name='facturaList'),
    path('instituciones/create/', csrf_exempt(views.factura_create), name='facturaCreate'),
]