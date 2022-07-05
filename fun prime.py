#prime fum
import numpy as np
from matplotlib import pyplot as plt
x=[]
R=[]
x.append(2)

lower = 3
upper = 200000

revr_num = 0
def recur_reverse(k):  
    global revr_num   # We can use it out of the function  
    if (k > 0):  
        Reminder = k % 10  
        revr_num = (revr_num * 10) + Reminder  
        recur_reverse(k // 10)  
    return revr_num  

def binaryToDecimal(binary): 
      
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return(decimal)
    
print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           x.append(num)

#print(x)
n=np.arange(1,len(x)+1)
for i in range(len(x)):
    y=int(np.binary_repr(x[i]))
    z=recur_reverse(y)
    revr_num=0
    R.append(x[i]-binaryToDecimal(z))

plt.scatter(n,R,color='r',s=0.9)
plt.grid()
plt.show()    