'''
    Weather chart for WR GA 31088
'''
import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'WR-Weather-Data-2020.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # get dates and high temps
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        # error handling for missing data
        try:
            high = int(row[6])  # tmax
            low = int(row[7])   # tmin
        except ValueError:
            print(f'Missing data for {current_date}')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# plot highs and lows
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5) # controls transparency
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)  # shade between the highs and lows

# format plot
plt.title('WR High - Lows Current', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
