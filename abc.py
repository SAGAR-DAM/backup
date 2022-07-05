import numpy as np
n=100000
m=n
y=n+1
x=1
for i in range(n-1):
    x=1+(n-1)/y
    y=x
    n=n-1
print(x)

print((1+1/m)**m)
print(np.exp(1))