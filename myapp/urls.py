# myapp/urls.py
from django.urls import path
from .views import NFTsListCreateView, NFTsDetailView,ApproveNftView
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router  = DefaultRouter()

router.register(r'myNfts', ApproveNftView,basename="myNft")

urlpatterns = [
    path('', include(router.urls)),  # This includes all routes from the DefaultRouter

    path('nfts/', NFTsListCreateView.as_view(), name='nfts-list-create'),
    path('nfts/<str:id>/', NFTsDetailView.as_view(), name='nfts-detail'),
    # path('nftss/<int:pk>/', ApproveNftView.as_view(), name='nft-detail'),

]
