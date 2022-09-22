import numpy as np
import matplotlib.pyplot as plt #paquete para graficar datos
import pandas as pd
from sklearn.metrics import mean_squared_error 
#se utiliza el módulo de regresión lineal del paquete scikit_learn
from sklearn.linear_model import LinearRegression 

# este paquete también se conoce como scikit_learn
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline

#ecuación de segundo grado
x=10*np.random.normal(0,1,65)
y=10*(-x**2)+np.random.normal(-100,100,65)

lm=LinearRegression()
lm.fit(x.reshape(-1,1),y.reshape(-1,1))
y_pred=lm.predict(x.reshape(-1,1))
#plt.figure(figsize=(10,5))
#plt.scatter(x,y,s=15)
#plt.plot(x,y_pred,color='r')
#plt.xlabel('Predicción',fontsize=16)
#plt.ylabel('Predicción',fontsize=16)
#plt.show()

# se establece que la ecuación es de segundo grado.
Input=[('polynomial',PolynomialFeatures(degree=2)),('modal',LinearRegression())]
pipe=Pipeline(Input)
pipe.fit(x.reshape(-1,1),y.reshape(-1,1))
poly_pred=pipe.predict(x.reshape(-1,1))
sorted_zip = sorted(zip(x,poly_pred))
x_poly, poly_pred = zip(*sorted_zip)
plt.figure(figsize=(10,6))
plt.scatter(x,y,s=15)
plt.plot(x,y_pred,color='r',label='Regresión lineal')
plt.plot(x_poly,poly_pred,color='g',label='Regresion polinómica')
plt.xlabel('Predicción',fontsize=16)
plt.ylabel('Escala',fontsize=16)
plt.legend()
plt.show()