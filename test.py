from DataStand import datastand
import pandas as pd

train = pd.read_csv('train.csv')

# General statistics
#datastand.stats(df = train)

# Report of missing data
datastand.report_missing(df = train)

# Plot heatmap to visualize missing data
#datastand.plot_missing(df = train)