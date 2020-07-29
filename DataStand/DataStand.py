# Necessary libraries
##
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import random
from tqdm import tqdm

class DataStand:
    """
        A helper class for giving insights about data in the following aspects:
            - size of dataframe
            - shape of dataframe
            - number of numerical and non-numerical columns
            - show head and tail of dataframe
            - show statistics of missing values, including visualizing the missing data
            - suggest a methodology/ strategy to fill missing values
            - filling missing values if the user chooses to
    """

    def __init__(self, df):
        self.df = df

        # General statistics

        print("General stats:\n==================")
        print(f"Size of DataFrame: {df.size}")
        print(f"Shape of DataFrame: {df.shape}")
        print(f"Number of unique data types : {set(df.dtypes)}")
        print(f"Number of numerical columns: {len(df.select_dtypes(np.number).columns)}")
        print(f"Number of non-numerical columns: {len(df.select_dtypes('object').columns)}")

        print(f"\nHead of DataFrame:")
        print(f"__________________\n{df.head()}")
        print(f"\nTail of DataFrame:")
        print(f"__________________\n{df.tail()}")

        # Missing data statistics

        if df.isnull().values.any() == True:
            print("\nMissing data:\n=======================")
            print(f"DataFrame contains {df.isnull().values.sum()} missing values("
                  f"{df.isnull().values.sum() / df.size *100 :.2f}%) as follows column-wise:")
            print("-----------------------------------------------------------------------")
            print(df.isnull().sum())  # Prints every column with corresponding number of missing values
            print("-----------------------------------------------------------------------")

            # Long listing missing data statistics (for every column)
            choice = input("\nDo you wish to long-list missing data statistics?(y/n): ").upper()
            print("\n")

            if choice == 'Y':
                for col in df.select_dtypes(np.number):     # Select only numerical columns

                    if df[str(col)].isnull().any() == True:
                        print(f"Column: \n\t{col}")
                        print("\nMissing data points {} out of total {}.".format(df[str(col)].isnull().sum(),
                                                                                 len(df[str(col)])))

                        # Show max, min, mean, std values of the column
                        # Helps user to choose an imputation strategy
                        print("Max value: {} Min value: {} \nMean: {} Std: {} ".format(df[str(col)].max(),
                                                                                       df[str(col)].min(),
                                                                                       np.mean(df[str(col)]),
                                                                                       np.std(df[str(col)])))
                        print("_________________________________________________________________")
                    else:
                        pass

            elif choice == 'N':
                pass

            # Further visualizing missing data
            plot_choice = input("\nYou can visualize missing data automatically right away or you can use the " \
                                "\nfunction plot_missing() after importing it from DataStand. Visualize now?(y/n): ").upper()

            if plot_choice == 'Y':
                plt.figure(figsize=(16, 10))
                sns.heatmap(df.isnull(), cbar=False, yticklabels=False)
                plt.title("Missing Data Heatmap (Cream/Grey parts show missing data)")
                plt.tight_layout()
                plt.show()

            elif plot_choice == 'N':
                pass

        else:
            print("\nDataFrame has no missing values.")

# plot missing data heatmap

def plot_missing(df):
    if df.isnull().values.any() == True:    # Plot only if there are missing values
        plt.figure(figsize=(16, 10))
        sns.heatmap(df.isnull(), cbar=False, yticklabels=False, )
        plt.title("Missing Data Heatmap (Cream/Grey parts show missing data)")
        plt.tight_layout()
        plt.show()
    else:
        pass

# Imputation of missing data

def impute_missing(df):
    """
        Iterate through dataframe columns; Fill missing value with a random value chosen from:
            np.arange(min value in the column, max_value, standard deviation of the column)
        This way we ensure we maintain the trend of data in that particular column
    NOTE:
        This method only applies for numerical columns
        We impute only columns with less than half missing data points of the total length of the column
    TODO:
        Add functionality for imputing categorical data
    """
    if df.isnull().values.any() == True:
        print("\nImputing missing data...")

        for col in tqdm(df.columns):

            # If column has missing values and they are less than half of the total
            if df[str(col)].isnull().any() == True and df[str(col)].isnull().values.sum() < len(df[str(col)]) / 2:

                # Values following distribution of the column(trend of data in the column)
                values = np.arange(df[str(col)].min(), df[str(col)].max(), np.std(df[str(col)]))

                # Iterate through column values
                for i in range(len(df[str(col)])):
                    if np.isnan(df.loc[i, str(col)]):  # check if value is nan; Returns True/ False

                        df.loc[i, str(col)] = random.choice(values)  # pick a random value from values
                    else:
                        pass
            else:
                pass
        print("Imputation complete.")
        return df
    else:
        print("DataFrame has no missing data hence no values to be imputed.")