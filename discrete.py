import numpy as np
import math

def P(n,k):
    return(math.factorial(n)/math.factorial(k))

def C(n,k):
    return(P(n,k)/math.factorial(n-k))

print(P(10,5))
print(C(10,5))
