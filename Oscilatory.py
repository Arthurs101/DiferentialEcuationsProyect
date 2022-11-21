import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.integrate import odeint  # importar la odeint para relizar la integración y resoluciíon del sistema de ecuaciones
k = 0
m = 0 
B = 0 ##constante de amortiguación 


def oscilate(Vector ,t):
    return [Vector[1], (-k * Vector[0] / m ) + (B / m * Vector[1])] #devuelve un nuevo vector con posiciones de velocidad y de posicíon 

Initial =[] #condiciones iniciales (posición , velocidad)

Initial.append( float(input("ingrese posición inicial (m):  ")) ) 
Initial.append( float(input("ingrese velocidad inicial (m/s): ")) )
k = float(input("Ceoficiente del resorte: (k) "))

if k <= 0:
    print("entrada no válida")
while(k <= 0 ):
    k = float(input("Ceoficiente del resorte: (k) "))
    
m = float(input("masa unida al  resorte (kg) "))
if m <= 0:
    print("entrada no válida")
    
while(m <= 0 ):
    m = float(input("masa del resorte (kg) "))
    
B = -float(input("Ceoficente de amortiguamiento "))
limit = float(input("Tiempo a simular (segundos) "))
if limit <= 0:
    print("entrada no válida")
while(limit <= 0 ):
    limit = int(input("Tiempo a simular (segundos) "))
    
t_output = np.arange(0, limit, 0.01)  #Rango

result = odeint(oscilate, Initial, t_output) 

fig, ax2 = plt.subplots(ncols = 1, figsize=(10,10))

x, v = result.T  # extraer columnas y filas de la posición (x) y la velocidad (v)
raw_data = {
    "Time": [],
    "PositionX": [],
    "Speed": []
}
raw_data["Time"] = t_output
raw_data["PositionX"] = x
raw_data["Speed"] = v
df = pd.DataFrame(raw_data)
df.to_excel('ResultadosSimulación.xlsx')
plt.suptitle(f'Resultados de Simulación: Masa: {m} kg , K : {k} , b: {-B}') 
plt.subplot(2, 1,1)

plt.plot(t_output, x)  #leyenda de la posición
plt.xlabel('tiempo (s)') 
plt.ylabel('posición (m)')
plt.title('Posición')

plt.subplot(2, 1, 2)
plt.plot(t_output, v)
plt.xlabel('tiempo (s)') 
plt.ylabel('velocidad (m/s)')
plt.title('Velocidad')
plt.legend()                     
plt.show()
          
                                            
    