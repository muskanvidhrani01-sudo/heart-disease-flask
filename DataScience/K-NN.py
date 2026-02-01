import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df =pd.read_csv("heart.csv")
x= df[["age","chol"]]
y=df["target"]

trainx,testx,trainy,testy=train_test_split(x,y,test_size=0.2, random_state=42)

model=KNeighborsClassifier(n_neighbors=3)
model.fit(trainx,trainy)

ypred=model.predict(testx)
print(ypred)

acc=accuracy_score(ypred,testy)
print(acc)

print(testy)
print(ypred)
testy_arr=np.array(testy)
tp=0
tn=0

for i in range(len(testy_arr)):
    if testy_arr[i]==1 and ypred[i]==1:
        tp=tp+1
    
    elif testy_arr[i]==0 and ypred[i]==0:
        tn=tn+1

acc=(tp+tn)/len(testy_arr)
print(acc)
