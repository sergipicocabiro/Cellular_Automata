import numpy as np
import matplotlib.pyplot as plt
import random

N=51 #Length of the array
M=60 #Time steps
grid=[] 
p=0.9 #probability

###Initialization###
A=np.zeros(N)
A[int(N/2)]=1
Anew=A.copy()

###Exclusive or###
def exor(a,b):
    if a!=b:
        return 1
    if a==b:
        return 0
###Time iterations and implementation###
for k in range(M):
    for i in range(1,N-1):    
        r=random.random()
        if(r<p):
            Anew[i]=exor(A[i-1],A[i+1])
    grid.append(A)
    A=Anew.copy() 

###Plot###
plt.imshow(grid, cmap='gist_yarg')
plt.show()