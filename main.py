from tokens import *


def separarRenglones():
    with open("programa.txt", "r") as programaPrincipal:
        iterador = []
        for lineas in programaPrincipal:
            iterador.append(lineas)
    return iterador


def crearObArb(numero, listaArgs):
    if numero == 24:
        return programa(numero, "programa", listaArgs)
    elif numero == 25:
        return definiciones(numero, "definiciones", listaArgs)
    elif numero == 26:
        return definicion(numero, "definicion", listaArgs)
    elif numero == 27:
        return defVar(numero, "defVar", listaArgs)
    elif numero == 28:
        return listaVar(numero, "listaVar", listaArgs)
    elif numero == 29:
        return defFunc(numero, "defFunc", listaArgs)
    elif numero == 30:
        return parametros(numero, "parametros", listaArgs)
    elif numero == 31:
        return listaParam(numero, "listaParam", listaArgs)
    elif numero == 32:
        return bloqFunc(numero, "bloqFunc", listaArgs)
    elif numero == 33:
        return defLocales(numero, "defLocales", listaArgs)
    elif numero == 34:
        return defLocal(numero, "defLocal", listaArgs)
    elif numero == 35:
        return sentencias(numero, "sentencias", listaArgs)
    elif numero == 36:
        return sentencia(numero, "sentencia", listaArgs)
    elif numero == 37:
        return otro(numero, "otro", listaArgs)
    elif numero == 38:
        return bloque(numero, "bloque", listaArgs)
    elif numero == 39:
        return valorRegreso(numero, "valorRegreso", listaArgs)
    elif numero == 40:
        return argumentos(numero, "argumentos", listaArgs)
    elif numero == 41:
        return listaArgumentos(numero, "listaArgumentos", listaArgs)
    elif numero == 42:
        return termino(numero, "termino", listaArgs)
    elif numero == 43:
        return llamadaFunc(numero, "llamadaFunc", listaArgs)
    elif numero == 44:
        return sentenciaBloque(numero, "sentenciaBloque", listaArgs)
    elif numero == 45:
        return expresion(numero, "expresion", listaArgs)


def anLeToArchivo(listaAnalizada):
    with open("AnalizadorLexico.txt", "w") as analizador:
        for partes in listaAnalizada:
            analizador.write(partes.__str__() + "\n")


def arSiToArchivo(listaArbol):
    with open("ArbolSintactico.txt", "w") as analizador:
        for partes in listaArbol:
            analizador.write(partes)


def cargarArchivo():
    matriz = []
    with open("compilador.lr", "r") as gramatica:
        for linea in gramatica:
            listaAuxiliar = linea.split("\t")
            matriz.append(listaAuxiliar)
    return matriz


def cargarReglas():
    matriz = []
    with open("Reglas.txt", "r") as gramatica:
        for linea in gramatica:
            listaAuxiliar = linea.split("\t")
            matriz.append(listaAuxiliar)
    return matriz


def analizadorSintactico(listaAnalizadorLexico):
    matriz = cargarArchivo()
    reglas = cargarReglas()
    pilaPrincipal = [0]
    contadorPila = 0
    contadorLexico = 0
    while contadorLexico < len(listaAnalizadorLexico):
        posicionTabla = int(matriz[pilaPrincipal[contadorPila]][listaAnalizadorLexico[contadorLexico].tipo])
        if posicionTabla == -1:
            return True, pilaPrincipal[1]
        elif posicionTabla == 0:
            return False
        else:
            if posicionTabla > 0:
                pilaPrincipal.append(listaAnalizadorLexico[contadorLexico])
                pilaPrincipal.append(posicionTabla)
                contadorLexico += 1
                contadorPila += 2
            else:
                regla = int((-1 * posicionTabla) - 2)
                listaArg = []
                for contador in range((int(reglas[regla][1]) * 2)):
                    if contador % 2 != 0:
                        listaArg.append(pilaPrincipal.pop())
                    else:
                        pilaPrincipal.pop()
                    contadorPila -= 1
                pilaPrincipal.append(crearObArb(int(reglas[regla][0]), list(reversed(listaArg))))
                contadorPila += 1
                posicionTabla1 = int(matriz[int(pilaPrincipal[contadorPila - 1])][int(reglas[regla][0])])
                pilaPrincipal.append(posicionTabla1)
                contadorPila += 1
    return False


