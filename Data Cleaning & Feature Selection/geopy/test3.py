"""计算距离"""
from geopy import distance
newport_ri = (29.312865650853063, 120.22639803225951)
cleveland_oh = (28.90452808981754, 120.0102472720782)
print(distance.distance(newport_ri, cleveland_oh).km)




# wellington = (-41.32, 174.81)
# salamanca = (40.96, -5.50)
# print(distance.distance(wellington, salamanca, ellipsoid='GRS-80').miles)
