# myapp/views.py
from rest_framework import generics
from .models import NFTs
from .serializers import NFTsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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
    

class ApproveNftView(APIView):
    def patch(self, request, pk):
        try:
            # Get the NFT object by primary key (pk)
            nft = NFTs.objects.get(pk=pk)

            # Update the `approved` field
            approved = request.data.get('approved', None)
            if approved is not None:
                nft.approved = approved
                nft.save()
                return Response({"message": "NFT approved successfully"}, status=status.HTTP_200_OK)
            
            return Response({"error": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)
        except NFTs.DoesNotExist:
            return Response({"error": "NFT not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
