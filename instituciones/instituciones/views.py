from rest_framework import generics, status
from rest_framework.response import Response

from .models import Institucion
from .serializers import InstitucionSerializer

class InstitucionListCreate(generics.ListCreateAPIView):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer
    
class InstitucionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer