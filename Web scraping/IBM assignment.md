```python
!pip install yfinance==0.1.67
#!pip install pandas==1.3.3
```
Collecting yfinance==0.1.67
  Downloading yfinance-0.1.67-py2.py3-none-any.whl (25 kB)
Requirement already satisfied: pandas>=0.24 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from yfinance==0.1.67) (1.3.5)
Requirement already satisfied: requests>=2.20 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from yfinance==0.1.67) (2.27.1)
Requirement already satisfied: lxml>=4.5.1 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from yfinance==0.1.67) (4.8.0)
Collecting multitasking>=0.0.7
  Downloading multitasking-0.0.10.tar.gz (8.2 kB)
  Preparing metadata (setup.py) ... done
Requirement already satisfied: numpy>=1.15 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from yfinance==0.1.67) (1.21.6)
Requirement already satisfied: python-dateutil>=2.7.3 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from pandas>=0.24->yfinance==0.1.67) (2.8.2)
Requirement already satisfied: pytz>=2017.3 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from pandas>=0.24->yfinance==0.1.67) (2022.1)
Requirement already satisfied: certifi>=2017.4.17 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from requests>=2.20->yfinance==0.1.67) (2021.10.8)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from requests>=2.20->yfinance==0.1.67) (1.26.9)
Requirement already satisfied: idna<4,>=2.5 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from requests>=2.20->yfinance==0.1.67) (3.3)
Requirement already satisfied: charset-normalizer~=2.0.0 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from requests>=2.20->yfinance==0.1.67) (2.0.12)
Requirement already satisfied: six>=1.5 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from python-dateutil>=2.7.3->pandas>=0.24->yfinance==0.1.67) (1.16.0)
Building wheels for collected packages: multitasking
  Building wheel for multitasking (setup.py) ... done
  Created wheel for multitasking: filename=multitasking-0.0.10-py3-none-any.whl size=8500 sha256=f9741ad458b820b6f20f395a9f3c45943af7c15c1c5a602bfffb915824ae3bbe
  Stored in directory: /home/jupyterlab/.cache/pip/wheels/34/ba/79/c0260c6f1a03f420ec7673eff9981778f293b9107974679e36
Successfully built multitasking
Installing collected packages: multitasking, yfinance
Successfully installed multitasking-0.0.10 yfinance-0.1.67

```python
import yfinance as yf
import pandas as pd
```

```python
apple = yf.Ticker("AAPL")
```

