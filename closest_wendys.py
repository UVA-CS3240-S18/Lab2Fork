# Mark Sherriff (mss2x)

import math
import webbrowser
#Note: the requests library must be installed for this change to work
import requests
import json

google_maps_url = "https://www.google.com/maps/@35.372742,-81.954957,15z?hl=en"

def distance_between(lat_1, lon_1, lat_2, lon_2):
    theta = lon_1 - lon_2
    dist = math.sin(lat_1 * math.pi / 180.0) * math.sin(lat_2 * math.pi / 180.0) + math.cos(lat_1 * math.pi / 180.0) * math.cos(lat_2 * math.pi / 180.0) * math.cos(theta * math.pi / 180.0)
    dist = math.acos(dist)
    dist = dist * 180.0 / math.pi
    dist = dist * 60 * 1.1515

    return dist

geo_locator_url = 'http://freegeoip.net/json'
response = requests.get(geo_locator_url)
result = json.loads(response.text)
lon = result['longitude']
lat = result['latitude']
datafile = open("wendys.csv", "r")

closest_dist = 200
closest_wendys = ""

for line in datafile:
    entry = line.split(";")
    dist_to_wendys = distance_between(lat, lon, float(entry[0]), float(entry[1]))
    if dist_to_wendys < closest_dist:
        google_maps_url = "https://www.google.com/maps?q=" + str(entry[4]) + "+" + str(entry[5]) + "+" + str(entry[6])
        print(google_maps_url)
        closest_dist = dist_to_wendys
        closest_wendys = entry[2]

datafile.close()

print("The closest Wendy's (", closest_wendys, ") is", closest_dist, "miles away.")
google_maps_url = google_maps_url.replace(' ', '+')
webbrowser.open(google_maps_url)

