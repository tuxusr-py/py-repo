dificult = int(input("Elige la dificultad (fácil 1, medio 2, difícil 3): "))
contador = 0
if dificult == 1:
	contador = 4
elif dificult == 2:
	contador = 8
elif dificult == 3: 
	contador = 12
contador2 = 0
numeros_principio = "   "
numeros = ""
tablero=[["x" for _ in range(contador)] for _ in range(contador)]
for i in range(contador):
    if len(str(i+1)) >= 2:
        numeros = numeros + " " + " ".join(str(i+1)[0]) 
    else:
        numeros = numeros + "  "
print (numeros_principio + numeros)
numeros=""
for i in range(contador):
    if len(str(i+1)) >= 2:
        numeros = numeros + " " + " ".join(str(i+1)[1]) 
    else:
        numeros = numeros + " " + " ".join(str(i+1)[0]) 
print (numeros_principio + numeros)
print ("    " + " ".join(["_" for _ in range(contador)]))
for i in tablero:
    if len(str(contador2 + 1)) == 1:
        print (str(contador2 + 1)+ "  |" + " ".join(tablero[contador2]) + "|")
    else:
        print (str(contador2 + 1)+ " |" + " ".join(tablero[contador2]) + "|")
    contador2 += 1
print ("    " + " ".join(["¯" for _ in range(contador)]))

