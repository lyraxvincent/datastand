import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random


class datastand:
    """

    """

    def __init__(self, df):
        self.df = df

    # General statistics

    def stats(df):

        print("General stats:\n______________")
        print(f"Size of DataFrame: {df.size}")
        print(f"Shape of DataFrame: {df.shape} :: {len(df)} rows and {len(df.columns)} columns")
        print(f"Number of numerical columns: {len(df.select_dtypes(np.number).columns)}")
        print(f"Number of non-numerical(string) columns: {len(df.select_dtypes('object').columns)}")
        print(f"Number of datetime columns: {len(df.select_dtypes('datetime').columns)}")
        print(f"Number of categorical columns: {len(df.select_dtypes('category').columns)}")

        print(f"\nHead of DataFrame:")
        print(f"__________________\n{df.head()}")
        print(f"\nTail of DataFrame:")
        print(f"__________________\n{df.tail()}")

    # Missing data statistics

    def report_missing(df):

        if df.isnull().values.any() == True:
            print(f"\nDataFrame contains {df.isnull().values.sum()} missing values("
                  f"{df.isnull().values.sum()/df.size *100 :.2f}%) as follows column-wise:")
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
            plot_choice = input("\nYou can visualize missing data using seaborn's heatmap automatically right away... \
                                \nor you can call the method 'datastand.plot_missing(df)' later. Visualize now?(y/n): "
                                ).upper()

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


    def plot_missing(df):
        plt.figure(figsize=(16, 10))
        sns.heatmap(df.isnull(), cbar=False, yticklabels=False, )
        plt.title("Missing Data Heatmap (Cream/Grey parts show missing data)")
        plt.tight_layout()
        plt.show()

    # Imputation of missing data

    def impute_missing(df):
        """
            Iterate through dataframe columns; Fill missing value with a random value chosen from:
                np.arange(min value in the column, max_value, standard deviation of the column)
            This way we ensure we maintain the trend of data in that particular column
        NOTE:
            This method only applies for numerical columns
            We impute only columns with less than half missing data points of the total length of the column
        """

        for col in df.columns:

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
                print("DataFrame has no missing data hence no values to be imputed.")
