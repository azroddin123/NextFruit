# import bluetooth

# # nearby_devices = bluetooth.discover_devices()
# nearby_devices = bluetooth.discover_devices(lookup_names=True,
#                                                       flush_cache=True, lookup_class=False)

# print(nearby_devices)


# addr= "B4:C4:FC:CB:6A:F8"
# port=1

# sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
# sock.connect((addr, 1))
# sock.send('Azhar hi')
# import bluetooth

# devices = bluetooth.discover_devices(lookup_names = False, flush_cache = True, duration = 20)


# print (bluetooth.lookup_name(devices[0]))

# for services in bluetooth.find_service(address = devices[0]):
#     print (" Name: %s" % (services["name"]))
#     print (" Description: %s" % (services["description"]))
#     print (" Protocol: %s" % (services["protocol"]))
#     print (" Provider: %s" % (services["provider"]))
#     print (" Port: %s" % (services["port"]))
#     print (" Service id: %s" % (services["service-id"]))
#     print ("")
 

# s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
# s.connect((devices[0],1))


import psutil
import os
battery = psutil.sensors_battery()
print(battery)

# int level = batteryStatus != null ? 
# batteryStatus.getIntExtra(BatteryManager.EXTRA_LEVEL, -1) : -1; int scale = 
# batteryStatus != null ? batteryStatus.getIntExtra(BatteryManager.EXTRA_SCALE, -1) : -1; 
# double batteryPct = (double) level / (double) scale; int percent = (int) (batteryPct * 100D);