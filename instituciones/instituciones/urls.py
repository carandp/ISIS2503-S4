from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('instituciones/docs/', views.FacturaListCreate.as_view(), name='instituciones_create'),
    path('instituciones/docs/<str:pk>/', views.FacturaRetrieveUpdateDestroy.as_view(), name='institucion-retrieve-update-destroy'),
]