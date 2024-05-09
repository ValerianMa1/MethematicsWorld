import numpy as np

print(np.fft.fft2(np.array(((1,2,3),(4,5,6),(7,8,9)))))
print(np.fft.ifft2(np.fft.fft2(np.array(((1,2,3),(4,5,6),(7,8,9))))))
