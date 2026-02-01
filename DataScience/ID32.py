import pandas as pd
import pickle
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
df=pd.read_csv("heart.csv")
x=df[["age","sex","trestbps","chol"]]
y=df["target"]
trainx,testx,trainy,testy=train_test_split(x,y,random_state=42,test_size=0.2)
model=DecisionTreeClassifier(criterion="entropy",max_depth=3)
model.fit(trainx,trainy)
plt.figure()
plt.scatter(df["age"],df["target"])
plt.savefig("templates/static/heart.png")
plt.close()
with open("ID32.pkl","wb") as f:
    pickle.dump(model,f)