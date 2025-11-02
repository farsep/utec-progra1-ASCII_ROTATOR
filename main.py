# La R antes de las comillas triples indica que es una cadena raw (cruda),
# lo que significa que los caracteres de escape se tratan literalmente.
# Esto es útil para el arte ASCII donde los caracteres como \n o \t no deben
# interpretarse como saltos de línea o tabulaciones.
art = r"""
                       .-'')
           ,.___  __.-'   /
          _;----''.._)_  (--...__
        ,'           `.__(       `-._
       '      __,....,_              \
      |    ,,'o    o | `.             \
       `. |    _'  _.'  /              |
      ,.- `>-'( )''    |               |
    ,'  _ /  ____,.--./                |
   |   / )")'         |               /
   `. ( ( (._         _._        __.-'
     `->..___`,-...--' /,--:'''''
      /      ``>/o\   //    `.
     /       .'/o /`-'|       \
 ___(      _/  `-'   ,'        \
|    `---,'---...._,'--.__     |\
| ,-----',       ,',' , _,`----' \
| |     \|       ('`-'-'  (`-.____`.
| |      `.       \        )\______)
| |        `-----'''------','op||
| |        `-,oobb.'ibbbbb: ,88||
| |         d"'''`Y8;"'''`PY8P_)|
| | -hrr-  `8b___od8boooood8P| ||
| |          Y8P"'' Y888PP' || ||
------------------------------------------------
"""

# FUNCION PARA DIVIDIR EL ARTE ASCII EN LINEAS
def split_lines(text):
    return text.splitlines()

# DEFINIMOS UNA NUEVA VARIABLE CON EL ARTE ASCII EN LINEAS
lines = split_lines(art)

# FUNCION PARA IMPRIMIR LAS LINEAS DEL ARTE ASCII
def print_lines(lines):
    for line in lines:
        print(line)

print_lines(lines)

'''
FUNCION PARA ROTAR 90 GRADOS EN SENTIDO HORARIO
THE ASCII ART
'''

def rotate_90_clockwise(lines):
    # Crear una nueva lista para las líneas rotadas
    new_lines = []

    # Determinar la longitud máxima de las líneas originales en base a la anchura inicial
    max_length = max(len(line) for line in lines)
    # Recorrer cada índice de carácter en las líneas originales
    for i in range(max_length):
        new_line = ''
        # Recorrer las líneas originales en orden inverso
        for line in reversed(lines):
            # Añadir el carácter correspondiente o un espacio si la línea es más corta
            if i < len(line):
                new_line += line[i]
            # Si la línea es más corta, añadir un espacio
            else:
                new_line += ' '
        # Añadir la nueva línea a la lista de líneas rotadas
        new_lines.append(new_line)
    return new_lines

# IMPRIMIR EL ARTE ASCII ROTADO 90 GRADOS EN SENTIDO HORARIO
print_lines(rotate_90_clockwise(lines))


