from Instrucciones.aritmeticas import *
from Instrucciones.trigonometricas import *
from Abstraccion.lexema import *
from Abstraccion.numero import *
from Errores.errores import *
import os

Palabras_Reservadas = {
    'ROPERACION'        :'Operacion',
    'RVALOR1'           :'Valor1',
    'RVALOR2'           :'Valor2', 
    'RSUMA'             :'Suma',
    'RRESTA'            :'Resta',
    'RMULTIPLICACION'   :'Multiplicacion',
    'RDIVISION'         :'Division',
    'RPOTENCIA'         :'Potencia',
    'RRAIZ'             :'Raiz',
    'RINVERSO'          :'Inverso',
    'RSENO'             :'Seno',
    'RCOSENO'           :'Coseno',
    'RTANGENTE'         :'Tangente',
    'RMODULO'           :'Modulo',
    'RTEXTO'            :'Texto',
    'RCOLORFONDONODO'   :'Color-Fondo-Nodo',
    'RCOLORFUENTENODO'  :'Color-Fuente-Nodo',
    'RFORMADO'          :'Forma-Nodo',
    'COMA'              :',',
    'PUNTO'             :'.',
    'DPUNTOS'           :':',
    'CORI'              :'[',
    'CORD'              :']',
    'LLAVEI'            :'{',
    'LLAVED'            :'}'
}

lexemas = list(Palabras_Reservadas.values())

global n_linea
global n_columna
global instrucciones
global lista_lexema
global lista_errores
global lista_Adicional
global lista_Resultado

n_linea = 1
n_columna = 1
lista_lexema = []
instrucciones = []
lista_errores = []
lista_Adicional = []
lista_Resultado = []

def Instruccion(cadena):
    global n_linea
    global n_columna
    global lista_lexema
    global lista_errores
    global lista_Adicional
    lexema = ''
    puntero = 0

    while cadena:
        char = cadena[puntero]
        puntero += 1

        if char == '\"':
            lexema, cadena = Armar_Lexema(cadena[puntero:])
            if lexema and cadena:
                n_columna += 1
                
                l = Lexema(lexema, n_linea, n_columna)

                lista_lexema.append(l)
                lista_Adicional.append(l)
                n_columna += len(cadena) + 1
                puntero = 0    
        elif char.isdigit():
            token, cadena =  Armar_Numero(cadena)
            if token and cadena:
                n_columna += 1

                n = Numero(token, n_linea, n_columna)

                lista_lexema.append(n)
                lista_Adicional.append(n)
                n_columna += len(str(token)) + 1
                puntero = 0
        elif char == '[' or char == ']':
             
            c = Lexema(char, n_linea, n_columna)

            lista_lexema.append(c)
            lista_Adicional.append(c)
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1
        elif char == '\t':
            n_columna += 4
            cadena = cadena[4:]
            puntero = 0
        elif char == '\n':
            cadena = cadena[1:]
            puntero = 0
            n_linea += 1
            n_columna = 1
        elif char == ' ' or char == '\r' or char == '{' or char == '}' or char == ',' or char == '.' or char == ':':
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1
        else:
            lista_errores.append(Errores(char, n_linea, n_columna))
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1

def Armar_Lexema(cadena):
    global n_linea
    global n_columna
    global lista_lexema
    lexema = ''
    puntero = ''
    for char in cadena:
        puntero += char
        if char == '\"':
            return lexema, cadena[len(puntero):]
        else:
            lexema += char
    return None, None

def Armar_Numero(cadena):
    numero = ''
    puntero = ''
    Decimal = False
    for char in cadena:
        puntero += char
        if char == '.':
            Decimal = True
        if char == '"' or char == ' ' or char == '\t'  or char == '\n':
            if Decimal:
                return float(numero), cadena[len(puntero)-1:]
            else:
                return int(numero), cadena[len(puntero)-1:]
        else:
            numero += char
    return None, None

def operar():
    global lista_lexema
    global instrucciones

    operacion = ''
    n1 = ''
    n2 = ''
    while lista_lexema:
        lexema = lista_lexema.pop(0)
        if lexema.operar(None) == 'Operacion':
            operacion = lista_lexema.pop(0)
        elif lexema.operar(None) == 'Valor1':
            n1 = lista_lexema.pop(0)
            if n1.operar(None) == '[':
                n1 = operar()
        elif lexema.operar(None) == 'Valor2':
            n2 = lista_lexema.pop(0)
            if n2.operar(None) == '[':
                n2 = operar()

        if operacion and n1 and n2:
            return Aritmetica(n1, n2, operacion, f'Inicio: {operacion.getFila()}:{operacion.getColumna()}',f'Fin: {n2.getFila()}:{n2.getColumna()}')
        elif operacion and n1 and operacion.operar(None) == ('Seno' or 'Coseno' or 'Tangente' or 'Inverso'):
            return Trigonometrica(n1, operacion, f'Inicio: {operacion.getFila()}:{operacion.getColumna()}',f'Fin: {n1.getFila()}:{n1.getColumna()}')
    return None

