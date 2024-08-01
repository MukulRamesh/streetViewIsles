import urllib.parse
from PIL import Image
import requests
from io import BytesIO
import json


searchLoc = "18 CLARK ST Trenton"

safeLoc = urllib.parse.quote_plus(searchLoc)

size = "6000x3000" #this just returns a nice quality image. the actual 

location = safeLoc
with open("key.txt", 'r') as file:
	key = file.readline()



metaURL = f"https://maps.googleapis.com/maps/api/streetview/metadata?size={size}&location={location}&key={key}"
url = f"https://maps.googleapis.com/maps/api/streetview?size={size}&location={location}&key={key}"

metaResponse = requests.get(metaURL)
metaJSON = metaResponse.json()

if (metaJSON['status'] != 'OK'):
	print(f"Failed to get image for location '{searchLoc}'.")
else:
	date = metaJSON.get("date")
	response = requests.get(url)
	img = Image.open(BytesIO(response.content))

	print(date)
	img.save("./output.png")