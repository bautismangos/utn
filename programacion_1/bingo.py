import random

numero_salido = []

carton = [
    [random.randint(1, 50) for _ in range(5)],
    [random.randint(1, 50) for _ in range(5)],
    [random.randint(1, 50) for _ in range(5)],
    [random.randint(1, 50) for _ in range(5)],
    [random.randint(1, 50) for _ in range(5)]
]

for fila in carton:
    for numero in fila:
        print(numero, end=" ")
    print(" ")

while True:
    numero = random.randint(1, 50)
    entrada = input("Ingrese S para iniciar el bingo: ")
    
    if entrada == "S" or entrada == "s":
        if len(numero_salido) >= 50:
            print("BINGOOO!!! Ve a reclamar tu premio.")
            break
            
        while numero in numero_salido:
            numero = random.randint(1, 50)
            
        numero_salido.append(numero)
        
        print("Iniciando sorteo...")
        print("El numero sorteado es:")
        print(numero)
        print("==" * 60)
        print("---CARTON---")
        print("==" * 60)
        for fila in carton:
            for num in fila:
                print(num, end=" ")
            print(" ")
            
        print("==" * 60)
    else:
        print("Debe ingresar s o S para iniciar el bingo.")
        continue
        
    for i in range(len(carton)):
        for j in range(len(carton[i])):
            if carton[i][j] == numero:
                carton[i][j] = "X"