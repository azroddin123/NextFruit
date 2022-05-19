from .models import Capsule, CapsuleDetails
from .serializers import CapsuleSerializer, CapsuleDetailsSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import psutil, random
    


battery = psutil.sensors_battery()
# print(battery)


class CapsuleAPIView(APIView):
    def get(self, request, *args, **kwargs):
        capsules = Capsule.objects.all()
        serializer = CapsuleSerializer(capsules, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        serializer = CapsuleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetOTPAPIView(APIView):
    def get(self, request, *args, **kwargs):
        random_object = Capsule.objects.all().order_by("?").first()
        serializer = CapsuleSerializer(random_object)
        return Response(data={"otp": serializer.data["otp"]}, status=status.HTTP_200_OK)


class MobileNumberAPIView(APIView):
    def get(self, request, *args, **kwargs):
        random_object = Capsule.objects.all().order_by("?").first()
        serializer = CapsuleSerializer(random_object)
        return Response(
            data={"mobile_number": serializer.data["mobile_number"]},
            status=status.HTTP_200_OK,
        )

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = CapsuleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={"Success": "Mobile Number Registered Successfully"},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            data={"Error": "Mobile Number Already Exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )


class BatteryPercentageAPIView(APIView):
    def get(self, request, *args, **kwargs):
        random_object = Capsule.objects.all().order_by("?").first()
        serializer = CapsuleSerializer(random_object)
        return Response(
            data={"Battery-Percentage": serializer.data["battery_percentage"]},
            status=status.HTTP_200_OK,
        )


class BatteryPercentageUsingModuleAPIView(APIView):
    def get(self, request, *args, **kwargs):
        battery = psutil.sensors_battery()
        battery_data = {
            "battery_percentage": round(battery.percent),
            "power-plugged": battery.power_plugged,
        }
        return Response(battery_data, status=status.HTTP_200_OK)

    # battery = psutil.sensors_battery()
    # return Response({})


class VolumeAPIView(APIView):
    def get(self, request, *args, **kwargs):
        random_object = Capsule.objects.all().order_by("?").first()
        serializer = CapsuleSerializer(random_object)
        return Response(
            data={"Volume": serializer.data["volume"]}, status=status.HTTP_200_OK
        )


class HardwareDetailsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        hardware_list = CapsuleDetails.objects.all().order_by("?").first()
        serializer = CapsuleDetailsSerializer(hardware_list)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddAccountAPIView(APIView):
    def get(self, request, *args, **kwargs):
        user_list = Capsule.objects.all().order_by("?").first()
        serializer = CapsuleSerializer(user_list)
        print(serializer)
        return Response(data={"email": serializer.data["email"], "password": serializer.data["password"]})

    def post(self, request, *arg , **kwargs) :
        serializer = CapsuleSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(data={ "Success" :  "Logged in Succefully"},status=status.HTTP_201_CREATED)
        return Response(data={"Error" : "Something Went Wrong"},status=status.HTTP_400_BAD_REQUEST)


class AllUsersAPIView(APIView):
    def get(self, request, *args, **kwargs):
        user_list = Capsule.objects.all()
        serializer = CapsuleSerializer(user_list,many=True)
        # print(serializer)
        return Response(data= serializer.data , status=status.HTTP_200_OK)
    


 # def post(self, request, *args, **kwargs):
    #     print(request.data)
    #     if request.data["mobile_number"]:
    #         print(request.data["mobile_number"])
    #         return Response(data = {"Success": "Mobile Number Registered Succefully"},
    #             status=status.HTTP_201_CREATED,
    #         )
    #     return Response(data = {"Error": "Something Went Wrong"}, status=status.HTTP_400_BAD_REQUEST
    # )


# class GenericApiView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin) :
#     serializer_class = CapsuleSerializer
    
    
#     queryset = Capsule.objects.all()
#     lookup_field = 'uuid'
    
#     def get(self,request,uuid = None) :
#         if uuid :
#             return self.retrieve(request)
#         else : 
#             return self.list(request)
    
#     def post(self,request) :
#         return self.create(request)
    
#     def put(self,request,uuid=None) : 
#         return self.update(request,uuid)
        
#     def delete(self,request,uuid) :
#         return self.destroy(request,uuid)

   

# class MobileNumberAPIView(APIView) :

#     def get(self,request,*args,**kwargs) :
#         return 'hi'

#     def post(self,request,*args,**kwargs) :
#                 serializer = CapsuleSerializer(data = request.data)
#                 print(request.data)
#                 if serializer.is_valid():
#                     serializer.save()
#                     return Response(serializer.data,status=status.HTTP_201_CREATED)
#                 return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

