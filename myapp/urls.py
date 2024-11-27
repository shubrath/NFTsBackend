# myapp/urls.py
from django.urls import path
from .views import NFTsListCreateView, NFTsDetailView,ApproveNftView

urlpatterns = [
    path('nfts/', NFTsListCreateView.as_view(), name='nfts-list-create'),
    path('nfts/<str:id>/', NFTsDetailView.as_view(), name='nfts-detail'),
    path('api/nfts/<str:pk>/', NFTsDetailView.as_view(), name='nft-detail'),

]
