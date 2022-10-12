#!/usr/bin/env python
# coding: utf-8

import numpy as np
inp = input().split()
x = inp[0].lower()
y = inp[1].lower()
match = int(inp[2])
mismatch = int(inp[3])
gap = int(inp[4])


# Start data: length of sequences, importing numpy, building of matrix

n = len(x)
m = len(y)
mat = np.array([[0 for j in range(m+1)] for i in range(n+1)])
for j in range(m+1):
    mat[0][j] = max(j*gap, 0)
    
for i in range(n+1):
    mat[i][0] = max(i*gap, 0)
    
# Filling matrix with weights

for i in range(1, n+1):
    for j in range(1, m+1):
        if x[i-1] == y[j-1]:
            diag = mat[i-1][j-1]+match
        else:
            diag = mat[i-1][j-1]+mismatch
        mat[i][j] = max(diag, mat[i-1][j]+gap, mat[i][j-1]+gap, 0)
        
        
max_coords = np.where(mat==np.amax(mat))
st = np.max(mat)
# Output sequences

a1=[]
a2=[]
n = max_coords[0][0]
m = max_coords[1][0]

while mat[n][m]>0:
    vert = mat[n-1][m]+gap
    hor = mat[n][m-1]+gap
    if x[n-1] == y[m-1]:
        diag1 = mat[n-1][m-1]+match
    else:
        diag1 = mat[n-1][m-1]+mismatch
    if mat[n][m] == diag1:
        a1.append((x[n-1]).upper())
        a2.append((y[m-1]).upper())
        n -= 1
        m -= 1    
    elif mat[n][m] == vert:
        a1.append((x[n-1]).upper())
        a2.append("_")
        n -= 1
    elif mat[n][m] == hor and (m>0 or m>=n):
        a1.append("_")
        a2.append((y[m-1]).upper())
        m -= 1
min_x = n
min_y = m
#Outputs
print(st, end=" ")
print(x[0:min_x], *a1[::-1], x[(max_coords[0][0]):len(x)+1], sep="", end=" ")
print(y[0:min_y], *a2[::-1], y[(max_coords[1][0]):len(y)+1], sep="")