def analizadorLexico(listaRenglones):
    listaResultante = []
    for renglon in listaRenglones:
        cadenaAuxiliar = ""
        banderaEstado = 0
        contadorPosiciones = 0
        while contadorPosiciones < len(renglon):
            if banderaEstado == 0:
                if renglon[contadorPosiciones].isalpha():
                    banderaEstado = 1
                    cadenaAuxiliar += renglon[contadorPosiciones]
                elif renglon[contadorPosiciones].isdigit():
                    banderaEstado = 2
                    cadenaAuxiliar += renglon[contadorPosiciones]
                elif renglon[contadorPosiciones] == "\"" or renglon[contadorPosiciones] == "\'":
                    banderaEstado = 4
                    cadenaAuxiliar += renglon[contadorPosiciones]
                elif renglon[contadorPosiciones] == "<" or renglon[contadorPosiciones] == ">":
                    banderaEstado = 5
                    cadenaAuxiliar += renglon[contadorPosiciones]
                elif renglon[contadorPosiciones] == "|":
                    banderaEstado = 6
                    cadenaAuxiliar += renglon[contadorPosiciones]
                elif renglon[contadorPosiciones] == "&":
                    banderaEstado = 7
                    cadenaAuxiliar += renglon[contadorPosiciones]
                elif renglon[contadorPosiciones] == "!":
                    banderaEstado = 8
                    cadenaAuxiliar += renglon[contadorPosiciones]
                elif renglon[contadorPosiciones] == "=":
                    banderaEstado = 9
                    cadenaAuxiliar += renglon[contadorPosiciones]
                elif renglon[contadorPosiciones] == "+" or renglon[contadorPosiciones] == "-":
                    listaResultante.append(objeto(5, "OPsuma", renglon[contadorPosiciones]))
                elif renglon[contadorPosiciones] == ";":
                    listaResultante.append(objeto(12, ";", renglon[contadorPosiciones]))
                elif renglon[contadorPosiciones] == ",":
                    listaResultante.append(objeto(13, ",", renglon[contadorPosiciones]))
                elif renglon[contadorPosiciones] == "(":
                    listaResultante.append(objeto(14, "(", renglon[contadorPosiciones]))
                elif renglon[contadorPosiciones] == ")":
                    listaResultante.append(objeto(15, ")", renglon[contadorPosiciones]))
                elif renglon[contadorPosiciones] == "{":
                    listaResultante.append(objeto(16, "{", renglon[contadorPosiciones]))
                elif renglon[contadorPosiciones] == "}":
                    listaResultante.append(objeto(17, "}", renglon[contadorPosiciones]))
                else:
                    pass
            elif banderaEstado == 1:
                if renglon[contadorPosiciones].isalpha() or renglon[contadorPosiciones].isdigit():
                    cadenaAuxiliar += renglon[contadorPosiciones]
                else:
                    if cadenaAuxiliar == "int" or cadenaAuxiliar == "float" or cadenaAuxiliar == "void":
                        listaResultante.append(objeto(4, "Tipo", cadenaAuxiliar))
                    elif cadenaAuxiliar == "if":
                        listaResultante.append(objeto(19, "if", cadenaAuxiliar))
                    elif cadenaAuxiliar == "while":
                        listaResultante.append(objeto(20, "while", cadenaAuxiliar))
                    elif cadenaAuxiliar == "return":
                        listaResultante.append(objeto(21, "return", cadenaAuxiliar))
                    elif cadenaAuxiliar == "else":
                        listaResultante.append(objeto(22, "else", cadenaAuxiliar))
                    else:
                        listaResultante.append(objeto(0, "Identificador", cadenaAuxiliar))
                    contadorPosiciones -= 1
                    cadenaAuxiliar = ""
                    banderaEstado = 0
            elif banderaEstado == 2:
                if renglon[contadorPosiciones].isdigit():
                    cadenaAuxiliar += renglon[contadorPosiciones]
                elif renglon[contadorPosiciones] == ".":
                    cadenaAuxiliar += renglon[contadorPosiciones]
                    banderaEstado = 3
                else:
                    listaResultante.append(objeto(1, "Real", cadenaAuxiliar))
                    contadorPosiciones -= 1
                    cadenaAuxiliar = ""
                    banderaEstado = 0
            elif banderaEstado == 3:
                if renglon[contadorPosiciones].isdigit():
                    cadenaAuxiliar += renglon[contadorPosiciones]
                else:
                    listaResultante.append(objeto(2, "flotante", cadenaAuxiliar))
                    contadorPosiciones -= 1
                    cadenaAuxiliar = ""
                    banderaEstado = 0
            elif banderaEstado == 4:
                if renglon[contadorPosiciones] == "\"" or renglon[contadorPosiciones] == "\'":
                    listaResultante.append(3, "Cadena", cadenaAuxiliar)
                    banderaEstado = 0
                    cadenaAuxiliar = ""
                else:
                    cadenaAuxiliar += renglon[contadorPosiciones]
            elif banderaEstado == 5:
                if renglon[contadorPosiciones] == "=":
                    cadenaAuxiliar += renglon[contadorPosiciones]
                else:
                    contadorPosiciones -= 1
                listaResultante.append(7, "OpRelac", cadenaAuxiliar)
                cadenaAuxiliar = ""
                banderaEstado = 0
            elif banderaEstado == 6:
                if renglon[contadorPosiciones] == "|":
                    cadenaAuxiliar += renglon[contadorPosiciones]
                    listaResultante.append(8, "OpOr", cadenaAuxiliar)
                    cadenaAuxiliar = ""
                    banderaEstado = 0
                else:
                    raise ValueError("OpOrError")
            elif banderaEstado == 7:
                if renglon[contadorPosiciones] == "&":
                    cadenaAuxiliar += renglon[contadorPosiciones]
                    listaResultante.append(9, "OpAnd", cadenaAuxiliar)
                    cadenaAuxiliar = ""
                    banderaEstado = 0
                else:
                    raise ValueError("OpAndError")
            elif banderaEstado == 8:
                if renglon[contadorPosiciones] == "=":
                    cadenaAuxiliar += renglon[contadorPosiciones]
                    listaResultante.append(11, "OpIgualdad", cadenaAuxiliar)
                else:
                    contadorPosiciones -= 1
                    listaResultante.append(10, "OpNot", cadenaAuxiliar)
                cadenaAuxiliar = ""
                banderaEstado = 0
            elif banderaEstado == 9:
                if renglon[contadorPosiciones] == "=":
                    cadenaAuxiliar += renglon[contadorPosiciones]
                    listaResultante.append(objeto(11, "OpIgualdad", cadenaAuxiliar))
                else:
                    contadorPosiciones -= 1
                    listaResultante.append(objeto(18, "=", cadenaAuxiliar))
                cadenaAuxiliar = ""
                banderaEstado = 0
            contadorPosiciones += 1
            # Para no saltar ningun elemento, verifica si la bandera no continua en uso.
            if contadorPosiciones == len(renglon):
                if banderaEstado == 1:
                    if cadenaAuxiliar == "int" or cadenaAuxiliar == "float" or cadenaAuxiliar == "void":
                        listaResultante.append(objeto(4, "Tipo", cadenaAuxiliar))
                    elif cadenaAuxiliar == "if":
                        listaResultante.append(objeto(19, "if", cadenaAuxiliar))
                    elif cadenaAuxiliar == "while":
                        listaResultante.append(objeto(20, "while", cadenaAuxiliar))
                    elif cadenaAuxiliar == "return":
                        listaResultante.append(objeto(21, "return", cadenaAuxiliar))
                    elif cadenaAuxiliar == "else":
                        listaResultante.append(objeto(22, "else", cadenaAuxiliar))
                    else:
                        listaResultante.append(objeto(0, "Identificador", cadenaAuxiliar))
                elif banderaEstado == 2:
                    listaResultante.append(objeto(1, "Entero", cadenaAuxiliar))
                elif banderaEstado == 3:
                    listaResultante.append(objeto(2, "Real", cadenaAuxiliar))
                elif banderaEstado == 4:
                    if renglon[contadorPosiciones] == "\"" or renglon[contadorPosiciones] == "\'":
                        listaResultante.append(objeto(3, "Cadena", cadenaAuxiliar))
                    else:
                        raise ValueError("CadenaInvalida")

    return listaResultante


def mostrarArbol(nivel, arbol, cadena):
    if type(arbol) != list and type(arbol) != str:
        cadena.append(("\t" * nivel) + arbol.simbolo + "\n")
        mostrarArbol(nivel + 1, arbol.contenido, cadena)
    else:
        for rama in arbol:
            cadena.append(("\t" * nivel) + rama.simbolo + "\n")
            if type(rama.contenido) != str:
                mostrarArbol(nivel + 1, rama.contenido, cadena)


if __name__ == '__main__':
    try:
        arbol = []
        # AnalizadorLexico (Analiza y escribe en archivo)
        lista = analizadorLexico(separarRenglones())
        lista.append(objeto(23, "$", "$"))
        anLeToArchivo(lista)
        # AnalizadorSintactico (Analiza y escribe arbol en archivo)
        mostrarArbol(0, analizadorSintactico(lista)[1], arbol)
        arSiToArchivo(arbol)
    except ValueError as e:
        print(e)
