
"""
将查询地理定位到地址和坐标
"""
from geopy.geocoders import Baidu, Bing, GoogleV3, DataBC, Nominatim

# geolocator = Nominatim(user_agent="specify_your_app_name_here")
geolocator = Baidu('EiQTTRKzlV3dKN1zcZ3c7iVhIl126xvC')
# geolocator = Bing('Ajg52RB8D2BIXygYwUTcJytDGsgqURLj5lfBptOH4jmTGHHFUvt0cMqdhdhdYfr-')
# geolocator = GoogleV3('AIzaSyAVwjaaOBKbssuyQsvyqQAQDwfuzO1PKCA')

location = geolocator.geocode("浙江金华市东阳市江北街道歌山北路280号")
print(location.address)
print((location.latitude, location.longitude))

