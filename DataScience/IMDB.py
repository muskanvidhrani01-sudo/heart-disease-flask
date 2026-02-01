import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
 
MyData=pd.read_csv("IMDB-Movie-Data.csv")
df= pd.DataFrame(MyData,columns=["Rating", "Votes"])
#print(df)
Model=KMeans(n_clusters=3,random_state=42)
Model.fit(df)
ans=Model.labels_
#print(ans)
plt.scatter(df["Rating"],df["Votes"],c=ans)
plt.show()