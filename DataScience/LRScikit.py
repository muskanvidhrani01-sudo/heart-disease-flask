import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df=pd.read_csv("heart.csv")
x= df[['age']]
y=df['chol']

trainx,testx,trainy,testy=train_test_split(x,y,test_size=0.2, random_state=42)

model=LinearRegression()
model.fit(trainx,trainy)
#predy=model.predict([[50]])
predy=model.predict(testx)
print(predy)

err=mean_squared_error(testy,predy)
print(err)