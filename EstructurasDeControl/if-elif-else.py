# Lee un número  
num = float(input("Ingresa un número: ")) 
# El resultado se almacena en una variable llamada result 
if num > 0: 
    result = "El número es positivo" 
elif num < 0: 
    result = "El número es negativo" 
else: 
    result = "El número es cero" 
print(result)