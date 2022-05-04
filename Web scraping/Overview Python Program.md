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
