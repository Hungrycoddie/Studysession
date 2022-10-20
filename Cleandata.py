import pandas as pd
import numpy as np

Load the data into a pandas DataFrame:

df = pd.read_csv("data.csv")

Drop any rows with missing values:

df.dropna(axis=0, inplace=True)

Drop any columns with missing values:

df.dropna(axis=1, inplace=True)

Drop any duplicate rows:

df.drop_duplicates(inplace=True)

Drop any duplicate columns:

df.drop_duplicates(inplace=True, axis=1)

Convert all data to the correct data type:

df = df.apply(pd.to_numeric, errors='coerce')

Save the cleaned data to a new file:

df.to_csv("cleaned_data.csv", index=False)