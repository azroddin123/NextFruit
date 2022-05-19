from django.contrib import admin
from importlib_metadata import version

# Register your models here.
from .models import Capsule, CapsuleDetails

class AdminCapsule(admin.ModelAdmin):
    model = Capsule
    list_display = ('otp','mobile_number','volume','battery_percentage')

class AdminCapsuleDetails(admin.ModelAdmin) :
    model = CapsuleDetails
    list_display = ('id','model_name','manufacturer','version','host','device_id')
   


admin.site.register(Capsule,AdminCapsule)
admin.site.register(CapsuleDetails,AdminCapsuleDetails)


