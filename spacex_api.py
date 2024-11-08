import pandas as pd

url = "http://api.spacexdata.com/v4/launches"

df = pd.read_json(url)

print(df.head())

print(df.comlumns)

print(df.dtypes)