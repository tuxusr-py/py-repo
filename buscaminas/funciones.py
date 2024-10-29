import random as r
def print_tablero():
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
    return tablero

def poner_minas(dificult, contador, minas):
    tablero_m=[["x" for _ in range(contador)] for _ in range(contador)]
    for i in range(minas):
        random = r.randint(0, contador - 1)
        random2 = r.randint(0, contador - 1)
        while tablero_m[random][random2] == "b":
            random = r.randint(0, contador - 1)
            random2 = r.randint(0, contador - 1)
        tablero_m[random][random2] = "b"
    return tablero_m

def nose(tablero_m):
    cosa = int(input("cosa: "))
    for i in tablero_m:
        if tablero_m[cosa % 10][cosa // 10 % 10] == "b":
            print("a")
        else:
            print("b")

dificult = int(input("Elige la dificultad (fácil 1, medio 2, difícil 3): "))
contador = 0
if dificult == 1:
    contador = 4
    minas = 4
elif dificult == 2:
    contador = 8
    minas = 10
elif dificult == 3: 
    contador = 12
    minas = 16
tablero_m = poner_minas(dificult, contador, minas)
nose(tablero_m)