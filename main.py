import urllib.parse

safeLoc = urllib.parse.quote_plus("18 CLARK ST Trenton")


size = "6000x3000"
location = safeLoc
key = "AIzaSyC5hgQGagiwSuiLlRghHxDisI__P11jGbk"

url = f"https://maps.googleapis.com/maps/api/streetview?size={size}&location={location}&key={key}"

print(url)