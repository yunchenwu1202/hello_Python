```python
import requests
from bs4 import BeautifulSoup

page = requests.get("http://EnterWebsiteURL...").text
# Creates a BeautifulSoup Object
soup = BeautifulSoup(page, "html.parser")

# Pulls all instances of <a> tag 
artists = soup.find_all('a')

# Clears data of all tags
for artist in artists:
  names = artist.contents[0]
  fullLink = artist.get('href')
  print(name)
  print(fullLink)
  ```
# Reading CSV files

```python
import pandas as pd
file = 'FileExample.csv'
df = pd.read_csv(file)
```

# Adding Headers 
```python 
df.columns = ['Name','Phone Number','Birthday']
```

## Reading JSON files

```pyhton
import json
with open('filesample.json','r') as openfile:
  json_object = json.load(openfile)
 print(json_object)
 ```
 
 ## Reading XML files
 ```python 
 import pandas as pd
 import xml.etree.ElementTree as etree
 tree = etree.parse("fileExample.xml")
 root = tree.getroot()
columns = ['Name','Phone Number','Birthday']
df = pd.DataFrame(columns = columns)

for node in root:
name = node.find("name").text
phonenumber = node.find("phonenumber").text
birthday = node.find("birthday").text

df = df.append(pd.Series([name, phonenumber, birthday], index = columns)... . ., ignore_index = True)
```
