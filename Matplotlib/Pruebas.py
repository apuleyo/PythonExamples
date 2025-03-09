import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AffinityPropagation

# Contexto y datos
datos = {"alan" : [2, 4],
         "alberto" : [3, 3],
         "alex" : [3, 2], 
         "zelda" : [7, 6], 
         "zoila" : [6, 7], 
         "zulema" : [6, 8]}

personas = set(datos.keys())
datos = pd.DataFrame(datos, index=["ahorro", "evaluacion"])
print(datos)

# Visualización de la información
plt.figure(figsize=(10, 7))  # Aumentar el ancho de la figura
plt.title("Analisis crediticio", fontsize=20)

plt.scatter(datos.T[0:3]["ahorro"], 
            datos.T[0:3]["evaluacion"], 
            marker="x", s=150, color="red",
            linewidths=5, label="Nombres con A")

plt.scatter(datos.T[3:]["ahorro"], 
            datos.T[3:]["evaluacion"], 
            marker="o", s=150, color="blue",
            linewidths=5, label="Nombres con Z")

for i in range(len(datos.columns)):
    plt.text(datos.iloc[0, i]+0.3, 
             datos.iloc[1, i]+0.3, 
             datos.columns[i].capitalize())
    
plt.xlabel("Ahorro", fontsize=15)
plt.ylabel("Evaluacion Crediticia", fontsize=15)
plt.legend(bbox_to_anchor=(0.8, 1.15), loc='upper left')
plt.box(False)
plt.xlim((0, 10.01))
plt.ylim((0, 10.01))
plt.grid()
plt.show()
