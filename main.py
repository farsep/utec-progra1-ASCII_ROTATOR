# La R antes de las comillas triples indica que es una cadena raw (cruda),
# lo que significa que los caracteres de escape se tratan literalmente.
# Esto es útil para el arte ASCII donde los caracteres como \n o \t no deben
# interpretarse como saltos de línea o tabulaciones.
art = r"""
                  _____
            _,---'     `-,_
            * `-,_         `-,
                  `-,@@@@@@@@@@                          _
                    @@@@@@@@@@@                    ((    ))
             (\_    ;;### ###;;                 {}  \\  //  {}
      _*__  (\_c\   ;; O ( O ;;                  \\---\/,-{=\    /=
    /\ \\ \  \ ( )  ;;, (_)  ;;                    ~~\\//~~ \\  //
    \ \ \\ \ @@@@@   ;;//~\\;;;                     (\_(\ {{=\\//=}
  ___\_\_\__| \  \ __ ;;;;;;;;_                      /  (o   \\//
 [==='`____`__ \  / /\ ;;;;; \ \_                    ) ) \  <`--'>
 |_  :~|~~~~~~|__/ /\ \       `, `-,_                ; (`~;  )  ('\
 |##-,_|@@@@@@|   \ \\/\       |_    @-,.   __    .&'   \ ;  ;  (/~
 |######-,_,__|_,-,\ *\ \=====@) `-,_@,-c).(_(,-'' \&....|   ;   :;
 |#########`-----,_`-,\\/_______\::::::-,_ ; )      |_ \ |_&-. ..(
 |####{}#######|!!!`-,__________):::::::::`-,; @)  .{ },-...\\&  `)
 |##{ __}}#####|!!!!!!!!!-,_    `-,::::::::::_//|  /(_)(     ||   ;
 |#{ }##{ }####|!!!!!!!!!!!!`-,_   \::::--,:/!!!/ /     \   //,--|:
 |#{ }###{}####|!!!!!!!!!!!!!!!!`---'!!!!!!!!!!| :   ^    ) ;~/  //
 |##{ }#{ }####|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!} \  / \   \; / _//
 |###{_~_}#####|!!!!!!!!!!!!!!!!!!!!!!!!!!!!,-:: /_/   \  \   C_/
 |#############|!!!!!!!!!!!!!!!!!!!!!!!!,-`X  (( //   __//
 |#############|!!!!!!!!!!!!!!!!!!!!,-`X  / \_,-'~   c__/
 |#############|!!!!!!!!!!!!!!!!,-`X  / \/,-`
 `;############|!!!!!!!!!!!!,-X   / \/,-`~
   X`-;########|!!!!!!!!,-'X / \ /,-'~
  /_\,-``-;####|!!!!!-'X  / \_,-'~
`-'         `-;|,-'X  / \',-'
                  /,-/,-'~
            ;    /,-'~
            `,_,-~  
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

# def rotate_90_counterclockwise(lines):
#     # Rotar 90 grados en sentido antihorario es equivalente a rotar 90 grados en sentido horario tres veces
#     return rotate_90_clockwise(rotate_90_clockwise(rotate_90_clockwise(lines)))


def rotate_90_counterclockwise(lines):
    # Crear una nueva lista para las líneas rotadas
    new_lines = []

    # Determinar la longitud máxima de las líneas originales en base a la anchura inicial
    max_length = max(len(line) for line in lines)
    # Recorrer cada índice de carácter en las líneas originales( de forma inversa al sentido horario)
    for i in range(max_length-1, -1, -1):
        new_line = ''
        # Recorrer las líneas originales en orden normal
        for line in lines:
            # Añadir el carácter correspondiente o un espacio si la línea es más corta
            if i < len(line):
                new_line += line[i]
            # Si la línea es más corta, añadir un espacio
            else:
                new_line += ' '
        # Añadir la nueva línea a la lista de líneas rotadas
        new_lines.append(new_line)
    return new_lines

def invert_the_image(lines):
    # Invertir la imagen es simplemente revertir el orden de las líneas
    # Solo porque no recuerdo si la profesora enseño el reversed entonces toca hacerlo manual
    new_lines = []
    for line in lines[::-1]:
        new_lines.append(line)
    return new_lines


def interactive_menu():
    """Simple looped menu (Spanish labels as requested)."""
    while True:
        print("\nMenu:")
        print("1. Mostrar un ASCII ART")
        print("2. Rotar 90 grados en sentido horario")
        print("3. Rotar 90 grados en sentido anti horario")
        print("4. Rotar 180 grados")
        print("0. Salir")
        choice = input("Elige una opción: ").strip()

        if choice == '1':
            print_lines(lines)
        elif choice == '2':
            print_lines(rotate_90_clockwise(lines))
        elif choice == '3':
            print_lines(rotate_90_counterclockwise(lines))
        # elif choice == '4':
        #     print_lines(reversed(lines))
        elif choice == '4':
            print_lines(invert_the_image(lines))
        elif choice in ('0', 'q', 'Q'):
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

interactive_menu()