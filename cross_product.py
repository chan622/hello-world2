import numpy as np

w = np.array([1,2,3])
r = np.array([2,0,1])

def cross_product(a,b):
    x = a[1]*b[2]-a[2]*b[1]
    y = a[2]*b[0]-a[0]*b[2]
    z = a[0]*b[1]-a[1]*b[0]
    return(np.array([x,y,z]))

print(cross_product(w,r))

#### cross product as a matrix
def cross_product_matrix(a):
    matrix = np.array([0,-a[2],a[1],a[2],0,-a[0],-a[1],a[0],0]).reshape(3,3)
    return(matrix)

print(cross_product_matrix(w))
print(np.dot(cross_product_matrix(w),r.reshape(-1,1)))
