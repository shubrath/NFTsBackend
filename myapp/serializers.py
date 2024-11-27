# myapp/serializers.py
from rest_framework import serializers
from .models import NFTs

class NFTsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFTs
        fields = ['object_id', 'nft_id', 'approved','secreat_key','is_share']
