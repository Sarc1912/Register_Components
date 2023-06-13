import platform
import psutil
import numpy as np



print("Architecture :", platform.architecture()[0])

print("[+] Machine :", platform.machine())

print("[+] System Name :",platform.system())

print("[+] Operating System Release :", platform.release())

print("[+] Number of Physical cores :", psutil.cpu_count(logical=False))
print("[+] Number of Total cores :", psutil.cpu_count(logical=True))
print("n")




def bytes_to_GB(bytes):
    gb = bytes/(1024*1024*1024)
    gb = round(gb, 2)
    return gb

# Using the virtual_memory() function it will return a tuple
virtual_memory = psutil.virtual_memory()

#This will print the primary memory details
print("[+] Total Memory present :", bytes_to_GB(virtual_memory.total), "Gb")
print("[+] Total Memory Available :", bytes_to_GB(virtual_memory.available), "Gb")
print("[+] Total Memory Used :", bytes_to_GB(virtual_memory.used), "Gb")
print("[+] Percentage Used :", virtual_memory.percent, "%")
print("n")

psutil.disk_partitions()