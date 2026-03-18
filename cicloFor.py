# Calculadora con for

tabla = int(input("Hola,ingresa que tabla de multiplicar quieres resolver: \n"))

print(f"Esta es la tabla del: {tabla}:\n " )

for x in range (1, 11):
    print(f"{tabla} X {x} = {tabla*x} \n")