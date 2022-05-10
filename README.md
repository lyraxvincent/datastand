# datastand

-----------
![package logo](images/logo.jpg)
Why datastand? __Data + Understand__  
A python package to help Data Scientists, Machine Learning Engineers and Analysts better understand data. Gives quick insights about a given dataset.  


------------------

# Installation
Run the following command on the terminal to install the package:
```python
pip install datastand
```
### Usage :
Code:
```python
from datastand import datastand
import pandas as pd

df = pd.read_csv("path/to/target/dataframe")

datastand(df)

```
Output:
```python

General stats:
==================
Shape of DataFrame: (1202, 13)
Number of unique data types : {dtype('int64'), dtype('O')}
Number of numerical columns: 2
Number of non-numerical columns: 11


Missing data:
=======================
DataFrame contains 2670 missing values (17.09%) as follows column-wise:
-----------------------------------------------------------------------
Gender                 41
Car_Category          372
Subject_Car_Colour    697
Subject_Car_Make      248
LGA_Name              656
State                 656
dtype: int64
-----------------------------------------------------------------------

Do you wish to long-list missing data statistics?(y/n): y
.
.
.
```
Code:
```python
# This function is already available in the DataStand class and also available separately
# Here we're running it separately 
from datastand import plot_missing

plot_missing(df)

```
Output:

![missing data heatmap](images/missing_data_heatmap.png)

Code:
```python
from datastand import impute_missing

impute_missing(df)

```
Output:
```python
Imputing missing data...
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 80/80 [00:02<00:00, 30.52it/s]
Imputation complete.
```
## Author/Maintainer
**Vincent N.**
[[LinkedIn]](https://www.linkedin.com/in/vincent-njonge-528070178)  [[Twitter]](https://twitter.com/lyraxvincent)
