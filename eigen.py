import numpy as np
from numpy import linalg as LA

A = np.array([[1,0,0],
              [1,2,0],
              [2,3,3]])

lamb, v = LA.eig(A)
print(lamb)
print(v)
print(v[1]*3,np.matmul(A,v[1]))
