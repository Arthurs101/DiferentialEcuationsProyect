import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
print ("Ingrese los datos")

opt = 0
def coolant(Ts, Ta,k,t):
    return (Ts + (Ta - Ts)*np.exp(-k*t)) - 273.15
while opt != 3:
    print ('''
1. Valor exacto de temperatura en un tiempo 
2. simulacion de intervalo de temperatura
3. Salir
           ''')
    opt = int(input("ingrese su eleccion: "))
    if opt == 1:
        Ts = float(input("ingrese la temperatira ambiente °C: "))
        Ta = float(input(" ingrese la temperatira inicial °C: "))
        k = float(input("ingrese un valor a la constante de enfriamiento: min^-1 :"))
        t = float(input("ingrese el valor especifico del tiempo (min): "))
        Ts = Ts + 273.15
        Ta = Ta + 273.15
        print(f'valor de temperatura en el minuto {t}: {(round(coolant(Ts,Ta,k,t)),2)} °C')
    elif opt == 2:
        Ts = float(input("ingrese la temperatira ambiente °C: "))
        Ta = float(input(" ingrese la temperatira inicial °C: "))
        Ts = Ts + 273.15
        Ta = Ta + 273.15
        k = float(input("ingrese un valor a la constante de enfriamiento: min^-1: "))
        t = float(input("ingrese el tiempo a simular (min): "))
        raw_data = {
            "Temperatura(C)" : [],
            "tiempo": []
        }
        for i in np.arange(0.0,t,0.1):
            raw_data["tiempo"].append(i)
            raw_data["Temperatura(C)"].append(coolant(Ts,Ta,k,i))
        df = pd.DataFrame(raw_data)
        df.to_excel("Temperatures.xlsx", index=False)
        plt.suptitle(f'Resultados de Simulación de Temperatura') 
        plt.xlabel('tiempo (min)') 
        plt.ylabel('Temperatura °C')
        plt.plot(raw_data["tiempo"],raw_data["Temperatura(C)"])  #leyenda de la posición     
        plt.legend()  
        plt.show()
            
            
        