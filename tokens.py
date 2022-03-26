class objeto:
    def __init__(self, tipo, simbolo, contenido):
        self.tipo = tipo
        self.simbolo = simbolo
        self.contenido = contenido

    def __str__(self):
        return f"Contenido: {self.contenido} Simbolo: {self.simbolo} Tipo: {self.tipo}"


class objetoArbol:
    def __init__(self, tipo, simbolo, contenido):
        self.tipo = tipo
        self.simbolo = simbolo
        self.contenido = contenido

    def __str__(self):
        cadena = "Tipo: " + str(self.tipo) + " Simbolo: " + self.simbolo
        for cosas in self.contenido:
            cadena += cosas
        return cadena


class programa(objetoArbol):
    def __init__(self, tipo, simbolo, contenido):
        objetoArbol.__init__(self, tipo, simbolo, contenido)


class definiciones(objetoArbol):
    def __init__(self, tipo, simbolo, contenido):
        objetoArbol.__init__(self, tipo, simbolo, contenido)


class definicion(objetoArbol):
    def __init__(self, tipo, simbolo, contenido):
        objetoArbol.__init__(self, tipo, simbolo, contenido)


class defVar(objetoArbol):
    def __init__(self, tipo, simbolo, contenido):
        objetoArbol.__init__(self, tipo, simbolo, contenido)


class listaVar(objetoArbol):
    def __init__(self, tipo, simbolo, contenido):
        objetoArbol.__init__(self, tipo, simbolo, contenido)


class defFunc(objetoArbol):
    def __init__(self, tipo, simbolo, contenido):
        objetoArbol.__init__(self, tipo, simbolo, contenido)


class parametros(objetoArbol):
    def __init__(self, tipo, simbolo, contenido):
        objetoArbol.__init__(self, tipo, simbolo, contenido)


class listaParam(objetoArbol):
    def __init__(self, tipo, simbolo, contenido):
        objetoArbol.__init__(self, tipo, simbolo, contenido)


class bloqFunc(objetoArbol):
    def __init__(self, tipo, simbolo, contenido):
        objetoArbol.__init__(self, tipo, simbolo, contenido)


class defLocales(objetoArbol):
    def __init__(self, tipo, simbolo, contenido):
        objetoArbol.__init__(self, tipo, simbolo, contenido)


class defLocal(objetoArbol):
    def __init__(self, tipo, simbolo, contenido):
        objetoArbol.__init__(self, tipo, simbolo, contenido)


class sentencias(objetoArbol):
    def __init__(self, tipo, simbolo, contenido):
        objetoArbol.__init__(self, tipo, simbolo, contenido)


class sentencia(objetoArbol):
    def __init__(self, tipo, simbolo, contenido):
        objetoArbol.__init__(self, tipo, simbolo, contenido)


class otro(objetoArbol):
    def __init__(self, tipo, simbolo, contenido):
        objetoArbol.__init__(self, tipo, simbolo, contenido)


class bloque(objetoArbol):
    def __init__(self, tipo, simbolo, contenido):
        objetoArbol.__init__(self, tipo, simbolo, contenido)


class valorRegreso(objetoArbol):
    def __init__(self, tipo, simbolo, contenido):
        objetoArbol.__init__(self, tipo, simbolo, contenido)


class argumentos(objetoArbol):
    def __init__(self, tipo, simbolo, contenido):
        objetoArbol.__init__(self, tipo, simbolo, contenido)


class listaArgumentos(objetoArbol):
    def __init__(self, tipo, simbolo, contenido):
        objetoArbol.__init__(self, tipo, simbolo, contenido)


class termino(objetoArbol):
    def __init__(self, tipo, simbolo, contenido):
        objetoArbol.__init__(self, tipo, simbolo, contenido)


class llamadaFunc(objetoArbol):
    def __init__(self, tipo, simbolo, contenido):
        objetoArbol.__init__(self, tipo, simbolo, contenido)


class sentenciaBloque(objetoArbol):
    def __init__(self, tipo, simbolo, contenido):
        objetoArbol.__init__(self, tipo, simbolo, contenido)


class expresion(objetoArbol):
    def __init__(self, tipo, simbolo, contenido):
        objetoArbol.__init__(self, tipo, simbolo, contenido)
