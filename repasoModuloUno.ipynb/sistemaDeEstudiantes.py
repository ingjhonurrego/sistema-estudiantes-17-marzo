

def registrar_estudiante():
    
   
    nombre = input("\n Ingrese porfavor el nombre del estudiante: ")    
      
    edad = int(input("Ingrese la edad: "))
    while edad <= 0:
        print("❌ Error ingresa un edad correcta \n")   
        edad = int(input("Ingrese la edad: "))
        
    n1 = float(input("Ingrese la primer nota: ")) 
    while n1 < 0 or n1 > 5: 
        print("❌ Error ingresa una nota que este entre 0 y 5")
        n1 = float(input("Ingrese la primer nota: "))  
               
    n2 = float(input("Ingrese la segunda nota: "))
    while n2 < 0 or n2 > 5: 
        print("❌ Error ingresa una nota que este entre 0 y 5 ")
        n2 = float(input("Ingrese la segunda nota: ")) 
        
    n3 = float(input("Ingrese la tercer nota: "))
    while n3 < 0 or n3 > 5: 
        print("❌ Error ingresa una nota que este entre 0 y 5 ")
        n3 = float(input("Ingrese la tercer nota: ")) 
        
    return nombre, edad, n1, n2, n3

def calcular_promedio(n1, n2, n3):
    
    promedio = (n1 + n2 + n3) / 3
    return  promedio


def evaluar_estado(promedio):
    if promedio >= 4.0:
        return "Aprobado✅"
    elif promedio >= 3.0 and promedio < 4.0: 
        return "En recuperacion😒"
    else:
        return "Reprobado ❌" 
    

opcion = 1 
estudiantesRegistrados = 0
promedioG = 0 

while opcion != 2:
    
    print("---------------------------------------------------------------------------")
    print("\n🙋===== SISTEMA DE ESTUDIANTES =====🙋\n")
    print ("1️⃣  Registrar estudiante")
    print ("2️⃣  Salir\n")
    opcion = int(input("Seleccione una opcion: "))

    
    if opcion == 1:
        nombre, edad, n1, n2, n3 = registrar_estudiante()
        resultadoPromedio = calcular_promedio(n1, n2, n3)
        print (f"\n Promedio del estudiante: {nombre} ", resultadoPromedio)
        
        estado = evaluar_estado(resultadoPromedio)
        print ("Estado academico: ",estado )
        
        estudiantesRegistrados += 1      
        promedioG += resultadoPromedio
        
    elif opcion == 2: 
        break
    
if estudiantesRegistrados > 0:
    print("\n 👨🏽 Total de estudiantes registrados: ", estudiantesRegistrados)
    print("\n 📈 Promedio general del grupo:", promedioG / estudiantesRegistrados )
    
    
print ("\n") 
print("--------------------------------(❁´◡`❁)----------------------------------")
print("\n Desarrollado por los estudiantes:\n  ")
print("1️⃣  Jhon Alexander Urrego Huertas")
print("2️⃣  Juan Carlos Corrales Ramirez")
print("3️⃣  Juan Jose Aya")
print("---------------------------------------------------------------------------")




    




     
  
        
        
       
        
    
    
 
    

