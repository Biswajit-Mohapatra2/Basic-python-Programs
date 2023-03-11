import os
import shutil
#Printing present working directory
print(os.getcwd())
#For checking System Disk Usages and free disk

print(shutil.disk_usage("/")) 
        #OR
total, used, free = shutil.disk_usage("/")
print(f"Total Disk Space Is: {total // (2 ** 30)} GB")
print(f"Used Disk Space Is: {used // (2 ** 30)} GB")
print(f"Free Disk Space Is: {free // (2 ** 30)} GB" )

