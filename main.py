import urllib.parse
from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO
import os

searchLoc = "18 CLARK ST Trenton"

safeLoc = urllib.parse.quote_plus(searchLoc)

size = "640x640" #this is the best quality image they have

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
	imgObj = Image.open(BytesIO(response.content))

	print(date)


root = Tk()
img = ImageTk.PhotoImage(imgObj)
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()