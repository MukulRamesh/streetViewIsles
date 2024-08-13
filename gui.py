import tkinter as tk
from tkinter import ttk
from io import BytesIO
import keyboard
from PIL import Image, ImageTk

import getImage
import spreadsheet

root = tk.Tk()


label = ttk.Label(root, text="""
Keyboard support:
Press "Space" to confirm that the label (near the bottom) is correct: Use the "Up" or "Down" arrow keys to select a new label if not.
Press "Enter" to move to the next image. Press "Esc" to back to the previous image.""", font=('Helvetica', '12'))
label.pack(ipadx=10, ipady=10)

LabelText = tk.StringVar()
LabelText.set('[SAMPLE TEXT]')

label = ttk.Label(root,
                    textvar=LabelText, padding=10, relief="solid", font=('Helvetica', '15', 'bold'))
label.pack(side = "bottom", fill="both", expand=True, padx=10, pady=10)

def setLabelText():
	LabelText.set(f"{spreadsheet.getLabel()} :: {spreadsheet.getAddress()} :: {spreadsheet.getIndex()}/{spreadsheet.getTotalRecords()}")


imgObj = Image.open("loading.jpg")
img = ImageTk.PhotoImage(imgObj)
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

def setImage(image):
	imgObj = Image.open(image)
	img = ImageTk.PhotoImage(imgObj)

	panel.config(image = img)
	panel.image = img
	panel.update_idletasks()

def setDefaultImage():
	setImage("loading.jpg")

def nextEntry():
	setDefaultImage()
	spreadsheet.incrementIndex()

	image = getImage.getImage(spreadsheet.getAddress())
	while image == None:
		spreadsheet.markUnfound()
		spreadsheet.incrementIndex()
		image = getImage.getImage(spreadsheet.getAddress())

	setLabelText()
	setImage(BytesIO(image))

nextEntry() # Initialize the first image

def prevEntry():
	setDefaultImage()
	spreadsheet.decrementIndex()

	image = getImage.getImage(spreadsheet.getAddress())
	while image == None:
		spreadsheet.markUnfound()
		spreadsheet.decrementIndex()
		image = getImage.getImage(spreadsheet.getAddress())

	setLabelText()
	setImage(BytesIO(getImage.getImage(spreadsheet.getAddress())))

confTKVar = tk.BooleanVar()

def switchConfirmationVar():
	val = confTKVar.get()
	confTKVar.set(not val)


style = ttk.Style().configure('TCheckbutton', font=('Helvetica', 12))
ttk.Checkbutton(root,
				text='Is the current label correct?',
				variable=confTKVar,
				onvalue=True,
				offvalue=False).pack()

keyboard.add_hotkey('space', switchConfirmationVar)
keyboard.add_hotkey('enter', nextEntry)
keyboard.add_hotkey('escape', prevEntry)


root.mainloop()
