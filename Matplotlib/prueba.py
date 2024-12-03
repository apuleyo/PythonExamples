import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

clientes = pd.DataFrame({"saldo" : [50000, 45000, 48000, 43500, 47000, 52000, 
                                    20000, 26000, 25000, 23000, 21400, 18000,
                                    8000, 12000, 6000, 14500, 12600, 7000],
                         
                         "transacciones": [25, 20, 16, 23, 25, 18,
                                           23, 22, 24, 21, 27, 18,
                                           8, 3, 6, 4, 9, 3]})

escalador = MinMaxScaler().fit(clientes.values) #Determinar cuál es el minimo y el máximo

clientes = pd.DataFrame(escalador.transform(clientes.values),
                       columns=["saldo", "transacciones"]) # DataFrame con los valores clientes.values escalados.
                       
kmeans = KMeans(n_clusters=7).fit(clientes.values) #Determinamos el cluster al que pertenece cada cliente

clientes["cluster"] = kmeans.labels_ #Añadimos una nueva columna al DataFrame con los valores del cluster
print(clientes)

# Instrucciones para graficar los clusters 

plt.figure(figsize=(8, 5), dpi=100) #Tamaño y resolución de la figura

colores = ["red", "blue", "orange", "black", "purple", "pink", "brown"] #Colores a utilizar par gráficar cada uno de los clusters

for cluster in range(kmeans.n_clusters):
	#Gráficar cada uno de los puntos
    plt.scatter(clientes[clientes["cluster"] == cluster]["saldo"], 
                clientes[clientes["cluster"] == cluster]["transacciones"],
                marker="o", s=180, color=colores[cluster], alpha=0.5)
    #Gráficar cada uno de los centroides
    plt.scatter(kmeans.cluster_centers_[cluster][0], 
                kmeans.cluster_centers_[cluster][1], 
                marker="P", s=280, color=colores[cluster])

plt.title("Clientes", fontsize=20)
plt.xlabel("Saldo en cuenta de ahorros (pesos)", fontsize=15)
plt.ylabel("Veces que uso tarjeta de credito", fontsize=15)
plt.text(0.8, 0.2, "K = %i" % kmeans.n_clusters, fontsize=15)
plt.text(0.8, 0, "Inercia = %0.2f" % kmeans.inertia_, fontsize=15)
plt.xlim(-0.1, 1.1)
plt.ylim(-0.1, 1.1)    
plt.show()

del clientes["cluster"]