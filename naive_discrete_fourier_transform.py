import numpy as np

# Naive implementation of DFT done by following the precise
# definition. Results in a O(n^2) complexity
def naive_discrete_fourier_transform(dataset):
  N = len(dataset)
  X = np.zeros(N, dtype='complex_')
  for k in range(N):
    X_k = 0
    for n in range(N):
      X_k += dataset[n] * np.exp(-2j * np.pi * k * n/N)
    X[k] = X_k
  return X