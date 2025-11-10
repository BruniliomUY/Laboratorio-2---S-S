# 🧠 Laboratorio: Digitalización de Señales

## 📋 About
Este laboratorio tiene como objetivo comprender el proceso de **digitalización de señales** y analizar las condiciones necesarias para que una señal muestreada represente de forma fiel a su contraparte en tiempo continuo.  

A través de la experimentación y el análisis, se busca evidenciar cómo el **muestreo insuficiente** puede generar fenómenos de **aliasing** y representación incorrecta de la información, algo que ocurre con frecuencia en sistemas digitales del mundo real.

---

## ⚙️ Activity
Durante la actividad se realizaron las siguientes etapas:

1. **Generación de señales analógicas** con diferentes frecuencias y formas de onda.  
2. **Muestreo** de las señales utilizando distintos períodos de muestreo.  
3. **Reconstrucción** de las señales digitalizadas para comparar con las originales.  
4. **Análisis del aliasing** y estudio del teorema de Nyquist-Shannon.  
5. **Visualización y discusión** de los resultados obtenidos mediante gráficos y observaciones.

---

## 🧩 Objetivos de aprendizaje
- Comprender el concepto de **frecuencia de muestreo** y su impacto en la fidelidad de una señal digital.  
- Identificar cuándo una señal digitalizada **representa correctamente** a su versión analógica.  
- Reconocer y explicar el fenómeno de **aliasing**.  
- Aplicar herramientas computacionales para simular y analizar señales muestreadas.

---

## 🧪 Herramientas utilizadas
- **Lenguaje:** Python / MATLAB / Octave *(indicar el utilizado)*  
- **Librerías:** NumPy, Matplotlib, SciPy *(si aplica)*  
- **Entorno:** Jupyter Notebook o similar  

---

## 📈 Resultados esperados
Al finalizar la práctica, el estudiante será capaz de:
- Evaluar si una frecuencia de muestreo es adecuada.  
- Simular señales analógicas y su digitalización.  
- Visualizar el error introducido por el submuestreo.  
- Interpretar correctamente las gráficas tiempo-frecuencia.

---

## 🧾 Estructura del repositorio
```bash
├── /notebooks/         # Simulaciones y gráficos
├── /data/              # Archivos de señal (si aplica)
├── /figures/           # Imágenes o resultados
├── README.md           # Este archivo
└── main.py             # Código principal (si aplica)
