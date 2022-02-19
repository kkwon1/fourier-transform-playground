import numpy as np

# Implementation of DFT using matrix multiplication and dot product
# I assume this should still result in a O(n^2) complexity, but I'm not
# entirely sure about the optimizations made within Numpy.
def discrete_fourier_transform(dataset):
  N = len(dataset)
  n = np.arange(N)
  k = n.reshape((N,1))
  e = np.exp(-2j * np.pi * k *n/N)
  X = np.dot(e, dataset)

  return X