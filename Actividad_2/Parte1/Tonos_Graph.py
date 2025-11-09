# Simulación del aliasing en señales de audio
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Audio, display


# Función para generar un tono senoidal

def generar_tono(f_tono, fs, duracion=0.01):
    t = np.arange(0, duracion, 1/fs)
    x = np.sin(2 * np.pi * f_tono * t)
    return t, x


# Función para reproducir y graficar

def reproducir_y_graficar(x, fs, titulo, t):
    print(f"\n▶ {titulo}")
    display(Audio(x, rate=fs))  # Reproductor interactivo

    plt.figure(figsize=(8, 3))
    plt.plot(t[:400], x[:400])
    plt.title(titulo)
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")
    plt.grid(True)
    plt.show()

# 1) Tono de 10 kHz muestreado a 44.1 kHz

f_tono = 10000  # Hz
fs1 = 44100     # Hz
t1, x1 = generar_tono(f_tono, fs1)
reproducir_y_graficar(x1, fs1, "10 kHz muestreado a 44.1 kHz", t1)


# 2) Tono de 10 kHz muestreado a 22.05 kHz

fs2 = 22050
t2, x2 = generar_tono(f_tono, fs2)
reproducir_y_graficar(x2, fs2, "10 kHz muestreado a 22.05 kHz", t2)

# 3) Tono de 10 kHz muestreado a 13 kHz (aliasing esperado)
fs3 = 13000
t3, x3 = generar_tono(f_tono, fs3)
reproducir_y_graficar(x3, fs3, "10 kHz muestreado a 13 kHz (aliasing)", t3)


# 4) Tono de 10 kHz muestreado a 5.25 kHz (aliasing fuerte)

fs4 = 5250
t4, x4 = generar_tono(f_tono, fs4)
reproducir_y_graficar(x4, fs4, "10 kHz muestreado a 5.25 kHz (aliasing fuerte)", t4)