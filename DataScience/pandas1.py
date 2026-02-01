import pandas as pd
import numpy as np

arr=np.array([1,2,3,4,5])
x=pd.Series(arr)
print(x)
print(x[1])
x=pd.Series(arr,index=["a","b","c","d","e"])
print(x)

mydict={"Name":"Muskan","Age":"22"}
x=pd.Series(mydict)
print(x)
print(x["Age"])


x=pd.Series([1,2,3,4,5])
print(x)
print(x*5)
print(x**2)
print(x[x>2])


s1=pd.Series([10,20,30,40])
s2=pd.Series([20,50,70,90])
#print(s1+s2)
print(s1.add(s2))
s3=pd.Series([70,40,20])
print(s2.add(s3,fill_value=0))

s1=pd.Series([10,20,30,40,50,60,70])
print(s1.head())
print(s1.tail())
print(s1.head(3))
print(s1.tail(3))
print(s1.iloc[0:3])
print(s1.iloc[2:5])

mydata=[
    {"name":"muskan","age":22},
    {"name":"priya","age":22},
    {"name":"jeetu","age":73}
]
mytable=pd.DataFrame(mydata)
print(mytable)
print(mytable["name"])
print(mytable[["name","age"]])
#del mytable["name"]
#mytable.pop("name")
mytable=mytable.drop("name",axis=1)
print(mytable)

#Concating 2 Data Frames
D1={"id":[1,2,3,4,5,6], "Value1":[10,20,30,40,50,60],"Value2":[100,200,300,400,500,600]}
Df1=pd.DataFrame(D1)
D2={"id":[1,2,3,10,11,12], "Value1":[70,80,90,100,110,120],"Value2":[700,800,900,1000,1100,1200]}
Df2=pd.DataFrame(D2)
#pd.concat(df1,df2) --> this will mot work as concat can only have one input
#Converting it into One Dictionary Set
df3=pd.concat({"Data1": Df1,"Data2": Df2})
print(df3)

df3=pd.merge(Df1,Df2,on="id",how="left")
print(df3)
df3=pd.merge(Df1,Df2,on="id",how="right")
print(df3)
df3=pd.merge(Df1,Df2,on="id",how="outer")
print(df3)