import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/pville_weather_1900_2023.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    #for index, column_header in enumerate(header_row):
        #print(index, column_header)
        
    #Get dates, and high and low temperatures from this file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[10])
            low = int(row[11])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
        
    # Plot the high and low temps
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)
    #ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    
    # Format plot.
    title = "Daily High and Low Temperatures - 1900-2023\nPhoenixville, PA"
    ax.set_title(title, fontsize=20)
    ax.set_xlabel("", fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)
    
    plt.show()