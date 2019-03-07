"""查找与一组坐标对应的地址"""
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="specify_your_app_name_here")
location = geolocator.reverse("52.509669, 13.376294")
print(location.address)

print((location.latitude, location.longitude))

print(location.raw)
