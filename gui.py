import tkinter as tk
from tkinter import ttk
from io import BytesIO
import keyboard
from PIL import Image, ImageTk

import getImage
import spreadsheet

root = tk.Tk()
root.title("Streetview Label Utility - Mukul Ramesh")

infoLabel = ttk.Label(root, text="""
Keyboard support:
Press "Space" to confirm that the label (near the bottom) is correct: Use the "Up" or "Down" arrow keys to select a new label if not.
Press "Esc" if the image is obscured in some way (for example, the plot is blurred, a tree is in the way, etc)
Press "Right Arrow" to move to the next image. Press "Left Arrow" to back to the previous image.""", font=('Helvetica', '12'))
infoLabel.pack(ipadx=10, ipady=10)





LabelOptions = ["OCCUPIED BUILDING","VACANT LOT","VACANT BUILDING","LOT","PARK / OPEN SPACE","PARKING LOT","UTILITY / RAIL","VACANT STOREFRONT"]
SelectedLabelOption = tk.IntVar(root, 0)
LabelOptionsText = tk.StringVar(root, LabelOptions[SelectedLabelOption.get()])
LabelOptionsDropDown = tk.OptionMenu(root, LabelOptionsText, *LabelOptions)
LabelOptionsDropDown.pack()

def moveLabelOptionDown():
	curLabelNum = SelectedLabelOption.get()
	if (curLabelNum < len(LabelOptions) - 1):
		curLabelNum += 1
		SelectedLabelOption.set(curLabelNum)
		LabelOptionsText.set(LabelOptions[curLabelNum])


def moveLabelOptionUp():
	curLabelNum = SelectedLabelOption.get()
	if (curLabelNum > 0):
		curLabelNum -= 1
		SelectedLabelOption.set(curLabelNum)
		LabelOptionsText.set(LabelOptions[curLabelNum])


ExcelLabelText = tk.StringVar()
ExcelLabelText.set('[SAMPLE TEXT]')
excelLabel = ttk.Label(root,
                    textvar=ExcelLabelText, padding=10, relief="solid", font=('Helvetica', '15', 'bold'))
excelLabel.pack(side = "bottom", fill="both", expand=True, padx=10, pady=10)
def setExcelLabelText():
	ExcelLabelText.set(f"{spreadsheet.getLabel()} :: {spreadsheet.getAddress()} :: {spreadsheet.getIndex()}/{spreadsheet.getTotalRecords()}")


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

	setExcelLabelText()
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

	setExcelLabelText()
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

keyboard.add_hotkey('up', moveLabelOptionUp)
keyboard.add_hotkey('down', moveLabelOptionDown)


keyboard.add_hotkey('right', nextEntry)
keyboard.add_hotkey('left', prevEntry)


root.mainloop()
