import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df =pd.read_csv("heart.csv")
x= df[["age","chol"]]
y=df["target"]

trainx,testx,trainy,testy=train_test_split(x,y,test_size=0.2, random_state=42)

model=LogisticRegression()
model.fit(trainx,trainy)
print(model.intercept_)
print(model.coef_)

#ypred=model.predict([[50,200]])
ypred=model.predict(testx)
print(ypred)

#prob=model.predict_proba([[50,200]])
#print(prob)

acc=accuracy_score(ypred,testy)
print(acc)