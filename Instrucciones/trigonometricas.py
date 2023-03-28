from Abstraccion.abstract import Expresion
from Instrucciones.aritmeticas import *
from math import *

class Trigonometrica(Expresion):

    def __init__(self, left, tipo, fila, columna):
        self.left = left
        self.tipo = tipo
        super().__init__(fila, columna)

    def operar(self, arbol):
        Dato = ''
        left_Value = ''
        if self.left != None:
            left_Value, Estado_left, Dato_left, Nodo_left = self.left.operar(arbol)
            Nodoleft = Lista_Nodos.pop(0)
            Dato_left += f'{Nodoleft}[label = "{left_Value}"]\n'


        if self.tipo.operar(arbol) == 'Seno':
            Nodo_Final = Lista_Nodos.pop(0)
            operacion = sin(left_Value)
            Dato_left += f'{Nodo_Final}[label = "Seno: {operacion}"]\n'
            Dato_left += f'{Nodo_Final}->{Nodoleft}\n'
            return operacion, True, Dato, Nodo_Final
        elif self.tipo.operar(arbol) == 'Coseno':
            Nodo_Final = Lista_Nodos.pop(0)
            operacion = cos(left_Value)
            Dato_left += f'{Nodo_Final}[label = "Coseno: {operacion}"]\n'
            Dato_left += f'{Nodo_Final}->{Nodoleft}\n'
            return operacion, True, Dato, Nodo_Final
        elif self.tipo.operar(arbol) == 'Tangente':
            Nodo_Final = Lista_Nodos.pop(0)
            operacion = tan(left_Value)
            Dato_left += f'{Nodo_Final}[label = "Tangente: {operacion}"]\n'
            Dato_left += f'{Nodo_Final}->{Nodoleft}\n'
            return operacion, True, Dato, Nodo_Final
        elif self.tipo.operar(arbol) == 'Inverso':
            Nodo_Final = Lista_Nodos.pop(0)
            operacion = (1/left_Value)
            Dato_left += f'{Nodo_Final}[label = "Inverso: {operacion}"]\n'
            Dato_left += f'{Nodo_Final}->{Nodoleft}\n'
            return operacion, True, Dato, Nodo_Final
        else:
            return None
        
    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()