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
    new_lines = []
    max_length = max(len(line) for line in lines)
    for i in range(max_length):
        new_line = ''
        for line in reversed(lines):
            if i < len(line):
                new_line += line[i]
            else:
                new_line += ' '
        new_lines.append(new_line)
    return new_lines


