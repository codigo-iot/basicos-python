# El usuario ingresa el límite de datos recopilados 
limit = int(input("Ingresa un número mayor a 3: ")) 
# Muestra los números positivos en múltiplos de 3 
print("los multiplos de tres", limit, "son:") 
for i in range(3, limit + 1, 3): 
    print(i)