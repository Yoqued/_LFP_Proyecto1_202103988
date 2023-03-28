from Abstraccion.abstract import Expresion

class Numero(Expresion):

    def __init__(self, valor,  fila, columna):
        self.valor = valor
        super().__init__(fila, columna)

    def operar(self, arbol):
        return self.valor, False, '', ''
    
    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()