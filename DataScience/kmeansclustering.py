import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

mydata=load_iris()
df=pd.DataFrame(mydata.data,columns=mydata.feature_names)
#print(df)
model=KMeans(n_clusters=2,random_state=42)
model.fit(df)
ans=model.labels_
plt.scatter(df["sepal length (cm)"], df["sepal width (cm)"],c=ans)
plt.show()
