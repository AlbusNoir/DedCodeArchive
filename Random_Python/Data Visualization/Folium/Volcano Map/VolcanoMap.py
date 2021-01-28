# folium map displaying volcanoes
import folium
import pandas

# credit for data:
# Global Volcanism Program, 2013. Volcanoes of the World, v. 4.9.0. Venzke, E (ed.). Smithsonian Institution.
# Downloaded 23 Jun 2020
data = pandas.read_excel("Holocene_Volcanoes_Edit.xlsx")

# convert columns to lists
lat = list(data["Latitude"])
lon = list(data["Longitude"])
elev = list(data["Elevation"])
name = list(data["Volcano Name"])
country = list(data["Country"])
type = list(data["Primary Volcano Type"])
status = list(data["Last Known Eruption"])


# colour coding function
def elev_color(elevation):
    if elevation < 500:
        return 'green'
    elif 500 <= elevation < 1000:
        return 'yellow'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


# html for google search link based on name
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Country: %s<br>
Height: %s (m)<br>
Type: %s<br>
Last Known Eruption: %s
"""

# location in lat/long
# no_wrap, max_bounds, min_zoom, max_zoom control the map look
# only point not fully visible is top: East Gakkel Ridge.
# you can still drag to it though
map = folium.Map(location = [37, -93],
                 zoom_start = 4,
                 tiles = "Stamen Terrain",
                 no_wrap = True,
                 max_bounds = True,
                 min_zoom = 3,
                 max_zoom = 15
                 )

# volcano groups
fg = folium.FeatureGroup(name="Volcanoes")

# utilize zip to iterate lists
for lt, ln, el, name, type, status, ctry in zip(lat, lon, elev, name, type, status, country):
    iframe = folium.IFrame(html=html % (name, name, ctry, el, type, status), width=200, height=100)
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=folium.Popup(iframe), fill_color=(
            elev_color(el)), color='grey', fill_opacity=0.7))
# layer control must be after fg add
map.add_child(fg)

map.save("VolcanoMap.html")
