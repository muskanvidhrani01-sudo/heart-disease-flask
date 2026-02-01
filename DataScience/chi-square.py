import pandas as pd
from scipy.stats import chi2_contingency
df=pd.read_csv("student.csv")
table=pd.crosstab(df["gender"],df["mode"])
chi2,p,dof,expected=chi2_contingency(table)
print(chi2)
print(p)
if p<0.05:
    print("Reject H0")
else:
    print("Accept H0")