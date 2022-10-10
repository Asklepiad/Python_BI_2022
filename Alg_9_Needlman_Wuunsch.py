#!/usr/bin/env python
# coding: utf-8


# Start data: length of sequences, importing numpy, building of matrix

x, y = input().split()
import numpy as np
n = len(x)
m = len(y)
mat = np.array([[0 for j in range(m+1)] for i in range(n+1)])
for j in range(m+1):
    mat[0][j] = -j
for i in range(n+1):
    mat[i][0] = -i
    

# Filling matrix with weights

for i in range(1, n+1):
    for j in range(1, m+1):
        if x[i-1] == y[j-1]:
            diag = mat[i-1][j-1]+1
        else:
            diag = mat[i-1][j-1]-1
        mat[i][j] = max(diag, mat[i-1][j]-1, mat[i][j-1]-1)       

        
# Output sequences

a1=[]
a2=[]


# Searching the right way

while n>0 or m>0: 
    vert = mat[n-1][m]-1
    hor = mat[n][m-1]-1  
    if x[n-1] == y[m-1]:
        diag1 = mat[n-1][m-1]+1
    else:
        diag1 = mat[n-1][m-1]-1
    if mat[n][m] == vert:
        a1.append(x[n-1])
        a2.append("_")
        n -= 1
    elif mat[n][m] == hor:
        a1.append("_")
        a2.append(y[m-1])
        m -= 1
    elif mat[n][m] == diag1:
        a1.append(x[n-1])
        a2.append(y[m-1])
        n -= 1
        m -= 1
        
#Outputs

print(*a1[::-1], sep="", end=" ")
print(*a2[::-1], sep="")

