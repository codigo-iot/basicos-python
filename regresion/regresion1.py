import numpy as np
import matplotlib.pyplot as plt #paquete para graficar datos
import pandas as pd
from sklearn.metrics import mean_squared_error # este paquete también se conoce como scikit_learn

#ecuación de segundo grado
x=10*np.random.normal(0,1,65)
y=10*(-x**2)+np.random.normal(-100,100,65)

#obtención de gráfica-

plt.figure(figsize=(10,5))
plt.scatter(x,y,s=15)
plt.xlabel('Predicción',fontsize=16)
plt.ylabel('Objetivo',fontsize=16)
plt.show()