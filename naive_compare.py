import numpy as np
import time
import matplotlib.pyplot as plt
from naive_discrete_fourier_transform import *
from discrete_fourier_transform import *

########################
#        TEST 1        #
########################

naive_results = []
dft_results = []

def perform_test_single_sine_wave(num_datapoints):
  # num_datapoints = 1000
  duration = 1
  sampling_interval = duration/num_datapoints

  amplitude = 3
  frequency = 1

  t = np.arange(0,1,sampling_interval)

  x = amplitude * np.sin(2*np.pi*frequency*t)


  start = time.time()
  naive_discrete_fourier_transform(x)
  end = time.time()
  duration = end-start
  print (f'Naive result for {num_datapoints} datapoints. Duration: {duration}')
  naive_results.append(duration)

  start = time.time()
  discrete_fourier_transform(x)
  end = time.time()
  duration = end-start
  print (f'DFT result for {num_datapoints} datapoints. Duration: {duration}')
  dft_results.append(duration)


datasizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
for datasize in datasizes:
  perform_test_single_sine_wave(datasize)

plt.figure(figsize = (12, 6))
plt.subplot(121)
plt.stem(datasizes, naive_results)
plt.xlabel('Number of Samples')
plt.ylabel('Duration in Seconds')

plt.subplot(122)
plt.stem(datasizes, dft_results)
plt.xlabel('Number of Samples')
plt.show()
