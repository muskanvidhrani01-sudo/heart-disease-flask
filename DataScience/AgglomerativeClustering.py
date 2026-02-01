import pandas as pd 
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

df=pd.read_csv("heart1.csv")
df=df.dropna()
le=LabelEncoder()
for c in df.columns:
    if df[c].dtype=="object":
        df[c]=le.fit_transform(df[c])

s=StandardScaler()
x=s.fit_transform(df)
#linkage can be single, complete or average.
ag=AgglomerativeClustering(n_clusters=3,metric="euclidean", linkage="single")
ans=ag.fit_predict(x)
print(ans)

d=dendrogram(linkage(x, method="single"))
plt.show()
