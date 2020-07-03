from dataStand import datastand
import pandas as pd

train = pd.read_csv('train.csv')

# General statistics
datastand.stats(train)

# Report of missing data
datastand.report_missing(train)

# Plot heatmap to visualize missing data
datastand.plot_missing(train)

# Impute missing data
datastand.impute_missing(train)
