#install phonenumbers package
import phonenumbers
from phonenumbers import geocoder

number = int(input(""))

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, 'en')


print(location) #This prints the country


#location of phone number in google map

#install opencage package
import opencage

from opencage.geocoder import OpenCageGeocode

#Get api key from opencage site

key = 'api_key'

geocoder = OpenCageGeocode(key)
query = str(location) 
results = geocoder.geocode(query)
print(results) #This prints the location details including cordinates

#Dislay it on google maps

#install folium package
import folium

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']


myMap = folium.Map(location=[lat, lng], zoom.start= 9)

folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save('mylocation.html')#Saves the map in html format
