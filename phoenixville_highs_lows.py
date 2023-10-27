import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/pville_weather_1900_2023.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    for index, column_header in enumerate(header_row):
        print(index, column_header)