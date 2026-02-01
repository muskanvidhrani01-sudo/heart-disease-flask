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
age=int(input("Enter Age "))
sex=int(input("Enter 0 or 1 "))
bps=int(input("Enter resting bp "))
chol=int(input("Enter Chol "))
mydf=pd.DataFrame([[age,sex,bps,chol]],columns=["age","sex","trestbps","chol"])
ans=model.predict(mydf)
print(ans[0])
if ans[0]==1:
    print("Heart Disease Detected!!!")
else:
    print("Heart Disease Not Detected!!!")