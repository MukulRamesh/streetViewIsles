import pandas as pd
import numpy as np
from datetime import datetime

print("Reading spreadsheet data (this may take a few seconds...)")
excelDF = pd.read_excel("COMPARISONS TRENTON_MASTER.xlsx", verbose=True)[["address", "parc_type2019"]]
excelDF = excelDF.replace(to_replace=' ', value=np.nan).replace(to_replace='CANAL', value=np.nan).dropna() # remove all entries whose address fields are empty, or "CANAL"
excelDF = excelDF.drop_duplicates(subset=["address"]) # we only care about unique address

df = pd.DataFrame(columns=["Index", "Address", "2019 Label", "Human Checked Label", "Image Not Found", "Image Obscured"])

# index = df.index[0] #gets the row number of the first entry that of the data frame (corresponds to the excel row number)

currentIndex = -1 # initialization adds 1. Serves purpose of debugging empty spreadsheet
currentEntry = {"Index": None, "Address": None, "2019 Label": None, "Human Checked Label": None, "Human Check Time": None, "Image Not Found": "FALSE", "Image Obscured": "FALSE"}

def getAddress():
    return excelDF.iloc[currentIndex]["address"]

def getLabel():
    return excelDF.iloc[currentIndex]["parc_type2019"]

def getIndex():
    return currentIndex

def getTotalRecords():
    return len(excelDF.index)

def incrementIndex():
    global currentIndex
    if (currentIndex < getTotalRecords() - 1):
        currentIndex += 1

def decrementIndex():
    global currentIndex
    if (currentIndex > 0):
        currentIndex -= 1

def setLabel(newLabel): # the new label (can be same as old label)
    currentEntry["Human Checked Label"] = newLabel

def markUnfound(): # mark entry if a streetview image was not found
    currentEntry["Image Not Found"] = "TRUE"

def markObscured(): # mark entry if the streetview was found, but the object of interest obscured or blurred.
    currentEntry["Image Obscured"] = "TRUE"

def addEntryToDataFrame():
    global currentEntry

    currentEntry["Index"] = df.index[currentIndex]
    currentEntry["Address"] = getAddress()
    currentEntry["2019 Label"] = getLabel()
    currentEntry["Human Check Time"] = str(datetime.now())

    currentEntry = {"Index": None, "Address": None, "2019 Label": None, "Human Checked Label": None, "Human Check Time": None, "Image Not Found": "FALSE", "Image Obscured": "FALSE"}



def saveToGoogleSheet(): # TODO send a batch update to the Google Sheet
    pass