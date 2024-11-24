fichas = [(a,b) for a in range(7) for b in range (a,7)]

eventoA = [ficha for ficha in fichas if sum(ficha)>5 ]

eventoB = [ficha for ficha in fichas if sum(ficha)%3 == 0]

print("Los pares posibles dentro de un dominó son")

for ficha in fichas:
    print (ficha, end=", ")

print("\n")

print("Las fichas que tienen la suma de puntos mayor a 5 son ")

for ficha in eventoA:
    print (ficha, end=", ")

print("\n")

print("Las fichas que tienen la suma de sus puntos múltiplos de 3 son")

for ficha in eventoB:
    print (ficha, end=", ")

print("\n")

print("El número de fichas que tienen una suma de puntos mayor que cinco es de", len(eventoA), end = "\n\n")

print("El número de fichas que tienen sus puntos como múltiplos de 3 es de", len(eventoB), end = "\n\n")

numTotal = len(fichas)

numEventoA = len(eventoA)

numEventoB = len(eventoB)

probabilidadA = numEventoA/numTotal

probabilidadB = numEventoB/numTotal

print("La proabilidad de que una ficha tenga sus puntos mayor a 5 es de ", "%.2f"%(probabilidadA*100), "%", sep="")

print("La probabilidad de que la suma de puntos sea múltiplo de 2 es de " ,"%.2f"%(probabilidadB*100), "%", sep="")