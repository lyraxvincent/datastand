# Necessary libraries
##
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import random
from tqdm import tqdm

class datastand:
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

    def stats(self=pd.DataFrame()):

        print("General stats:\n______________")
        print(f"Size of DataFrame: {self.size}")
        print(f"Shape of DataFrame: {self.shape}")
        print(f"Number of unique data types : {set(self.dtypes)}")
        print(f"Number of numerical columns: {len(self.select_dtypes(np.number).columns)}")
        print(f"Number of non-numerical columns: {len(self.select_dtypes('object').columns)}")

        print(f"\nHead of DataFrame:")
        print(f"__________________\n{self.head()}")
        print(f"\nTail of DataFrame:")
        print(f"__________________\n{self.tail()}")

    # Missing data statistics

    def report_missing(self=pd.DataFrame()):

        if self.isnull().values.any() == True:
            print(f"\nDataFrame contains {self.isnull().values.sum()} missing values("
                  f"{self.isnull().values.sum() / self.size *100 :.2f}%) as follows column-wise:")
            print("-----------------------------------------------------------------------")
            print(self.isnull().sum())  # Prints every column with corresponding number of missing values
            print("-----------------------------------------------------------------------")

            # Long listing missing data statistics (for every column)
            choice = input("\nDo you wish to long-list missing data statistics?(y/n): ").upper()
            print("\n")

            if choice == 'Y':
                for col in self.select_dtypes(np.number):     # Select only numerical columns

                    if self[str(col)].isnull().any() == True:
                        print(f"Column: \n\t{col}")
                        print("\nMissing data points {} out of total {}.".format(self[str(col)].isnull().sum(),
                                                                                 len(self[str(col)])))

                        # Show max, min, mean, std values of the column
                        # Helps user to choose an imputation strategy
                        print("Max value: {} Min value: {} \nMean: {} Std: {} ".format(self[str(col)].max(),
                                                                                       self[str(col)].min(),
                                                                                       np.mean(self[str(col)]),
                                                                                       np.std(self[str(col)])))
                        print("_________________________________________________________________")
                    else:
                        pass

            elif choice == 'N':
                pass

            # Further visualizing missing data
            plot_choice = input("\nYou can visualize missing data using seaborn's heatmap automatically right away... \
                                \nor you can call the method 'datastand.plot_missing(df)' later. Visualize now?(y/n): "
                                ).upper()

            if plot_choice == 'Y':
                plt.figure(figsize=(16, 10))
                sns.heatmap(self.isnull(), cbar=False, yticklabels=False)
                plt.title("Missing Data Heatmap (Cream/Grey parts show missing data)")
                plt.tight_layout()
                plt.show()

            elif plot_choice == 'N':
                pass

        else:
            print("\nDataFrame has no missing values.")


    def plot_missing(self=pd.DataFrame()):
        if self.isnull().values.any() == True:    # Plot only if there are missing values
            plt.figure(figsize=(16, 10))
            sns.heatmap(self.isnull(), cbar=False, yticklabels=False, )
            plt.title("Missing Data Heatmap (Cream/Grey parts show missing data)")
            plt.tight_layout()
            plt.show()
        else:
            pass

    # Imputation of missing data

    def impute_missing(self=pd.DataFrame()):
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
        if self.isnull().values.any() == True:
            print("Imputing missing data...")

            for col in tqdm(self.columns):

                # If column has missing values and they are less than half of the total
                if self[str(col)].isnull().any() == True and self[str(col)].isnull().values.sum() < len(self[str(col)]) / 2:

                    # Values following distribution of the column(trend of data in the column)
                    values = np.arange(self[str(col)].min(), self[str(col)].max(), np.std(self[str(col)]))

                    # Iterate through column values
                    for i in range(len(self[str(col)])):
                        if np.isnan(self.loc[i, str(col)]):  # check if value is nan; Returns True/ False

                            self.loc[i, str(col)] = random.choice(values)  # pick a random value from values
                        else:
                            pass
                else:
                    pass
            print("Imputation complete.")
        else:
            print("DataFrame has no missing data hence no values to be imputed.")
