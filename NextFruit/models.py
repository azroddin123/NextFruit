from uuid import uuid4
from django.db import models

# from sqlalchemy import null

class Capsule(models.Model) :
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    username =  models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    password = models.CharField(max_length=100,null=True,blank=True)
    capsule_id = models.IntegerField(blank=True,null=True)
    otp = models.IntegerField(blank=True,null=True)
    volume = models.IntegerField(blank=True,null=True)
    mobile_number = models.PositiveIntegerField(blank=True,null=True,unique=True)
    battery_percentage = models.IntegerField(blank=True,null=True)
    class Meta :
         db_table = "capsule"
        
class CapsuleDetails(models.Model) :
    id = models.IntegerField(primary_key=True)
    model_name = models.CharField(max_length=100,blank=True,null=True)
    device = models.CharField(max_length=30,blank=True,null=True)
    manufacturer = models.CharField(max_length=100,blank=True,null=True)
    device_id = models.CharField(max_length=100,blank=True,null=True)
    physical_device = models.BooleanField(default=False,blank=True,null=True)
    host = models.CharField(max_length=100,blank=True,null=True)
    version = models.IntegerField(blank=True,null=True)
    class Meta :
         db_table = "capsuledetails"
