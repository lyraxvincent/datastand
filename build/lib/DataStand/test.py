from DataStand import DataStand
from DataStand import impute_missing
import pandas as pd

train = pd.read_csv('train.csv')

#DataStand(train)
impute_missing(train)

