#Q) Is avg marks different from 70(H0:U=70 or not)
import pandas as pd
from scipy.stats import ttest_1samp
df=pd.read_csv("student.csv")
tvalue,pvalue=ttest_1samp(df["marks"],70)
print(tvalue)
print(pvalue)

if pvalue<0.05:
    print("Reject H0")
else:
    print("Accept H0")