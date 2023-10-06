import numpy as np
import matplotlib.pyplot as plt
import imageio

N=51 #Length of the array
M=90 #Time steps
grid=[] 

###Initialization###
A=np.zeros((N,N))
A[int(N/2)][int(N/2)]=1
Anew=A.copy()

###Exclusive or###
def exor(a,b,c,d):
    if a==b and b==c and a==d:
        return 0
    else:
        return 1
###Time iterations and implementation###
image_list=[]
for k in range(M):
    for i in range(1,N-1):
        for j in range(1,N-1):
            Anew[i][j]=exor(A[i-1][j],A[i+1][j],A[i][j-1],A[i][j+1])
    A=Anew.copy() 
    plt.imshow(Anew, cmap='gist_yarg')
    plt.axis('off')
    plt.savefig(f'C:/Users/sergi/OneDrive/Escritorio/Modelling Master/Deterministic Modelling/CA/{k}.png')
    image_list.append(imageio.imread(f'{k}.png'))
    
imageio.mimsave('C:/Users/sergi/OneDrive/Escritorio/Modelling Master/Deterministic Modelling/CA/animation.gif', image_list, fps=5)
