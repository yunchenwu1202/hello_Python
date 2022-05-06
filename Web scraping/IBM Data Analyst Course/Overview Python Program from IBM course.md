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
## Reading CSV files

```python
import pandas as pd
file = 'FileExample.csv'
df = pd.read_csv(file)
```

## Adding Headers 
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

## Scrape Data from HTML tables into Dataframe using Beautifulsoup and Pandas
```python
import pandas as pd

# get the contents of the webpage in text format and store in a variable called data
data  = requests.get(url).text

soup = BeautifulSoup(data,"html.parser")

#find all html tables in the web page
tables = soup.find_all('table') # in html table is represented by the tag <table>

# we can see how many tables were found by checking the length of the tables list
len(tables)

for index,table in enumerate(tables):
    if ("10 most densely populated countries" in str(table)):
        table_index = index
print(table_index)

print(tables[table_index].prettify())

population_data = pd.DataFrame(columns=["Rank", "Country", "Population", "Area", "Density"])

for row in tables[table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col != []):
        rank = col[0].text
        country = col[1].text
        population = col[2].text.strip()
        area = col[3].text.strip()
        density = col[4].text.strip()
        population_data = population_data.append({"Rank":rank, "Country":country, "Population":population, "Area":area, "Density":density}, ignore_index=True)

population_data

```

## Scrape data from HTML tables into a Dataframe using Beautifulsoup and read_HTML
```python
pd.read_html(str(tables[5]), flavor='bs4')

population_data_read_html = pd.read_html(str(tables[5]), flavor='bs4')[0]

population_data_read_html
```

## Scrape data from HTML tables into a Dataframe using read_html
```python
dataframe_list = pd.read_html(url, flavor='bs4')
len(dataframe_list)
dataframe_list[5]
pd.read_html(url, match="10 most densely populated countries", flavor='bs4')[0]
```




