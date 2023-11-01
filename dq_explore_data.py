import json

# Explore the structure of the data
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)
    
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

mags = []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    mags.appeng(mag)