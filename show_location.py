import folium
import os,sys
import webbrowser

from geopy.geocoders import Nominatim

address= str(sys.argv[1])
geolocator = Nominatim(user_agent="FUN Project")
location = geolocator.geocode(address)
longitude = location.latitude
latitude = location.longitude




map = folium.Map(location=[longitude,latitude])
folium.Marker(location=[longitude,latitude ],popup='Default popup Marker1',tooltip='Click here to see Popup').add_to(map)
map.save("show_location.html")
webbrowser.open('file://' + os.path.realpath("show_location.html"))

