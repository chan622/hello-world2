import numpy as np
from numpy import linalg as LA

A = np.array([[9,-4,-2,-4],[-56,32,-28,44],[-14,-14,6,-14],[42,-33,21,-45]])
w,v = LA.eig(A)
print(w)
print(v[:,0])

B = np.array([[3,0,0],[-3,4,9],[0,0,3]])
w,v = LA.eig(B)
print(w)
print(v)
print(LA.inv(B))
