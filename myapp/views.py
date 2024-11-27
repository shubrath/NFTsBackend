# myapp/views.py
from rest_framework import generics,viewsets
from .models import NFTs
from .serializers import NFTsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

# List all NFTs or create a new one
class NFTsListCreateView(generics.ListCreateAPIView):
    print("hello")
    queryset = NFTs.objects.all()
    serializer_class = NFTsSerializer
    if serializer_class.errors:
        print(serializer_class.errors)

# Retrieve, update, or delete a specific NFT
class NFTsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NFTs.objects.all()
    serializer_class = NFTsSerializer
    lookup_field = 'id'


    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ApproveNftView(viewsets.ModelViewSet):
    print("inside the approved function")
    @action(detail=False, methods=['patch'], url_path=r'update-nft/(?P<pk>[^/.]+)')
    def update_nft_by_id(self, request, pk=None):
        """
        Updates an NFT by its primary key (pk).
        """
        try:
            # Find the NFT by primary key
            print("fteching the nft...",pk)
            nft = NFTs.objects.get(nft_id=str(pk))
        except NFTs.DoesNotExist:
            return Response({'error': 'NFT not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # Use the NFTUpdateSerializer to validate and update only specific fields
        serializer = NFTsSerializer(nft, data=request.data, partial=True)  # partial=True allows partial updates
        if serializer.is_valid():
            serializer.save()  # Updates only the fields provided in the request data
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)