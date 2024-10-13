# librairies
import pandas as pd

# data
df = pd.read_csv("./data/raw/mock_data.csv", delimiter=",", header="infer")

# change some data types
df["positionNumber"] = df["positionNumber"].astype("category")
df["reportsToPositionNumber"] = df["reportsToPositionNumber"].astype("category")

df.info()
print(df.head())
