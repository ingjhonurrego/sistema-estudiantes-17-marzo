frase = input("escriba una frase:  ")
letra = input("escriba una letra:  ")

contador = 0

for i in frase:
    if i == letra:
        contador += 1
print("la letra", letra, "aparece", contador, " veces en la palabra: ", frase)
        