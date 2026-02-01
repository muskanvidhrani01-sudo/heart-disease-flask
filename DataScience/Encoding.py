import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

df =pd.read_csv("heart1.csv")
print(df)
le=LabelEncoder()
df["sex_enc"]=le.fit_transform(df["Sex"])
print(df)
print(df.dtypes)

for c in df.columns:
    if df[c].dtype=="object":
        df[c]=le.fit_transform(df[c])

print(df)
print(df.dtypes)