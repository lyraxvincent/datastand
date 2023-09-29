"""datastand module"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import random
from typing import Literal, Union


class datastand:
    """
        A helper class for giving insights about data in the following aspects:
            - size and shape of dataframe
            - number of numerical and non-numerical columns
            - small overview of dataframe
            - show statistics of missing values, including visualizing the missing data
            - suggest a methodology/ strategy to fill missing values
            - filling missing values with the chosen method

        :param df: Pandas dataframe
        :param long_list_missing: whether to long list missing data statistics. Defaults to False.
        :param plot_missing: whether to plot missing data heatmap. Defaults to True.
    """

    def __init__(
        self,
        df: pd.DataFrame,
        long_list_missing: bool = False,
        plot_missing: bool = True
    ):

        self.df = df
        self.long_list_missing = long_list_missing
        self.plot_missing = plot_missing

        # General statistics
        print("General stats:\n==================")
        print(f"Shape of DataFrame: {self.df.shape}")
        print(f"Number of unique data types : {set(self.df.dtypes)}")
        print(f"Number of numerical columns: {len(self.df.select_dtypes(np.number).columns)}")
        print(f"Number of non-numerical columns: {len(self.df.select_dtypes('object').columns)}")

        # Missing data statistics
        if self.df.isnull().values.any():
            print("\n\nMissing data:\n=======================")
            print(f"DataFrame contains {self.df.isnull().values.sum()} missing values ("
                  f"{self.df.isnull().values.sum() / self.df.size *100 :.2f}%) as follows column-wise:")
            print("-----------------------------------------------------------------------")
            print(self.df[self.df.columns[self.df.isnull().any()]].isnull().sum())
            print("-----------------------------------------------------------------------")

            # Long listing missing data statistics (for every column)
            if self.long_list_missing:

                for col in self.df.columns:

                    if self.df[str(col)].isnull().any():
                        print(f"Column: \n\t{col}\n\t_______________")
                        print(f"\nMissing data points {self.df[str(col)].isnull().sum()} out of total "
                              f"{len(self.df[str(col)])}; ({(self.df[str(col)].isnull().values.sum() / len(self.df) * 100):.2f}%)")

                        # Show max, min, mean, std values of the column if numerical
                        # Helps user to choose an imputation strategy
                        if self.df[col].dtype == int or self.df[col].dtype == float:
                            print(f"Max value: {self.df[str(col)].max()} Min value: {self.df[str(col)].min()} \n"
                                  f"Mean: {np.mean(self.df[str(col)])} Std: {np.std(self.df[str(col)])} ")
                            print("_________________________________________________________________")
                        elif self.df[col].dtype == 'O':
                            print(f"Most occurring value: {self.df[col].value_counts().index.to_list()[0]}, count: {self.df[col].value_counts().to_list()[0]}")
                            print("_________________________________________________________________")
                        else:
                            pass

            # Further visualizing missing data
            if self.plot_missing:
                plt.figure(figsize=(16, 10))
                sns.heatmap(self.df.isnull(), cbar=False, yticklabels=False)
                plt.title("Missing Data Heatmap")
                plt.tight_layout()
                plt.show()

        else:
            print("\nDataFrame has no missing values.")


# plot missing data heatmap
def plot_missing(df: pd.DataFrame) -> None:
    """
    Plot mising data heatmap

    Args:
        df (pd.DataFrame): Pandas dataframe
    """

    if df.isnull().values.any():
        plt.figure(figsize=(16, 10))
        sns.heatmap(df.isnull(), cbar=False, yticklabels=False)
        plt.title("Missing Data Heatmap")
        plt.tight_layout()
        plt.show()
    else:
        print("Dataframe has no missing values.")


# Imputation of missing data
def impute_missing(
    df: pd.DataFrame,
    inplace: bool = False,
    method: Literal["constant", "random"] = "constant"
) -> Union[pd.DataFrame, None]:
    """

    :param df: Pandas DataFrame
    :param inplace: Hold changes to original DataFrame or not
    :param method: How to impute categorical columns
                    'constant' - fill with a constant value 'NULL'
                    'random' - pick a value from existing categories and fill at random

    :return: Imputed DataFrame

    NOTES:
    ------
        Iterate through dataframe columns;
        For numerical columns: fill missing value with a random value chosen from:
            np.arange(min value in the column, max_value, standard deviation of the column)
        For categorical columns: fill with a constant value (method 1)
                                 fill with a value chosen from the already existing categories at random
        This way we ensure we maintain the trend of data in that particular column
        We impute only columns with less than half missing data points of the total length of the column

    """

    if inplace:
        df_ = df
    else:
        df_ = df[:]  # make a copy explicitly to avoid imputing inplace


    if df_.isnull().values.any():

        print("\nImputing missing data...")

        # Impute numerical columns
        for col in df_.select_dtypes(np.number).columns:
            # If column has missing values and they are less than half of the total
            if df_[str(col)].isnull().any() and df_[str(col)].isnull().values.sum() < len(df_[str(col)]) / 2:
                # Values following distribution of the column(trend of data in the column)
                values = np.arange(df_[str(col)].min(), df_[str(col)].max(), np.std(df_[str(col)]))
                # Iterate through column values
                for i in range(len(df_[str(col)])):
                    if np.isnan(df_.loc[i, str(col)]):  # check if value is nan; Returns True/ False
                        df_.loc[i, str(col)] = random.choice(values)  # pick a random value from values

        # Impute categorical columns
        for col in df_.select_dtypes('O').columns:

            if (df_[col].dtype == 'O') & (df_[col].nunique() < 21): # consider only columns with <=20 unique values
                # method 1 - 'random'
                if method == 'random':
                    values = list(df_[col].unique())
                    if np.nan in values:
                        values.remove(np.nan)

                    for i in range(len(df_[str(col)])):
                        try:
                            if np.isnan(df_.loc[i, str(col)]):
                                df_.loc[i, str(col)] = random.choice(values)
                        except TypeError:
                            pass
                # method 2 - 'constant' == 'NULL'
                elif method == 'constant':
                    for i in range(len(df_[str(col)])):
                        try:
                            if np.isnan(df_.loc[i, str(col)]):
                                df_.loc[i, str(col)] = 'NULL'
                        except TypeError:
                            pass
        print("Imputation complete.")
        return df_

    print("DataFrame has no missing data hence no values to be imputed.")
