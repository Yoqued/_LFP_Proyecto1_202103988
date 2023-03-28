from Abstraccion.abstract import Expresion

class Errores(Expresion):
    
    def __init__(self, lexema, fila, columna):
        self.lexema = lexema
        super().__init__(fila, columna)

    def operar(self, arbol):
        no = f'\t\t"No.": {arbol}\n'
        desc = '\t\t"Descipcion-Token": {\n'
        lex = f'\t\t\t"Lexema": {self.lexema}\n'
        tipo = '\t\t"Descipcion-Token": {\n'
        fila = f'\t\t\t"Fila": {self.fila}\n'
        columna = f'\t\t\t"Columna": {self.columna}\n'
        fin = '\t\t}\n'

        return '\t{\n' + no + desc + lex + tipo + fila + columna + fin + '\t}'
    
    def getColumna(self):
        return super().getColumna()
    
    def getFila(self):
        return super().getFila()