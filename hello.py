import pandas as pd
import numpy as np

df = pd.read_csv("dataset1.csv")

#TASK 1
print("First 5 Records:")
print(df.head())
print("\nLast 5 Records:")
print(df.tail())
print("\nDataset Shape (Rows, Columns):")
print(df.shape)
print("\nTotal Rows:", df.shape[0])
print("Total Columns:", df.shape[1])

#TASK 2

print("\nColumn Names:")
print(df.columns)
print("\nData Types:")
print(df.dtypes)
print("\nDataset Information:")
df.info()
print("\nDescriptive Statistics:")
print(df.describe())
print("\nAverage Salary:")
print(df["salary"].mean())
print("\nStandard Deviation of Numerical Columns:")
print(df.std(numeric_only=True))
print("\nFeature with Highest Standard Deviation:")
print(df.std(numeric_only=True).idxmax())

#TASK 3

print("\nMissing Values:")
print(df.isnull().sum())
print("\nPercentage of Missing Values:")
print((df.isnull().sum() / len(df)) * 100)
print("\nColumn with Maximum Missing Values:")
print(df.isnull().sum().idxmax())
print("\nNumber of Duplicate Records:")
print(df.duplicated().sum())
print("\nDataset Size Before Cleaning:", len(df))
df = df.drop_duplicates()
print("Dataset Size After Cleaning:", len(df))
