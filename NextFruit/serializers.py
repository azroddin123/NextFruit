
from pyrsistent import field
from rest_framework import serializers
from .models import Capsule, CapsuleDetails

class CapsuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capsule
        fields = '__all__'
        

class CapsuleDetailsSerializer(serializers.ModelSerializer) :
    class Meta :
        model =  CapsuleDetails
        fields = '__all__'
        
        

