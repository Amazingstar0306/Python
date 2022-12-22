import os
# First, import folium package
import folium
from geopy.geocoders import Nominatim as NT

# Initialize Nominatim API
geo_locator = NT(user_agent="geoapiExercises")
# write the place
place_1 = "Yemen"

location_1 = geo_locator.geocode(place_1)
# now, it will search for the location by using the latitude and longitude, with zoom_start = 15
user_map1 = folium.Map(location=[location_1.longitude, location_1.latitude],
                       zoom_start=15)
# At last, open the base map
user_map1
#print(user_map1)