import psutil


cuse = psutil.disk_usage('c:')
print('C: information: ' + str(cuse))

#duse = psutil.disk_usage('d:')
#print('D: information: ' + str(duse))

input('press enter to end')
