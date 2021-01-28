# spawned as a result of researching into will's thing
# get disk space from psutil then run some conversions
# end result is to get from the output to something we understand

import psutil

# drive = psutil.disk_usage('c:')
drive = input('''What disk are you looking for info on?
Enter as letter: with the colon. 
> ''')

# print all info (total, used, free, percent)
drive_str = str(drive)
print(f'Disk usage for disk {drive_str}')

# strip out the used for below and total because why not
used = psutil.disk_usage(drive).used
total = psutil.disk_usage(drive).total

print(f'Disk is using {used} b out of {total} b')

'''
at this point we assume this is in bytes in BINARY(base2)
that's fine. we can just do simple math to convert that
we can actually do it using base10 too so
'''


ki = used / 1024
kb = used / 1000
print(f'Disk {drive_str} is using {ki} Kibibytes, which is {kb} Kilobytes')

mi = ki / 1024
mb = kb / 1000
print(f'Disk {drive_str} is using {mi} Mebibytes, which is {mb} Megabytes')

gi = mi / 1024
gb = mb / 1000
print(f'Disk {drive_str} is using {gi} Gibibytes, which is {gb} Gigabytes')

ti = gi / 1024
tb = gb / 1000
print(f'Disk {drive_str} is using {ti} Tebibytes, which is {tb} Terabytes')

# can be expanded for pebi/peta, exbi/exa, zebi/zetta, yobi/yotta

input('Done')  # lazy holder so you can see console output
