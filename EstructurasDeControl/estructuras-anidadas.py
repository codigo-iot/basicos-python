# Solicita un número 
num = float(input("Ingresa un número: ")) 
# condición uno 
if num > 0: 
    adjective = " " 
    if num >= 1000000: 
        adjective = " muy grande " 
    elif num >= 1000: 
        adjective = " grande " 
    # El resultado es una cadena con el adjetivo y el tipo de número 
    result = "Es realmente un número" + adjective + "y positivo" 
elif num < 0: 
    result = "Es un número negativo" 
else: 
    result = "Este número es cero" 
# Imprime el resultado 
print(result)