#!/usr/bin/env python
# coding: utf-8


import numpy as np
inp = input().split()
x = inp[0]
y = inp[1]
gap = int(inp[2])
prematr = [int(i) for i in inp[3::]]
dic = {'A':0, 'T':1, 'G':2, 'C':3}
matr = np.resize(prematr,(4,4))


# Start data: length of sequences, importing numpy, building of matrix

n = len(x)
m = len(y)
mat = np.array([[0 for j in range(m+1)] for i in range(n+1)])
for j in range(m+1):
    mat[0][j] = j*gap
for i in range(n+1):
    mat[i][0] = i*gap



# Filling matrix with weights

for i in range(1, n+1):
    for j in range(1, m+1):
        diag = mat[i-1][j-1]+matr[dic[x[i-1]]][dic[y[j-1]]]
        mat[i][j] = max(diag, mat[i-1][j]+gap, mat[i][j-1]+gap)


# Output sequences

a1=[]
a2=[]


# Searching the right way
while n>0 or m>0:
    vert = mat[n-1][m]+gap
    hor = mat[n][m-1]+gap
    diag1 = mat[n-1][m-1]+matr[dic[x[n-1]]][dic[y[m-1]]]
    
    
    if mat[n][m] == hor and (m>0 or m>=n):
        a1.append("_")
        a2.append(y[m-1])
        m -= 1
    elif mat[n][m] == vert:
        a1.append(x[n-1])
        a2.append("_")
        n -= 1
    elif mat[n][m] == diag1:
        a1.append(x[n-1])
        a2.append(y[m-1])
        n -= 1
        m -= 1

#Outputs

print(*a1[::-1], sep="", end=" ")
print(*a2[::-1], sep="")

