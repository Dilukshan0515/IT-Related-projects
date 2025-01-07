#Checking the windows version using python
#installing wmi library --> pip install wmi
import wmi
data=wmi.WMI()
for os_name in data.win32_Operatingsystem():
    print(os_name.Caption)
