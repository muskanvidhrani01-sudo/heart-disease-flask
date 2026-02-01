import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

df=pd.read_csv("heart.csv")
x=df.drop("target",axis=1)
y=df["target"]

trainx,testx,trainy,testy=train_test_split(x,y,test_size=0.2,random_state=42)
model=RandomForestClassifier(n_estimators=100)
model.fit(trainx,trainy)
predy=model.predict(testx)
print(accuracy_score(testy,predy))