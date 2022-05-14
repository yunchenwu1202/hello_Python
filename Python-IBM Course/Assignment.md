## Q1.
```python
df.dtypes
```
## Q2.
```python
df.drop(["id","Unnamed: 0"] , axis = 1, inplace = True)
df.describe()
```
## Q3.
```python
df['floors'].value_counts().to_frame()
```
## Q4.
```python
sns.boxplot(x="waterfront", y="price", data=df)
```
## Q5.
```python
1
sns.regplot(x="sqft_above", y="price", data=df, ci = None)
```
## Q6.
```python
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = df[['sqft_living']]
Y = df['price']
lm = LinearRegression()
lm
lm.fit(X,Y)
lm.score(X, Y)
```
## Q7.
```python
features =["floors", "waterfront","lat" ,"bedrooms" ,"sqft_basement" ,"view" ,"bathrooms","sqft_living15","sqft_above","grade","sqft_living"]     

X = df[features]
Y = df['price']
lm.fit(X,Y)

LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None,
         normalize=False)

lm.score(X,Y)
```
## Q8.
```python
pipe=Pipeline(Input)
pipe

pipe.fit(X,Y)

pipe.score(X,Y)
```
## Q9.
```python
from sklearn.linear_model import Ridge

RigeModel=Ridge(alpha=0.1)
RigeModel.fit(x_train, y_train)
RigeModel.score(x_test, y_test)
```
## Q10.
```python
pr = PolynomialFeatures(degree=2)
x_train_pr = pr.fit_transform(x_train)
x_test_pr = pr.fit_transform(x_test)

RigeModel=Ridge(alpha=0.1)
RigeModel.fit(x_train_pr, y_train)
RigeModel.score(x_test_pr, y_test)
```
