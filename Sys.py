import platform
import multiprocessing
import socket
import cpuinfo

#Prints some system info
print("Hardware Architecture =", platform.machine())
print("OS =",platform.system())
print("Hardware version =",platform.version())
# print("Windows edition =", platform.win32_ver(release='', version='', csd='', ptype=''))
# print("Windows edition =", platform.win32_edition())


#print("Processor Name =", platform.processor())
if __name__ == '__main__':
    from cpuinfo import get_cpu_info

    for key, value in get_cpu_info().items():
        print("{0}: {1}".format(key, value))

get_cpu_info()
print("Number of threads =", multiprocessing.cpu_count())
print("Hostname =", platform.node())

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print("Private IP Addresss =", (s.getsockname()[0]))
s.close()

#Desktop CPUs
#Intel


#Rocket Lake

if "Family 6 Model 167" in platform.processor():
    print("This system is a Desktop PC and it runs an Intel Core 11th Gen, Rocket Lake CPU")

#Comet Lake
elif "Family 6 Model 165" in platform.processor():
    print("This system is a Desktop PC and it runs an Intel Core 10th Gen, Comet Lake CPU")

#Coffee Lake
elif "Family 6 Model 158" in platform.processor():
    print("This system is a Desktop PC and it runs an Intel Core 8th Gen/9th Gen, Coffee Lake/Coffee Lake Refresh CPU")

#Kaby Lake
elif "Family 6 Model 158" in platform.processor():
    print("This system is a Desktop PC and it runs an Intel Core 7th Gen, Kaby Lake CPU")

#Skylake
elif "Family 6 Model 94" in platform.processor():
    print("This system is a Desktop PC and it runs an Intel Core 6th Gen, Skylake CPU")

#Broadwell
elif "Family 6 Model 71" in platform.processor():
    print("This system is a Desktop PC and it runs an Intel Core 5th Gen, Broadwell CPU")

#Haswell
elif "Family 6 Model 60" in platform.processor():
    print("This system is a Desktop PC and it runs an Intel Core 4th Gen, Haswell CPU")
#AMD
elif "Family 25 Model 80" in platform.processor():
    print("This system is a Desktop PC and it runs an AMD 5000 series {Zen3} Cezanne CPU")


#Intel
#Laptop CPUs
#Alder Lake (Mobile)
elif "Family 6 Model 154" in platform.processor():
    print("This system is a Laptop/Tablet and it runs an Intel Core 12th Gen Alder Lake (Mobile) P-Series (Ultimate mobile performance) CPU")

#Tiger Lake (Mobile)
elif "Family 6 Model 141" in platform.processor():
    print("This system is a Laptop/Tablet and it runs an Intel Core 11th Gen Comet Lake (Mobile) H-series (Ultimate mobile performance) CPU")

elif "Family 6 Model 140" in platform.processor():
    print("This system is a Laptop/Tablet and it runs an Intel Core 11th Gen Comet Lake (Mobile) U-Series (Medium power) CPU")

#Comet Lake/Amber Lake/Whiskey Lake/Coffee Lake/Kaby Lake (Mobile)
elif "Family 6 Model 142" in platform.processor():
    print("This system is a Laptop/Tablet and it runs an Intel Core 10th/8th/7th Gen Comet Lake/Amber Lake/Whiskey Lake/Coffee Lake/Kaby Lake (Mobile) U-Series/Y-Series (Medium power/Extremely-Low power) CPU")

#Ice Lake (Mobile)
elif "Family 6 Model 126" in platform.processor():
    print("This system is a Laptop/Tablet and it runs an Intel Core 10th Gen Ice Lake (Mobile) U-Series (Medium power) CPU")

elif "Family 6 Model 125" in platform.processor():
    print("This system is a Laptop/Tablet and it runs an Intel Core 10th Gen Ice Lake (Mobile) Y-Series (Extremely-Low power) CPU")

#Cannon Lake (Mobile)
elif "Family 6 Model 102" in platform.processor():
    print("This system is a Laptop/Tablet and it runs an Intel Core 8th Gen Cannon Lake (Mobile) U-Series (Medium power) CPU")

#Skylake (Mobile)
elif "Family 6 Model 78" in platform.processor():
    print("This system is a Laptop/Tablet and it runs an Intel Core 6th Gen Skylake (Mobile) U-Series/Y-Series (Medium power/Extremely-Low power) CPU")

#Broadwell (Mobile)
elif "Family 6 Model 61" in platform.processor():
    print("This system is a Laptop/Tablet and it runs an Intel Core 5th Gen Broadwell (Mobile) U-Series/Y-Series/S-Series (Medium power/Extremely-Low power) CPU")

#Not configured
#else:
 #   print("Undefined")


#Require User input for better results
