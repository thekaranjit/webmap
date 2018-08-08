import pandas


import folium.plugins

data = pandas.read_csv("volcano.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return'orange'
    else:
        return 'red'

map = folium.Map(
    location=[38.58, -99.09],
    zoom_start=6,
    tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name="Volcanos")

marker_color = ''




for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.Marker(
        location=[lt, ln],
        popup="Elevation is " + str(el),
        icon=folium.Icon(color=color_producer(el)
        )))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(
    data=open('world.json', 'r', encoding='utf-8-sig'),
    style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 1000000 <= x['properties']['POP2005'] < 2000000 else 'red'}))





map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("Map4.html")




