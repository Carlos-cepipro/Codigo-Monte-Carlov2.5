import matplotlib.pyplot as plt
import numpy as np
from random import uniform
from math import sqrt

cuadro = 5000  
radio = cuadro / 2  
centro = cuadro / 2  

theta = np.linspace(0, 2 * np.pi, 100)
circ_x = centro + radio * np.cos(theta)
circ_y = centro + radio * np.sin(theta)


n = 2000  
puntos_x = [uniform(0, cuadro) for _ in range(n)]
puntos_y = [uniform(0, cuadro) for _ in range(n)]

x_in, y_in = [], []
x_out, y_out = [], []

for i in range(n):
    distancia = sqrt((puntos_x[i] - centro)**2 + (puntos_y[i] - centro)**2)
    if distancia <= radio:
        x_in.append(puntos_x[i])
        y_in.append(puntos_y[i])
    else:
        x_out.append(puntos_x[i])
        y_out.append(puntos_y[i])

PI_estimate = 4 * (len(x_in) / n)
print(f"Estimación de pi: {PI_estimate}")

cuadro_x = [0, 0, cuadro, cuadro, 0]
cuadro_y = [0, cuadro, cuadro, 0, 0]

plt.plot(cuadro_x, cuadro_y, color="black")  
plt.plot(circ_x, circ_y, label="Circunferencia", color="blue") 


plt.scatter(x_in, y_in, color="red", s=1, label="Dentro")
plt.scatter(x_out, y_out, color="green", s=1, label="Fuera")


plt.text(centro * 0.5, centro * 1.1, f"Pi estimado: {PI_estimate:.4f}", fontsize=12)

plt.gca().set_aspect("equal")  
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Estimación de Pi usando Monte Carlo")
plt.legend()
plt.show()
