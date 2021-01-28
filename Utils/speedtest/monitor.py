import speedtest
import datetime
import time
import csv

s = speedtest.Speedtest()

cur_date = datetime.datetime.now().strftime("%Y%m%d")
cur_date_str = str(cur_date)
ext = ".csv"
f = cur_date_str + ext

counter = 10
test_num = 1

with open(f, 'w', newline = "") as testcsv:
    csv_writer = csv.DictWriter(testcsv, fieldnames = ['time', 'down', 'up'])
    csv_writer.writeheader()
    while counter != 0:
        print(f'Running test {test_num}')
        time_now = datetime.datetime.now().strftime("%H:%M")
        downspeed = round((round(s.download()) / 1048567), 2)
        upspeed = round((round(s.upload()) / 1048576), 2)

        csv_writer.writerow({'time': time_now, 'down': downspeed, 'up': upspeed})

        time.sleep(60)
        counter -= 1
        test_num += 1

input('Testing Finished')
