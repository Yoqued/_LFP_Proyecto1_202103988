from Abstraccion.abstract import Expresion
global Lista_Nodos
global Dato 
Lista_Nodos = []
Dato = ''

def llenarlistaNodos():
    global Lista_Nodos
    Lista_Nodos.clear()
    for i in range(400):
        Lista_Nodos.append('nodo'+str(i))

class Aritmetica(Expresion):


    def __init__(self, left, right, tipo, fila, columna):
        self.left = left
        self.right = right
        self.tipo = tipo
        super().__init__(fila, columna)

    def operar(self, arbol):
        global Dato
        Estado_left = False
        Estado_right = False
        left_Value = ''
        right_Value = ''
        Dato = ''

        if self.left != None:
            left_Value, Estado_left, Dato_left, Nodo_left = self.left.operar(arbol)
            Dato = ''
        if self.right != None:
            right_Value, Estado_right, Dato_right, Nodo_right = self.right.operar(arbol)
            Dato = ''

        if self.tipo.operar(arbol) == 'Suma':
            if Estado_left is False  and Estado_right is False:
                Dato += Dato_left
                Dato += Dato_right
                Nodoleft = Lista_Nodos.pop(0)
                Nodoright = Lista_Nodos.pop(0)
                Dato += f'{Nodoleft}[label = "{left_Value}"]\n'
                Dato += f'{Nodoright}[label = "{right_Value}"\n]'
                Nodo_Final = Lista_Nodos.pop(0)
                Dato += f'{Nodo_Final}[label = "Suma: {left_Value + right_Value}"\n]'
                Dato += f'{Nodo_Final}->{Nodoleft}\n'
                Dato += f'{Nodo_Final}->{Nodoright} \n'
            elif Estado_left and Estado_right is False:
                Dato += Dato_left
                Dato += Dato_right
                Nodoright = Lista_Nodos.pop(0)
                Dato += f'{Nodoright}[label = "{right_Value}"]\n'
                Nodo_Final = Lista_Nodos.pop(0)
                Dato += f'{Nodo_Final}[label = "Suma: {left_Value + right_Value}"\n]'
                Dato += f'{Nodo_Final}->{Nodo_left}\n'
                Dato += f'{Nodo_Final}->{Nodoright} \n'
            elif Estado_right and Estado_left is False:
                Dato += Dato_left
                Nodoleft = Lista_Nodos.pop(0)
                Dato += f'{Nodoleft}[label = "{left_Value}"]\n'
                Nodo_Final = Lista_Nodos.pop(0)
                Dato += f'{Nodo_Final}[label = "Suma: {left_Value + right_Value}"\n]'
                Dato += Dato_right
                Dato += f'{Nodo_Final}->{Nodoleft}\n'
                Dato += f'{Nodo_Final}->{Nodo_right} \n'
            elif Estado_left and Estado_right:
                Dato += Dato_left
                Dato += Dato_right
                Nodo_Final = Lista_Nodos.pop(0)
                Dato += f'{Nodo_Final}[label = "Suma: {left_Value + right_Value}"\n]'
                Dato += f'{Nodo_Final}->{Nodo_left}\n'
                Dato += f'{Nodo_Final}->{Nodo_right} \n'

            return (left_Value + right_Value), True, Dato, Nodo_Final
        elif self.tipo.operar(arbol) == 'Resta':
            if Estado_left is False  and Estado_right is False:
                Dato += Dato_left
                Dato += Dato_right
                Nodoleft = Lista_Nodos.pop(0)
                Nodoright = Lista_Nodos.pop(0)
                Dato += f'{Nodoleft}[label = "{left_Value}"]\n'
                Dato += f'{Nodoright}[label = "{right_Value}"\n]'
                Nodo_Final = Lista_Nodos.pop(0)
                Dato += f'{Nodo_Final}[label = "Resta: {left_Value - right_Value}"\n]'
                Dato += f'{Nodo_Final}->{Nodoleft}\n'
                Dato += f'{Nodo_Final}->{Nodoright} \n'
            elif Estado_left and Estado_right is False:
                Dato += Dato_left
                Dato += Dato_right
                Nodoright = Lista_Nodos.pop(0)
                Dato += f'{Nodoright}[label = "{right_Value}"]\n'
                Nodo_Final = Lista_Nodos.pop(0)
                Dato += f'{Nodo_Final}[label = "Resta: {left_Value - right_Value}"\n]'
                Dato += f'{Nodo_Final}->{Nodo_left}\n'
                Dato += f'{Nodo_Final}->{Nodoright} \n'
            elif Estado_right and Estado_left is False:
                Dato += Dato_left
                Nodoleft = Lista_Nodos.pop(0)
                Dato += f'{Nodoleft}[label = "{left_Value}"]\n'
                Nodo_Final = Lista_Nodos.pop(0)
                Dato += f'{Nodo_Final}[label = "Resta: {left_Value - right_Value}"\n]'
                Dato += Dato_right
                Dato += f'{Nodo_Final}->{Nodoleft}\n'
                Dato += f'{Nodo_Final}->{Nodo_right} \n'
            elif Estado_left and Estado_right:
                Dato += Dato_left
                Dato += Dato_right
                Nodo_Final = Lista_Nodos.pop(0)
                Dato += f'{Nodo_Final}[label = "Resta: {left_Value - right_Value}"\n]'
                Dato += f'{Nodo_Final}->{Nodo_left}\n'
                Dato += f'{Nodo_Final}->{Nodo_right} \n'
            return (left_Value - right_Value), True, Dato, Nodo_Final
        elif self.tipo.operar(arbol) == 'Multiplicacion':
            if Estado_left is False  and Estado_right is False:
                Dato += Dato_left
                Dato += Dato_right
                Nodoleft = Lista_Nodos.pop(0)
                Nodoright = Lista_Nodos.pop(0)
                Dato += f'{Nodoleft}[label = "{left_Value}"]\n'
                Dato += f'{Nodoright}[label = "{right_Value}"\n]'
                Nodo_Final = Lista_Nodos.pop(0)
                Dato += f'{Nodo_Final}[label = "Multiplicacion: {left_Value * right_Value}"\n]'
                Dato += f'{Nodo_Final}->{Nodoleft}\n'
                Dato += f'{Nodo_Final}->{Nodoright} \n' 
            elif Estado_left and Estado_right is False:
                Dato += Dato_left
                Dato += Dato_right
                Nodoright = Lista_Nodos.pop(0)
                Dato += f'{Nodoright}[label = "{right_Value}"]\n'
                Nodo_Final = Lista_Nodos.pop(0)
                Dato += f'{Nodo_Final}[label = "Multiplicacion: {left_Value * right_Value}"\n]'
                Dato += f'{Nodo_Final}->{Nodo_left}\n'
                Dato += f'{Nodo_Final}->{Nodoright} \n'
            elif Estado_right and Estado_left is False:
                Dato += Dato_left
                Nodoleft = Lista_Nodos.pop(0)
                Dato += f'{Nodoleft}[label = "{left_Value}"]\n'
                Nodo_Final = Lista_Nodos.pop(0)
                Dato += f'{Nodo_Final}[label = "Multiplicacion: {left_Value * right_Value}"\n]'
                Dato += Dato_right
                Dato += f'{Nodo_Final}->{Nodoleft}\n'
                Dato += f'{Nodo_Final}->{Nodo_right} \n'
            elif Estado_left and Estado_right:
                Dato += Dato_left
                Dato += Dato_right
                Nodo_Final = Lista_Nodos.pop(0)
                Dato += f'{Nodo_Final}[label = "Multiplicacion: {left_Value * right_Value}"\n]'
                Dato += f'{Nodo_Final}->{Nodo_left}\n'
                Dato += f'{Nodo_Final}->{Nodo_right} \n'
            return (left_Value * right_Value), True, Dato, Nodo_Final
        elif self.tipo.operar(arbol) == 'Division':
            if Estado_left is False  and Estado_right is False:
                Dato += Dato_left
                Dato += Dato_right
                Nodoleft = Lista_Nodos.pop(0)
                Nodoright = Lista_Nodos.pop(0)
                Dato += f'{Nodoleft}[label = "{left_Value}"]\n'
                Dato += f'{Nodoright}[label = "{right_Value}"\n]'
                Nodo_Final = Lista_Nodos.pop(0)
                Dato += f'{Nodo_Final}[label = "Division: {left_Value / right_Value}"\n]'
                Dato += f'{Nodo_Final}->{Nodoleft}\n'
                Dato += f'{Nodo_Final}->{Nodoright} \n'
            elif Estado_left and Estado_right is False:
                Dato += Dato_left
                Dato += Dato_right
                Nodoright = Lista_Nodos.pop(0)
                Dato += f'{Nodoright}[label = "{right_Value}"]\n'
                Nodo_Final = Lista_Nodos.pop(0)
                Dato += f'{Nodo_Final}[label = "Division: {left_Value / right_Value}"\n]'
                Dato += f'{Nodo_Final}->{Nodo_left}\n'
                Dato += f'{Nodo_Final}->{Nodoright} \n'
            elif Estado_right and Estado_left is False:
                Dato += Dato_left
                Nodoleft = Lista_Nodos.pop(0)
                Dato += f'{Nodoleft}[label = "{left_Value}"]\n'
                Nodo_Final = Lista_Nodos.pop(0)
                Dato += f'{Nodo_Final}[label = "Division: {left_Value / right_Value}"\n]'
                Dato += Dato_right
                Dato += f'{Nodo_Final}->{Nodoleft}\n'
                Dato += f'{Nodo_Final}->{Nodo_right} \n'
            elif Estado_left and Estado_right:
                Dato += Dato_left
                Dato += Dato_right
                Nodo_Final = Lista_Nodos.pop(0)
                Dato += f'{Nodo_Final}[label = "Division: {left_Value / right_Value}"\n]'
                Dato += f'{Nodo_Final}->{Nodo_left}\n'
                Dato += f'{Nodo_Final}->{Nodo_right} \n'
            return (left_Value / right_Value), True, Dato, Nodo_Final
        elif self.tipo.operar(arbol) == 'Modulo':
            if Estado_left is False  and Estado_right is False:
                Dato += Dato_left
                Dato += Dato_right
                Nodoleft = Lista_Nodos.pop(0)
                Nodoright = Lista_Nodos.pop(0)
                Dato += f'{Nodoleft}[label = "{left_Value}"]\n'
                Dato += f'{Nodoright}[label = "{right_Value}"\n]'
                Nodo_Final = Lista_Nodos.pop(0)
                Dato += f'{Nodo_Final}[label = "Modulo: {left_Value % right_Value}"\n]'
                Dato += f'{Nodo_Final}->{Nodoleft}\n'
                Dato += f'{Nodo_Final}->{Nodoright} \n'
            elif Estado_left and Estado_right is False:
                Dato += Dato_left
                Dato += Dato_right
                Nodoright = Lista_Nodos.pop(0)
                Dato += f'{Nodoright}[label = "{right_Value}"]\n'
                Nodo_Final = Lista_Nodos.pop(0)
                Dato += f'{Nodo_Final}[label = "Modulo: {left_Value % right_Value}"\n]'
                Dato += f'{Nodo_Final}->{Nodo_left}\n'
                Dato += f'{Nodo_Final}->{Nodoright} \n'
            elif Estado_right and Estado_left is False:
                Dato += Dato_left
                Nodoleft = Lista_Nodos.pop(0)
                Dato += f'{Nodoleft}[label = "{left_Value}"]\n'
                Nodo_Final = Lista_Nodos.pop(0)
                Dato += f'{Nodo_Final}[label = "Modulo: {left_Value % right_Value}"\n]'
                Dato += Dato_right
                Dato += f'{Nodo_Final}->{Nodoleft}\n'
                Dato += f'{Nodo_Final}->{Nodo_right} \n'
            elif Estado_left and Estado_right:
                Dato += Dato_left
                Dato += Dato_right
                Nodo_Final = Lista_Nodos.pop(0)
                Dato += f'{Nodo_Final}[label = "Modulo: {left_Value % right_Value}"\n]'
                Dato += f'{Nodo_Final}->{Nodo_left}\n'
                Dato += f'{Nodo_Final}->{Nodo_right} \n'
            return (left_Value % right_Value), True, Dato, Nodo_Final
        elif self.tipo.operar(arbol) == 'Potencia':
            if Estado_left is False  and Estado_right is False:
                Dato += Dato_left
                Dato += Dato_right
                Nodoleft = Lista_Nodos.pop(0)
                Nodoright = Lista_Nodos.pop(0)
                Dato += f'{Nodoleft}[label = "{left_Value}"]\n'
                Dato += f'{Nodoright}[label = "{right_Value}"\n]'
                Nodo_Final = Lista_Nodos.pop(0)
                Dato += f'{Nodo_Final}[label = "Potencia: {left_Value ** right_Value}"\n]'
                Dato += f'{Nodo_Final}->{Nodoleft}\n'
                Dato += f'{Nodo_Final}->{Nodoright} \n'
            elif Estado_left and Estado_right is False:
                Dato += Dato_left
                Dato += Dato_right
                Nodoright = Lista_Nodos.pop(0)
                Dato += f'{Nodoright}[label = "{right_Value}"]\n'
                Nodo_Final = Lista_Nodos.pop(0)
                Dato += f'{Nodo_Final}[label = "Potencia: {left_Value ** right_Value}"\n]'
                Dato += f'{Nodo_Final}->{Nodo_left}\n'
                Dato += f'{Nodo_Final}->{Nodoright} \n'
            elif Estado_right and Estado_left is False:
                Dato += Dato_left
                Nodoleft = Lista_Nodos.pop(0)
                Dato += f'{Nodoleft}[label = "{left_Value}"]\n'
                Nodo_Final = Lista_Nodos.pop(0)
                Dato += f'{Nodo_Final}[label = "Potencia: {left_Value ** right_Value}"\n]'
                Dato += Dato_right
                Dato += f'{Nodo_Final}->{Nodoleft}\n'
                Dato += f'{Nodo_Final}->{Nodo_right} \n'
            elif Estado_left and Estado_right:
                Dato += Dato_left
                Dato += Dato_right
                Nodo_Final = Lista_Nodos.pop(0)
                Dato += f'{Nodo_Final}[label = "Potencia: {left_Value ** right_Value}"\n]'
                Dato += f'{Nodo_Final}->{Nodo_left}\n'
                Dato += f'{Nodo_Final}->{Nodo_right} \n'
            return (left_Value ** right_Value), True, Dato, Nodo_Final
        elif self.tipo.operar(arbol) == 'Raiz':
            if Estado_left is False  and Estado_right is False:
                Dato += Dato_left
                Dato += Dato_right
                Nodoleft = Lista_Nodos.pop(0)
                Nodoright = Lista_Nodos.pop(0)
                Dato += f'{Nodoleft}[label = "{left_Value}"]\n'
                Dato += f'{Nodoright}[label = "{right_Value}"\n]'
                Nodo_Final = Lista_Nodos.pop(0)
                Dato += f'{Nodo_Final}[label = "Raiz: {left_Value ** (1/right_Value)}"\n]'
                Dato += f'{Nodo_Final}->{Nodoleft}\n'
                Dato += f'{Nodo_Final}->{Nodoright} \n'
            elif Estado_left and Estado_right is False:
                Dato += Dato_left
                Dato += Dato_right
                Nodoright = Lista_Nodos.pop(0)
                Dato += f'{Nodoright}[label = "{right_Value}"]\n'
                Nodo_Final = Lista_Nodos.pop(0)
                Dato += f'{Nodo_Final}[label = "Raiz: {left_Value ** (1/right_Value)}"\n]'
                Dato += f'{Nodo_Final}->{Nodo_left}\n'
                Dato += f'{Nodo_Final}->{Nodoright} \n'
            elif Estado_right and Estado_left is False:
                Dato += Dato_left
                Nodoleft = Lista_Nodos.pop(0)
                Dato += f'{Nodoleft}[label = "{left_Value}"]\n'
                Nodo_Final = Lista_Nodos.pop(0)
                Dato += f'{Nodo_Final}[label = "Raiz: {left_Value ** (1/right_Value)}"\n]'
                Dato += Dato_right
                Dato += f'{Nodo_Final}->{Nodoleft}\n'
                Dato += f'{Nodo_Final}->{Nodo_right} \n'
            elif Estado_left and Estado_right:
                Dato += Dato_left
                Dato += Dato_right
                Nodo_Final = Lista_Nodos.pop(0)
                Dato += f'{Nodo_Final}[label = "Raiz: {left_Value ** (1/right_Value)}"\n]'
                Dato += f'{Nodo_Final}->{Nodo_left}\n'
                Dato += f'{Nodo_Final}->{Nodo_right} \n'
            return (left_Value ** (1/right_Value)), True, Dato, Nodo_Final
        else:
            return None
        
    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()