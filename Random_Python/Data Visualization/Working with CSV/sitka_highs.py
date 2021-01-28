'''
    From python crash course
    working with csv files
'''
import csv

filename = 'sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    ''' print the headers and their positions '''
    #for index, column_header in enumerate(header_row):
    #    print(index, column_header)

    ''' get high temps from file '''
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

print(highs)
