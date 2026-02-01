import numpy as np 
x=np.arange(1,6)
y=x
print(x)
print(y)
x[0]=8
print(x)
print(y)

x=np.arange(1,6)
y=x.copy()
x[0]=9
print(x)
print(y)

