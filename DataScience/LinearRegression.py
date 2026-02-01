import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("heart.csv")
x= df['age']
x=np.array(x)
y=df['chol']
y=np.array(y)
n=len(x)

xsum=np.sum(x)
ysum=np.sum(y)
xysum=np.sum(x*y)
x2sum=np.sum(x*x)

b=(n*xysum-xsum*ysum)/(n*x2sum-xsum**2)
print(b)
a=(ysum-b*xsum)/n
print(a)
x=50
predy=a+b*x
print(predy)