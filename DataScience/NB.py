import pandas as pd
import pickle 
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


df=pd.read_csv("heart.csv")
x=df[["age","sex","trestbps","chol"]]
y=df["target"]
trainx,testx,trainy,testy=train_test_split(x,y,random_state=42,test_size=0.2)
model=GaussianNB()
model.fit(trainx,trainy)
with open("nb.pkl","wb") as f:
    pickle.dump(model,f)
