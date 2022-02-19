import matplotlib.pyplot as plt
import numpy as np

# sampling rate
sr = 100
# sampling interval
ts = 1.0/sr
t = np.arange(0,1,ts)

freq = 1.
x = 3*np.sin(2*np.pi*freq*t)

freq = 4
x += np.sin(2*np.pi*freq*t)

freq = 7   
x += 0.5* np.sin(2*np.pi*freq*t)

# plt.figure(figsize = (8, 6))
# plt.plot(t, x, 'r')
# plt.ylabel('Amplitude')

# plt.show()

# Dot Product
def discreteFourierTransform(x):
  N = len(x)
  n = np.arange(N)
  k = n.reshape((N,1))
  e = np.exp(-2j * np.pi * k *n/N)
  X = np.dot(e, x)

  return X

# For Loop DFT
def test(x):
  N = len(x)
  X = np.zeros(N, dtype='complex_')
  for k in range(N):
    Xk = 0
    for n in range(N):
      Xk += x[n] * np.exp(-2j * np.pi * k * n/N)
    X[k] = Xk
  return X

# FFT
# TODO: Implement FFT

# Use Numpy library

X = discreteFourierTransform(x)
# X = test(x)

# calculate the frequency
N = len(X)
n = np.arange(N)
T = N/sr
freq = n/T


plt.figure(figsize = (8, 6))
plt.stem(freq, abs(X), 'b', \
         markerfmt=" ", basefmt="-b")
plt.xlabel('Freq (Hz)')
plt.ylabel('DFT Amplitude |X(freq)|')
plt.show()

n_oneside = N//2
# get the one side frequency
f_oneside = freq[:n_oneside]

# normalize the amplitude
X_oneside =X[:n_oneside]/n_oneside

plt.figure(figsize = (12, 6))
plt.subplot(121)
plt.stem(f_oneside, abs(X_oneside), 'b', \
         markerfmt=" ", basefmt="-b")
plt.xlabel('Freq (Hz)')
plt.ylabel('DFT Amplitude |X(freq)|')

plt.subplot(122)
plt.stem(f_oneside, abs(X_oneside), 'b', \
         markerfmt=" ", basefmt="-b")
plt.xlabel('Freq (Hz)')
plt.xlim(0, 10)
plt.tight_layout()
plt.show()