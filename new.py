# import device

# target_name = "My Phone"
# target_address = None

# # nearby_devices = bluetooth.discover_devices()
# nearby_devices = device.discover_devices(duration=14,lookup_names=True,
#                                         flush_cache=True, lookup_class=False)


# print(nearby_devices)


import ctypes
print(dir(ctypes))

from ctypes import wintypes

class SYSTEM_POWER_STATUS(ctypes.Structure):
    _fields_ = [
        ('ACLineStatus', wintypes.BYTE),
        ('BatteryFlag', wintypes.BYTE),
        ('BatteryLifePercent', wintypes.BYTE),
        ('Reserved1', wintypes.BYTE),
        ('BatteryLifeTime', wintypes.DWORD),
        ('BatteryFullLifeTime', wintypes.DWORD),
    ]

SYSTEM_POWER_STATUS_P = ctypes.POINTER(SYSTEM_POWER_STATUS)

# GetSystemPowerStatus = ctypes.pydll.LoadLibrary.
# GetSystemPowerStatus.argtypes = [SYSTEM_POWER_STATUS_P]
# GetSystemPowerStatus.restype = wintypes.BOOL

status = SYSTEM_POWER_STATUS()
print(status)

# if not GetSystemPowerStatus(ctypes.pointer(status)):
#     raise ctypes.WinError()

print('ACLineStatus', status.ACLineStatus)
print('BatteryFlag', status.BatteryFlag)
print('BatteryLifePercent', status.BatteryLifePercent)
print('BatteryLifeTime', status.BatteryLifeTime)
print('BatteryFullLifeTime', status.BatteryFullLifeTime)