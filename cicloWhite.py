menu = """
Restaurante el buen sabor:

1. Hamburguesa $20.000
2. Pizza $15.000
3. Ensalada $4.500
4. Salchipapa $8.000
5. perro caliente $12.000
6. Salir

"""
print(menu)

opcion = 0
cuenta = 0
totalhamburguesa = 0
totalpizza = 0
totalensalda = 0
totalsalchipapas = 0
totalperrocaliente = 0
cuentahamburguesa = 0
cuentapizza = 0
cuentaensalda = 0
cuentasalchipapas = 0
cuentaperrocaliente = 0


while opcion != 6:
    opcion = int(input("Ingrese una opcion del menu: "))
    if opcion == 1:
        print("Has elegido hamburguesa")
        totalhamburguesa += 1
        cuenta += 20000
        cuentahamburguesa += 20000
    if opcion == 2:
        print("Has elegido pizza")
        totalpizza += 1
        cuenta = cuenta + 15000
        cuentapizza += 15000
    if opcion == 3:
        print("Has elegido ensalada")
        totalensalda += 1
        cuenta += 4500
        cuentaensalda += 4500
    if opcion == 4:
        print("Has elegido salchipapas")
        totalsalchipapas += 1
        cuenta = cuenta + 8000
        cuentasalchipapas += 8000
    if opcion == 5:
        print("Has elegido perrocaliente")
        totalperrocaliente += 1
        cuenta = cuenta + 12000
        cuentaperrocaliente += 12000
        
    if opcion == 6:
     
        print(f"Gracias por visitar el restaurante, su cuenta es: {cuenta}")
        
        print(f"cantidad de hamburguesas: {totalhamburguesa} \n y la cuenta de hamburguesas es: {cuentahamburguesa} ")
        print(f"cantidad de pizza: {totalpizza} \n y la cuenta de pizza es: {cuentapizza}" )
        print(f"cantidad de ensalada: {totalensalda}\n y la cuenta de ensalada es: {cuentaensalda}" )
        print(f"cantidad de salchipapas: {totalsalchipapas} \n y la cuenta de salchipapas es: {cuentasalchipapas} " )
        print(f"cantidad de perro caliente: {totalperrocaliente} \n y la cuenta de  perro caliente es:{cuentaperrocaliente} " )
        
              
        
        
        break
    else: 
        print ("opcion invalida")
        
        print(menu) 
    
    
        





