import numpy as np
from matplotlib import pyplot as plt
from numpy.fft import fft, ifft, fftfreq, fftshift

def senoidal(freq, sample_rate, duration):
    x = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    frequencies = x * freq
    # 2pi because np.sin takes radians
    y = np.cos((2 * np.pi) * frequencies)
    return x, y
     
def DFT(x, fs, title="Espectro de Magnitud (FFT)"):
    """
    Calcula y grafica la FFT de una señal x muestreada a frecuencia fs.

    Parámetros:
        x  : array, señal en el tiempo
        fs : float, frecuencia de muestreo [Hz]
        title : str, título del gráfico
    """
    N = len(x)
    X = fft(x)
    X_shifted = fftshift(X)
    freqs = fftshift(fftfreq(N, d=1.0 / fs))
    X_mag = np.abs(X_shifted)
    # Gráfico
    plt.figure(figsize=(8,4))
    plt.plot(freqs, X_mag)
    plt.title(title)
    plt.xlabel("Frecuencia [Hz]")
    plt.ylabel("|X(f)| (normalizado)")
    plt.grid(True)
    plt.show()

    return freqs, X_mag

def CTFT(x, fs, title="Espectro de Magnitud (FFT con Zero-Padding)", padding_factor=4):
    """
    Calcula y grafica la FFT de una señal x muestreada a frecuencia fs con zero-padding.

    Parámetros:
        x  : array, señal en el tiempo
        fs : float, frecuencia de muestreo [Hz]
        title : str, título del gráfico
        padding_factor : int, factor de aumento del tamaño (default=4)
    """
    N = len(x)
    N_pad = padding_factor * N   # nuevo tamaño (4 veces más puntos)
    
    # FFT con zero-padding
    X = fft(x, N_pad)
    X_shifted = fftshift(X)
    freqs = fftshift(fftfreq(N_pad, d=1.0 / fs))
    X_mag = np.abs(X_shifted)

    # Gráfico
    plt.figure(figsize=(8,4))
    plt.plot(freqs, X_mag)
    plt.title(title)
    plt.xlabel("Frecuencia [Hz]")
    plt.ylabel("|X(f)|")
    plt.grid(True)
    plt.show()

    return freqs, X_mag



 
#Ejemplo fs<fmax no cumple la condicion de Nyquist, se produce aliasing

#def Señal sinusoidal de prueba
SAMPLE_RATE = 150  # Hertz
DURATION = 0.5  # Seconds
# Generamos una señal sinusoidal de 150 Hz durante 5 segundos
x, y = senoidal(100, SAMPLE_RATE, DURATION)
plt.plot(x, y)
plt.ylim(1, -1)
plt.show()

DFT(y, SAMPLE_RATE)
CTFT(y, SAMPLE_RATE)

#Ejemplo fs>fmax cumple la condicion de Nyquist, se produce aliasing

#def Señal sinusoidal de prueba
SAMPLE_RATE = 250  # Hertz
DURATION = 0.5  # Seconds
# Generamos una señal sinusoidal de 150 Hz durante 5 segundos
x, y = senoidal(100, 250, DURATION)
plt.plot(x, y)
plt.ylim(1, -1)
plt.show()

DFT(y, SAMPLE_RATE)
CTFT(y, SAMPLE_RATE)
