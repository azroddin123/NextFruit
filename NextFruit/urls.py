from django.urls import path
from NextFruit.views import (
    CapsuleAPIView,
    GetOTPAPIView,
    MobileNumberAPIView,
    BatteryPercentageAPIView,
    VolumeAPIView,
    HardwareDetailsAPIView,
    BatteryPercentageUsingModuleAPIView,
    AddAccountAPIView,
    AllUsersAPIView,

    
)

urlpatterns = [
    path("get_otp", GetOTPAPIView.as_view()),
    path("capsule", CapsuleAPIView.as_view()),
    path("mobile_number", MobileNumberAPIView.as_view()),
    path("battery_percentage", BatteryPercentageAPIView.as_view()),
    path("volume", VolumeAPIView.as_view()),
    path("hardware_details", HardwareDetailsAPIView.as_view()),
    path("batter_using_package", BatteryPercentageUsingModuleAPIView.as_view()),
    path("add_account", AddAccountAPIView.as_view()),
    path("all_users", AllUsersAPIView.as_view()),
    # path('generic_users/<uuid:uuid>/',GenericApiView.as_view())
] 
