import pandas
import folium

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

fg = folium.FeatureGroup(name="My Map")

marker_color = ''




for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(
        location=[lt, ln],
        popup="Elevation is " + str(el),
        icon=folium.Icon(color=color_producer(el)
        )))


fg.add_child(folium.GeoJson())



map.add_child(fg)


map.save("Map2.html")




