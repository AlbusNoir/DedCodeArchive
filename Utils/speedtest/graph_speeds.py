import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import csv
import datetime

times = []
download = []
upload = []
avg_down = []
avg_up = []

cur_date = datetime.datetime.now().strftime("%Y%m%d")
cur_date_str = str(cur_date)
ext = ".csv"
ext2 = ".png"
speedtest_file = cur_date_str + ext
speedtest_image = cur_date_str + ext2

with open(speedtest_file, 'r') as csv_file:
    plots = csv.reader(csv_file, delimiter=',')
    next(csv_file)
    for row in plots:
        if row:
            times.append(str(row[0]))
            download.append(float(row[1]))
            upload.append(float(row[2]))

#print(time, '\n', download, '\n', upload)

avg_dl = sum(download) / len(download)
avg_ul = sum(upload) / len(upload)

for x in range(0, len(download)):
    avg_down.append(avg_dl)
    
for y in range(0, len(upload)):
    avg_up.append(avg_ul)

plt.figure()
plt.plot(times, download, label='Download', color='r')
plt.plot(times, upload, label='Upload', color='b')
plt.plot(times, avg_down, label='Avg Download', color='c')
plt.plot(times, avg_up, label='Avg Upload', color='m')
plt.xlabel('Time')
plt.ylabel('Speed in Mb/s')
plt.title("Internet Speed")
plt.legend()
plt.savefig(speedtest_image, bbox_inches='tight')
plt.show()
