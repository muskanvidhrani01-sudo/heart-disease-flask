import pandas as pd
import numpy as np

mydata={
    "HDFC":{"Qtr1":20000,"Qtr2":24000,"Qtr3":300000},
    "SBI":{"Qtr1":17000,"Qtr2":20000,"Qtr3":220000},
    "Kotak":{"Qtr1":15000,"Qtr2":24000,"Qtr3":280000}}
df=pd.DataFrame(mydata)
print(df)
df.to_csv("Bank.csv")

df=pd.read_csv("heart.csv")
print(df)
print(df["age"].max())
print(df["age"].min())
print(df["age"].count())
print(df["age"].sum())
print(df["age"].mean())
print(df["age"].median())
print(df["age"].mode())
print(df["age"].quantile([0.25,0.5,0.75]))
print(df["age"].var())
print(df["age"].std())