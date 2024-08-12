import urllib.parse
from PIL import Image
import requests
from tkinter import *
from io import BytesIO
from PIL import Image, ImageTk

with open("key.txt", 'r') as file:
	key = file.readline()

def getImage(searchLoc = "18 CLARK ST Trenton"):
	safeLoc = urllib.parse.quote_plus(searchLoc)

	size = "640x640" #this is the best quality image they have

	location = safeLoc

	metaURL = f"https://maps.googleapis.com/maps/api/streetview/metadata?size={size}&location={location}&key={key}"
	url = f"https://maps.googleapis.com/maps/api/streetview?size={size}&location={location}&key={key}"

	metaResponse = requests.get(metaURL)
	metaJSON = metaResponse.json()

	if (metaJSON['status'] != 'OK'):
		print(f"Failed to get image for location '{searchLoc}'.")

		return None
	else:

		response = requests.get(url)

		return response.content

