"""
====================================================================================================================
Author: Brijan Iyer
Description: Switch the laptop display's refresh rate based on available refresh rates when in battery powered mode.
Version: 0.1
====================================================================================================================
"""

import psutil
import win32api 
import win32con
import pywintypes
import wmi
import pythoncom
from winreg import *
from apscheduler.schedulers.background import BackgroundScheduler


"""
Switching the refresh rate of the laptop's display. However, If an external monitor is connected Nvidia Optimus is the only option enabled
and laptop display configuration will be disabled. Hence, refresh rates can't be changed and in this situation the refresh rate of only the external monitor would update.
"""
sched = BackgroundScheduler()

def update_refrate():
    pythoncom.CoInitialize()
    
    acmode = psutil.sensors_battery().power_plugged #Get AC plugged in state
    hklmcon = ConnectRegistry(None, HKEY_LOCAL_MACHINE) #Access HKLM registry
    smtfanevnt = OpenKey(hklmcon,r"SOFTWARE\Lenovo\ImController\PluginData\GamingPlugin\Event\FanManagerPlugin\SmartFanModeEvent") # Lenovo Vantage Smart Fan mode event registry path for stored settings
    smartfanmode = QueryValueEx(smtfanevnt, "SmartFanMode") # Lenovo Vantage updates SmartFanMode registry key when switching between silent, balanced and performance thermal modes. Silent = (1,4), balanced (2,4) and performance = (3,4)
    win32dev = pywintypes.DEVMODEType() #Utilize win32con DEVMODE to programmatically set display frequency
    win32dev.Fields = win32con.DM_DISPLAYFREQUENCY
    win32vidcon = wmi.WMI().Win32_VideoController()

    """Get Max Refresh Rate from Win32_VideoController using WMI and store in a list"""
    gpurefrates = list() #It is possible to have multi connected displays. Hence, fetch all connected display's refresh rates in a list.
    for getmaxrefrate in win32vidcon:
        maxrefrate = getmaxrefrate.wmi_property('MaxRefreshRate').value
        gpurefrates.append(maxrefrate)
        
    """Conditionally set min freq to 60hz when on battery or max out to max avialable refresh rate on AC power"""
    if (acmode == False) and (smartfanmode == (1, 4)):
        win32dev.DisplayFrequency = 60
        win32api.ChangeDisplaySettings(win32dev, 0)
        refrate=str(win32dev.DisplayFrequency) + "hz"
        print(refrate, acmode, smartfanmode)
        
    if (acmode == True):
        win32dev.DisplayFrequency = gpurefrates[0] or gpurefrates[1] #Currently only sets upto one externally connected display ref rate and laptop display ref rate. 
        win32api.ChangeDisplaySettings(win32dev, 0)
        refrate=str(win32dev.DisplayFrequency) + "hz"
        print(refrate, acmode, smartfanmode)
  
sched.add_job(update_refrate,'interval',seconds=3)
sched.start()

    

