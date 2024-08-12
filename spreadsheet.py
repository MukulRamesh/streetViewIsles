import pandas as pd
import numpy as np

print("Reading spreadsheet data (this may take a few seconds...)")
df = pd.read_excel("COMPARISONS TRENTON_MASTER.xlsx")[["address", "parc_type2019"]]
df = df.replace(to_replace=' ', value=np.nan).replace(to_replace='CANAL', value=np.nan).dropna() # remove all entries whose address fields are empty, or "CANAL"
df = df.drop_duplicates(subset=["address"]) # we only care about unique address

# index = df.index[0] #gets the row number of the first entry that of the data frame (corresponds to the excel row number)

currentIndex = 0

def getAddress():
    return df.iloc[currentIndex]["address"]

def getLabel():
    return df.iloc[currentIndex]["parc_type2019"]

def incrementIndex():
    global currentIndex
    currentIndex += 1

def decrementIndex():
    global currentIndex
    currentIndex -= 1

def setLabel(): # TODO either as confirmed, or as the new label
    pass

def markUnfound(): # TODO mark entry if a streetview image was not found
    pass