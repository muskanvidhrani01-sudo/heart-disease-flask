import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("heart.csv")
#Q1#print(df.head(7))
#Q2#print(df.tail())
#Q3#print(df.dtypes)
#Q4#print(df[['age','chol']])
#Q5#print(df.loc[10:20,['age','sex','target']])
#Q6#print(df.iloc[0:10,0:4])
#Q7#print(df[30:46])
#Q8#print(df['chol']>300)
#Q9#df['BMI_Category']='Unknown'
#print(df)
#Q10#df['HR_Diff']=220-df['thalach']
#print(df)
#Q11#df.pop('HR_Diff')
#print(df)

#Q12
#df1=pd.DataFrame(df.head(10))
#df2=pd.DataFrame(df.tail(10))
#df=pd.concat[df1,df2]
#print(df)

#Q13
#print(df['chol'].mean())
#print(df['chol'].median())

#Q14
#print(df['trestbps'].var())
#print(df['trestbps'].std())

#Q15
#print(df[["age","chol","thalach"]].max())
#print(df[["age","chol","thalach"]].min())

#Q16
#df1=df['chol'].quantile([0.25,0.50,0.75])
#print(df1)

#Q17
#df1=df.groupby("sex").mean()
#print(df1['chol'])

#Q18
#df1=df.groupby("cp")
#print(df1['chol'].mean())
#print(df1['thalach'].mean())
#print(df1['thalach'].max())

#Q19
#print(df.sort_values(by=['chol'],ascending=False))

#Q20
#print(df.sort_values(by=['age','chol'],ascending=[True,False]))

#Q21
#df1=df['chol'].mean()
#df['chol']=df['chol'].fillna(value=df1)
#print(df)

#Q22
#df['chol'].dropna()
#df['trestbps'].dropna()
#print(df)

#Q23
# df1=pd.pivot_table(data=df, index='sex',columns='target',values='chol',aggfunc='mean')
#print(df1)

#Q24
#df1=pd.pivot_table(data=df, index='cp',values='thalach',aggfunc='max')
#print(df1)

#Q25
#print(df.rename(columns={'trestbps':'rest_bp'}))

#Q26
#print(df.reset_index())
9
#Q27
#plt.xlabel('Age')
#plt.ylabel('cholestrol')
#plt.title('Age vs Cholestrol graph')
#plt.plot(df['age'],df['chol'],marker='o',linestyle='dotted')
#plt.show()

#Q28
#plt.xlabel('Chest Pain Type (cp)')
#plt.ylabel('No. of Patients')
#plt.title('No. of patients for each chest pain type')
#df1=(df['cp'].value_counts().sort_index())
#plt.bar(df1.index,df1.values)
#plt.show()

#Q29
#plt.xlabel('Frequency')
#plt.ylabel('target')
#plt.title('Frequency of disease/no disease')
#freq=df['target'].count()
#plt.barh(df['target'],freq,color=['red','green'])
#plt.show()

#Q30
#plt.xlabel('Age')
#plt.ylabel('thalach')
#plt.title('Scatter plot of Age vs thalach')
#plt.scatter(df['age'],df['thalach'])
#plt.grid(True)
#plt.show()

#Q31
#plt.title('Male vs Female')
#count=df['sex'].value_counts()
#size=count.values.tolist()
#plt.pie(size,labels=['male','female'],colors=['red','green'],explode=(0.1,0))
#plt.show()

#Q32
#plt.xlabel('Chol level')
#plt.ylabel('Frequency')
#plt.title('chol level frequency')
#plt.hist(df['chol'],bins=10, rwidth=0.6, edgecolor='black' ,color='blue')
#plt.show()

#Q33
#plt.ylabel('Resting BP')
#plt.title('Box Plot of resting bp')
#plt.boxplot(df['trestbps'])
#plt.show()

#Q34


#Q35
#plt.xlabel('sex')
#plt.ylabel('Avg value')
#plt.title('Avg chol n BP by sex')
#avg=df.groupby('sex')[['chol','trestbps']].mean()
#avg.index=avg.index.map({0:'female',1:'male'})
#plt.bar(avg.index, edgecolor='black' ,color='blue',height=0.8)
#plt.show()

#Q36
#plt.xlabel('Resting BP')
#plt.ylabel('thalach')
#plt.title('Scatter plot of Resting BP vs thalach')
#plt.scatter(df['trestbps'],df['thalach'],marker='+')
#plt.grid(True)
#plt.show()


