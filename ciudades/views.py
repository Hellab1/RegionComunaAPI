# Elementos necesarios para que el API REST funcione 
from rest_framework import generics
 
from .serializers import RegionSerializer
 
from .models import Region
 
# Create your views here.
 
class CiudadesViewSet(generics.ListAPIView):    
    
    queryset = Region.objects.all()
    serializer_class = RegionSerializer