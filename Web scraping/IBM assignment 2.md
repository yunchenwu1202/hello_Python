## Table of Contacnt 
```python
#!pip install pandas==1.3.3
#!pip install requests==2.26.0
!mamba install bs4==4.10.0 -y
!mamba install html5lib==1.1 -y
!pip install lxml==4.6.4
#!pip install plotly==5.3.1

import pandas as pd
import requests
from bs4 import BeautifulSoup
```

## Using Webscraping to Extract Stock Data 

1. Request library to download the webpage. 
```python 
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"

data  = requests.get(url).text
```

2. Parse text into html using beautiful soup. 
```python 
soup = BeautifulSoup(data, 'html5lib')
```

3. Turn the html table into a pandas dataframe.
```python
netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

# First we isolate the body of the table which contains all the information
# Then we loop through each row and find all the column values for each row
for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    # Finally we append the data of each row to the table
    netflix_data = netflix_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)    
 ```
    
 4. Now print out the dataframe.
 ```python
 netflix_data.head()
 ```
 
 5. We can also use the pandas read_html funnction using the url.
 ```python
 read_html_pandas_data = pd.read_html(url)
 ```
 
 6. Convert beautiful soup into a string
 ```python
 read_html_pandas_data = pd.read_html(str(soup))
 ```
 
 7. Due to there's only one table on the page, therefore just take the first table in the list returned.
```python
netflix_dataframe = read_html_pandas_data[0]

netflix_dataframe.head()
```




