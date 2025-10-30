import numpy as np
from matplotlib import pyplot as plt
from numpy.fft import fft, ifft

#def Señal sinusoidal de prueba
SAMPLE_RATE = 44100  # Hertz
DURATION = 5  # Seconds

def senoidal(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    # 2pi because np.sin takes radians
    y = np.sin((2 * np.pi) * frequencies)
    return x, y
# Generamos una señal sinusoidal de 2 Hz durante 5 segundos
x, y = senoidal(2, SAMPLE_RATE, DURATION)
plt.plot(x, y)
plt.show()
     
def CTFT(muestras,f_m):
yf = fft(muestras)
xf = fftfreq(muestras.size / f_m)
return yf, xf
