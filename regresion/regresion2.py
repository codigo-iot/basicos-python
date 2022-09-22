import numpy as np
import matplotlib.pyplot as plt #paquete para graficar datos
import pandas as pd
from sklearn.metrics import mean_squared_error # este paquete también se conoce como scikit_learn
#se utiliza el módulo de regresión lineal del paquete scikit_learn
from sklearn.linear_model import LinearRegression 

#ecuación de segundo grado
x=10*np.random.normal(0,1,65)
y=10*(-x**2)+np.random.normal(-100,100,65)

lm=LinearRegression()
lm.fit(x.reshape(-1,1),y.reshape(-1,1))
y_pred=lm.predict(x.reshape(-1,1))
plt.figure(figsize=(10,5))
plt.scatter(x,y,s=15)
plt.plot(x,y_pred,color='r')
plt.xlabel('Predicción',fontsize=16)
plt.ylabel('Predicción',fontsize=16)
plt.show()