import numpy as np
import time
import matplotlib.pyplot as plt
from naive_discrete_fourier_transform import *
from discrete_fourier_transform import *
from cooley_tukey_fourier_transform import *

########################
#        TEST 1        #
########################

naive_results = []
dft_results = []
fft_results = []

def perform_test_single_sine_wave(num_datapoints):
  # num_datapoints = 1000
  duration = 1
  sampling_interval = duration/num_datapoints

  amplitude = 3
  frequency = 1

  t = np.arange(0,1,sampling_interval)

  x = amplitude * np.sin(2*np.pi*frequency*t)


  # start = time.time()
  # naive_discrete_fourier_transform(x)
  # end = time.time()
  # duration = end-start
  # print (f'Naive result for {num_datapoints} datapoints. Duration: {duration}')
  # naive_results.append(duration)

  start = time.time()
  discrete_fourier_transform(x)
  end = time.time()
  duration = end-start
  print (f'DFT result for {num_datapoints} datapoints. Duration: {duration}')
  dft_results.append(duration)

  start = time.time()
  FFT(x)
  end = time.time()
  duration = end-start
  print (f'DFT result for {num_datapoints} datapoints. Duration: {duration}')
  fft_results.append(duration)

def power_of_two_list(start, n):
  list = []
  for j in range(start, n):
    list.append(2**j)
  return list

datasizes = power_of_two_list(5,15)
# datasizes = range(100, 1000, 100)
for datasize in datasizes:
  perform_test_single_sine_wave(datasize)

plt.figure(figsize = (18, 6))
plt.tight_layout()
# plt.subplot(121)
# plt.stem(datasizes, naive_results)
# plt.title('For Loop Implementation')
# plt.xlabel('Number of Samples')

plt.subplot(1, 2, 1)
plt.stem(datasizes, dft_results)
plt.title('Dot Product Implementation')
plt.xlabel('Number of Samples')
plt.ylabel('Duration in Seconds')

plt.subplot(1, 2, 2)
plt.stem(datasizes, fft_results)
plt.title('Fast Fourier Transform')
plt.xlabel('Number of Samples')
plt.show()
