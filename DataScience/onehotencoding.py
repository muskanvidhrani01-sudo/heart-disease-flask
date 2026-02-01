import pandas as pd
df=pd.read_csv("heart1.csv")
df_new=pd.get_dummies(
    df,
    columns=["ST_Slope"]
)
print(df.head(5))
print(df_new.head(5))
df_new.to_csv("heart1_new.csv")