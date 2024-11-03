# myapp/views.py
from rest_framework import generics
from .models import NFTs
from .serializers import NFTsSerializer

# List all NFTs or create a new one
class NFTsListCreateView(generics.ListCreateAPIView):
    print("hello")
    queryset = NFTs.objects.all()
    serializer_class = NFTsSerializer

# Retrieve, update, or delete a specific NFT
class NFTsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NFTs.objects.all()
    serializer_class = NFTsSerializer
    lookup_field = 'id'
