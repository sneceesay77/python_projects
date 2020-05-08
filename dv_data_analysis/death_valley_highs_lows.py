import csv
import matplotlib.pyplot as plt
from datetime import datetime

#filename = 'sitka_weather_07-2018_simple.csv'
filename = 'death_valley_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    head_row = next(reader)
    print(head_row)
    
    for index, column_header in enumerate(head_row):
        print(index, column_header)
    
    #Get Max temperatures
    highs, dates, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])    
            low = int(row[5])     
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    #print(highs)
    #print(dates)
    
#Plot high and low temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#Format plots
plt.title("Daily high and low temperatures in 2018\nDeath Valley, CA", fontsize=24)
plt.xlabel("", fontsize = 16)
plt.ylabel("Temperature (F)", fontsize=16)
fig.autofmt_xdate()
plt.tick_params(axis='both', which='major', labelsize='16')
plt.show()
    
