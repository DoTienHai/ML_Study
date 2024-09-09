import numpy as np

def random_array(dimension, min, max):
    return np.random.randint(min, max + 1, size=(dimension))

# Matrix multiplication
A = random_array([4,2], -10, 10)
B = random_array([2,4], -10, 10)
C = np.dot(A,B)

# matrix determinant
det_C = np.linalg.det(C)
if det_C:
    # Inverse matrix
    inv_C = np.linalg.inv(C)
    # eigenvalues ​​and eigenvectors of the matrix
    eigvals, eigvecs = np.linalg.eig(C)

# Variance and standard deviation
var = np.var(A)
std_dev = np.std(A)