def operar_():
    global instrucciones
    global lista_Resultado
    Da = ''
    while True:
        operacion = operar()
        if operacion:
            instrucciones.append(operacion)
        else:
            break
    
    for instruccion in instrucciones:
        res, vac1, dato, vac2 = instruccion.operar(None)
        lista_Resultado.append(res)
        print(res)
        Da = Da + dato
         
    instrucciones = []
    return instrucciones, lista_Resultado, Da

def getError():
    global lista_errores
    return lista_errores

def getErrores(self):
    lista_errores = getError()
    contador = 1

    archivo = open("Errores.txt", 'w')

    print('{')
    archivo.write('{\n')
    while lista_errores:
        error = lista_errores.pop(0)
        archivo.write(str(error.operar(contador)))
        print(error.operar(contador),',')
        archivo.write(' ,')
        archivo.write('\n')
        contador += 1
    archivo.write('}')
    print('}')
    archivo.close()

def Graficar(Dato):
    global lista_Adicional

    while lista_Adicional:
        token = lista_Adicional.pop(0)

        if token.operar(None) == 'Texto':
            titulo = lista_Adicional.pop(0)
        elif token.operar(None) == 'Color-Fondo-Nodo':
            color = lista_Adicional.pop(0)
        elif token.operar(None) == 'Color-Fuente-Nodo':
            fuente = lista_Adicional.pop(0)
        elif token.operar(None) == 'Forma-Nodo':
            forma = lista_Adicional.pop(0)
    
    Nodo = '''digraph{\n'''

    colorsito = color.operar(None).lower()

    if colorsito == 'amarillo' or colorsito == '#ffff00':
        Nodo += f'node[fillcolor = "yellow"'
    elif colorsito == 'rojo' or colorsito == '#ff0000':
        Nodo += f'node[fillcolor = "red"'
    elif colorsito == 'azul' or colorsito == '#0000FF':
        Nodo += f'node[fillcolor = "blue"'
    elif colorsito == 'rosado' or colorsito == '#FFC0CB':
        Nodo += f'node[fillcolor = "pink"'
    elif colorsito == 'anaranjado' or colorsito == '#FFA500':
        Nodo += f'node[fillcolor = "orange"'
    elif colorsito == 'verde' or colorsito == '#008000':
        Nodo += f'node[fillcolor = "green"'
    elif colorsito == 'cafe' or colorsito == '#A52A2A':
        Nodo += f'node[fillcolor = "brown"'
    elif colorsito == 'morado' or colorsito == '#800080':
        Nodo += f'node[fillcolor = "purple"'


    fuentesita = fuente.operar(None).lower()

    if fuentesita == 'amarillo' or fuentesita == '#ffff00':
        Nodo += f' fontcolor = "yellow"'
    elif fuentesita == 'rojo' or fuentesita == '#ff0000': 
        Nodo += f' fontcolor = "red"'
    elif fuentesita == 'azul' or fuentesita == '#0000FF': 
        Nodo += f' fontcolor = "azul"'
    elif fuentesita == 'rosado' or fuentesita == '#FFC0CB': 
        Nodo += f' fontcolor = "red"'
    elif fuentesita == 'anaranjado' or fuentesita == '#FFA500': 
        Nodo += f' fontcolor = "anaranjado"'
    elif fuentesita == 'verde' or fuentesita == '#008000': 
        Nodo += f' fontcolor = "verde"'
    elif fuentesita == 'cafe' or fuentesita == '#A52A2A': 
        Nodo += f' fontcolor = "cafe"'
    elif fuentesita == 'morado' or fuentesita == '#800080': 
        Nodo += f' fontcolor = "morado"'

    formita = forma.operar(None).lower()

    if formita == "cuadrado":
        Nodo += f' shape = "square"'
    if formita == "circulo":
        Nodo += f' shape = "circle"'
    if formita == "ovalo":
        Nodo += f' shape = "oval"'
    if formita == "triangulo":
        Nodo += f' shape = "triangle"'
    if formita == "rectangulo":
        Nodo += f' shape = "rectangle"'
    if formita == "rombo":
        Nodo += f' shape = "rhombus"'
    if formita == "estrella":
        Nodo += f' shape = "star"'
    if formita == "hexagono":
        Nodo += f' shape = "hexagon"'
    
    Nodo += " style = filled]\n"

    Nodo += Dato

    Nodo += '''\n}'''

    with open('Hola.dot', 'w') as f:
        f.write(Nodo)
    
    os.system('dot -Tpng Hola.dot -o Hola.png')





