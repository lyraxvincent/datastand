from DataStand import DataStand
from DataStand import impute_missing
from DataStand import plot_missing
import pandas as pd

train = pd.read_csv('train.csv')

DataStand(train)
plot_missing(train)
impute_missing(train)

