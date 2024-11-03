# myapp/urls.py
from django.urls import path
from .views import NFTsListCreateView, NFTsDetailView

urlpatterns = [
    path('nfts/', NFTsListCreateView.as_view(), name='nfts-list-create'),
    path('nfts/<str:id>/', NFTsDetailView.as_view(), name='nfts-detail'),
]
