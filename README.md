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
______________
Size of DataFrame: 309200
Shape of DataFrame: (3865, 80)
Number of unique data types : {dtype('int64'), dtype('O'), dtype('float64')}
Number of numerical columns: 79
Number of non-numerical columns: 1


Missing data:
=======================
DataFrame contains 185698 missing values(60.06%) as follows column-wise:
-----------------------------------------------------------------------
galactic year                                                                   0
galaxy                                                                          0
existence expectancy index                                                      1
existence expectancy at birth                                                   1
Gross income per capita                                                        28
                                                                             ... 
Adjusted net savings                                                         2953
Creature Immunodeficiency Disease prevalence, adult (% ages 15-49), total    2924
Private galaxy capital flows (% of GGP)                                      2991
Gender Inequality Index (GII)                                                3021
y                                                                               0
Length: 80, dtype: int64
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
