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
    dates, prcp = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        # error handling for missing data
        try:
            precip = float(row[3])  # prcp
        except ValueError:
            print(f'Missing data for {current_date}')
        else:
            dates.append(current_date)
            prcp.append(precip)

# plot highs and lows
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, prcp, c='blue', alpha=0.5) # controls transparency

# format plot
plt.title('WR Precipitation 2020', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Amount (In)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
