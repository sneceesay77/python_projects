import json

#Building a world map
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline



#Explore teh structure of the data
filename = 'eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)
    
readable_file = 'readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)
    
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

#Extracting magnitudes
mags, lons, lats = [], [], []
for eq_dicts in all_eq_dicts:
    mag = eq_dicts['properties']['mag']
    lon = eq_dicts['geometry']['coordinates'][0]
    lat = eq_dicts['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:10])
print(lats[:10])

#one way of specifying chart data
#data = [Scattergeo(lon=lons, lat=lats)]

#another way of specifying chart data
data = [{
    'type': 'scattergeo', 
    'lon': lons, 
    'lat': lats,
    'marker':{
        'size': [5*mag for mag in mags]
    },
}]

my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')