```python
apple_info=apple.info
apple_info
```
{'zip': '95014',
 'sector': 'Technology',
 'fullTimeEmployees': 100000,
 'longBusinessSummary': 'Apple Inc. designs, manufactures, and markets smartphones, personal computers, tablets, wearables, and accessories worldwide. It also sells various related services. In addition, the company offers iPhone, a line of smartphones; Mac, a line of personal computers; iPad, a line of multi-purpose tablets; AirPods Max, an over-ear wireless headphone; and wearables, home, and accessories comprising AirPods, Apple TV, Apple Watch, Beats products, HomePod, and iPod touch. Further, it provides AppleCare support services; cloud services store services; and operates various platforms, including the App Store that allow customers to discover and download applications and digital content, such as books, music, video, games, and podcasts. Additionally, the company offers various services, such as Apple Arcade, a game subscription service; Apple Music, which offers users a curated listening experience with on-demand radio stations; Apple News+, a subscription news and magazine service; Apple TV+, which offers exclusive original content; Apple Card, a co-branded credit card; and Apple Pay, a cashless payment service, as well as licenses its intellectual property. The company serves consumers, and small and mid-sized businesses; and the education, enterprise, and government markets. It distributes third-party applications for its products through the App Store. The company also sells its products through its retail and online stores, and direct sales force; and third-party cellular network carriers, wholesalers, retailers, and resellers. Apple Inc. was incorporated in 1977 and is headquartered in Cupertino, California.',
 'city': 'Cupertino',
 'phone': '408 996 1010',
 'state': 'CA',
 'country': 'United States',
 'companyOfficers': [],
 'website': 'https://www.apple.com',
 'maxAge': 1,
 'address1': 'One Apple Park Way',
 'industry': 'Consumer Electronics',
 'ebitdaMargins': 0.33890998,
 'profitMargins': 0.26579002,
 'grossMargins': 0.43019,
 'operatingCashflow': 112241000448,
 'revenueGrowth': 0.112,
 'operatingMargins': 0.309,
 'ebitda': 128217997312,
 'targetLowPrice': 157,
 'recommendationKey': 'buy',
 'grossProfits': 152836000000,
 'freeCashflow': 80153247744,
 'targetMedianPrice': 191,
 'currentPrice': 161.11,
 'earningsGrowth': 0.25,
 'currentRatio': 1.038,
 'returnOnAssets': 0.19875,
 'numberOfAnalystOpinions': 43,
 'targetMeanPrice': 190.2,
 'debtToEquity': 170.714,
 'returnOnEquity': 1.45567,
 'targetHighPrice': 215,
 'totalCash': 63913000960,
 'totalDebt': 122797998080,
 'totalRevenue': 378323009536,
 'totalCashPerShare': 3.916,
 'financialCurrency': 'USD',
 'revenuePerShare': 22.838,
 'quickRatio': 0.875,
 'recommendationMean': 1.9,
 'exchange': 'NMS',
 'shortName': 'Apple Inc.',
 'longName': 'Apple Inc.',
 'exchangeTimezoneName': 'America/New_York',
 'exchangeTimezoneShortName': 'EDT',
 'isEsgPopulated': False,
 'gmtOffSetMilliseconds': '-14400000',
 'quoteType': 'EQUITY',
 'symbol': 'AAPL',
 'messageBoardId': 'finmb_24937',
 'market': 'us_market',
 'annualHoldingsTurnover': None,
 'enterpriseToRevenue': 6.956,
 'beta3Year': None,
 'enterpriseToEbitda': 20.525,
 '52WeekChange': 0.24496484,
 'morningStarRiskRating': None,
 'forwardEps': 6.53,
 'revenueQuarterlyGrowth': None,
 'sharesOutstanding': 16319399936,
 'fundInceptionDate': None,
 'annualReportExpenseRatio': None,
 'totalAssets': None,
 'bookValue': 4.402,
 'sharesShort': 103292182,
 'sharesPercentSharesOut': 0.0063,
 'fundFamily': None,
 'lastFiscalYearEnd': 1632528000,
 'heldPercentInstitutions': 0.59268004,
 'netIncomeToCommon': 100554997760,
 'trailingEps': 6.015,
 'lastDividendValue': 0.22,
 'SandP52WeekChange': 0.0018931627,
 'priceToBook': 36.599274,
 'heldPercentInsiders': 0.00071000005,
 'nextFiscalYearEnd': 1695600000,
 'yield': None,
 'mostRecentQuarter': 1640390400,
 'shortRatio': 1.18,
 'sharesShortPreviousMonthDate': 1647302400,
 'floatShares': 16302468781,
 'beta': 1.187745,
 'enterpriseValue': 2631645003776,
 'priceHint': 2,
 'threeYearAverageReturn': None,
 'lastSplitDate': 1598832000,
 'lastSplitFactor': '4:1',
 'legalType': None,
 'lastDividendDate': 1643932800,
 'morningStarOverallRating': None,
 'earningsQuarterlyGrowth': 0.204,
 'priceToSalesTrailing12Months': 6.949666,
 'dateShortInterest': 1649894400,
 'pegRatio': 2.63,
 'ytdReturn': None,
 'forwardPE': 24.672281,
 'lastCapGain': None,
 'shortPercentOfFloat': 0.0063,
 'sharesShortPriorMonth': 111286790,
 'impliedSharesOutstanding': 0,
 'category': None,
 'fiveYearAverageReturn': None,
 'previousClose': 159.48,
 'regularMarketOpen': 159.67,
 'twoHundredDayAverage': 159.4393,
 'trailingAnnualDividendYield': 0.005423878,
 'payoutRatio': 0.14310001,
 'volume24Hr': None,
 'regularMarketDayHigh': 161.23,
 'navPrice': None,
 'averageDailyVolume10Day': 99354490,
 'regularMarketPreviousClose': 159.48,
 'fiftyDayAverage': 165.462,
 'trailingAnnualDividendRate': 0.865,
 'open': 159.67,
 'toCurrency': None,
 'averageVolume10days': 99354490,
 'expireDate': None,
 'algorithm': None,
 'dividendRate': 0.92,
 'exDividendDate': 1651795200,
 'circulatingSupply': None,
 'startDate': None,
 'regularMarketDayLow': 159.48,
 'currency': 'USD',
 'trailingPE': 26.784706,
 'regularMarketVolume': 11107999,
 'lastMarket': None,
 'maxSupply': None,
 'openInterest': None,
 'marketCap': 2629218598912,
 'volumeAllCurrencies': None,
 'strikePrice': None,
 'averageVolume': 89411750,
 'dayLow': 159.48,
 'ask': 160.27,
 'askSize': 1200,
 'volume': 11107999,
 'fiftyTwoWeekHigh': 182.94,
 'fromCurrency': None,
 'fiveYearAvgDividendYield': 1.1,
 'fiftyTwoWeekLow': 122.25,
 'bid': 160.28,
 'tradeable': False,
 'dividendYield': 0.0058,
 'bidSize': 1800,
 'dayHigh': 161.23,
 'regularMarketPrice': 161.11,
 'preMarketPrice': 159.66,
 'logo_url': 'https://logo.clearbit.com/apple.com'}
 
 ```python
 apple_share_price_data = apple.history(period="max")
 ```
 
 ```python
apple_share_price_data.head()
 ```
 	Open	High	Low	Close	Volume	Dividends	Stock Splits
Date							
1980-12-12	0.100326	0.100762	0.100326	0.100326	469033600	0.0	0.0
1980-12-15	0.095528	0.095528	0.095092	0.095092	175884800	0.0	0.0
1980-12-16	0.088548	0.088548	0.088112	0.088112	105728000	0.0	0.0
1980-12-17	0.090293	0.090729	0.090293	0.090293	86441600	0.0	0.0
1980-12-18	0.092911	0.093347	0.092911	0.092911	73449600	0.0	0.0

 ```python
apple_share_price_data.reset_index(inplace=True)
 ```
 
 
 ```python
apple_share_price_data.plot(x="Date", y="Open")
 ```
 <AxesSubplot:xlabel='Date'>

