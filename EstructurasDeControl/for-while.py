MIN = 1 
MAX = 20 
#La instrucción end="" al final del argumento de print, evita que el programa continue a la siguiente línea 
print(" ", end="") 
for i in range(MIN, MAX + 1): 
    print("%4d" % i, end="") 
print() 
for i in range(MIN, MAX + 1): 
    print("%4d" % i, end="") 
for j in range(MIN, MAX + 1): 
    print("%4d" % (i * j), end="") 
print()