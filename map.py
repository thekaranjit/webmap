import folium

map = folium.Map(
    location=[20.59, 78.96],
    zoom_start=6,
    tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")

for cordinate in [[20.2, 78.1],[21.2, 76.1]]:
    fg.add_child(folium.Marker(
        location=cordinate,
        popup="Hi Iam a Marker",
        icon=folium.Icon(color='green'
        )))


map.add_child(fg)


map.save("Map1.html")




