from django.db import models

class NFTs(models.Model):
    object_id = models.CharField(max_length=255, unique=True) 
    nft_id = models.CharField(max_length=255, unique=True)    
    approved = models.CharField(max_length=50)    
    is_share = models.BooleanField(default=False)
    secreat_key = models.CharField(max_length=50,default = " ")    

    def __str__(self):
        return self.nft_id