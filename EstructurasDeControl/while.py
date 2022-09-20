line = input("Ingresa 8 bits (ceros y unos) ") 
# Inicia el bucle hasta encontrar un espacio en blanco 
while line != "": 
    # Condición que asegura que tiene exactamente 8 ceros y unos  
    if line.count("0") + line.count("1") != 8 or len(line) != 8: 
        # Si es diferente de ocho, intenta de nuevo 
        print("no son ocho bits") 
    else: 
        # Cuenta los unos 
        ones = line.count("1") 
        # Este conteo regresa el número de veces que aparece el uno en la cadena de ocho bits 
        # despliega el bit de paridad 
        if ones % 2 == 0: 
            print("El bit de paridad debe de ser 0.") 
        else: 
            print("El bit de paridad debe de ser 1.") 
            # Lee la siguiente cadena de bits 
    line = input("Enter 8 bits: ")