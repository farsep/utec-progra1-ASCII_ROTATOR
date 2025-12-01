import sys
import os

# --- STEP 1: CONFIGURATION (Vendoring) ---
# We calculate the path to the 'libs' folder relative to this script
current_dir = os.path.dirname(os.path.abspath(__file__))
libs_path = os.path.join(current_dir, 'libs')

# We add it to the start of the system path so Python finds these packages first
if libs_path not in sys.path:
    sys.path.insert(0, libs_path)

from google import genai


# from google import genai
#
# client = genai.Client()
#
# response = client.models.generate_content(
#     model="gemini-2.5-flash",
#     contents="Explain how AI works in a few words",
# )
#
# print(response.text)


#Importando las librerias para leer el archivo y mostrarlo en pantalla

#from pathlib import Path

#from twisted.mail.test.test_mail import empty

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

def reflect_the_image(lines):
    # Invertir la imagen es simplemente revertir el orden de las líneas
    # Solo porque no recuerdo si la profesora enseño el reversed entonces toca hacerlo manual
    new_lines = []
    for line in lines[::-1]:
        new_lines.append(line)
    return new_lines

# def rotate_180(lines):
#     # Rotar 180 grados es equivalente a rotar 90 grados dos veces
#     return rotate_90_clockwise(rotate_90_clockwise(lines))

def rotate_180(lines):
    # Rotar 180 grados recorriendo las líneas en orden inverso y cada línea invertida
    new_lines = []
    for line in reversed(lines):
        new_lines.append(line[::-1])
    return new_lines

def show_frecuency_of_characters(lines):
    frequency = {}
    for line in lines:
        for char in line:
            frequency[char] = frequency.get(char, 0) + 1
    return frequency

def read_file(filename, max_width: int = 50):
    # Leer el contenido de un archivo y devolverlo como una cadena
    # Si se produce un error, devuelve un mensaje de error
    #Verificar que el texto no tenga mas de 50 caracteres
    try:
        with open(filename, 'r') as f:
            readable_art = f.read()
    except Exception as e:
        return f"Error leyendo el archivo: {e}"

    readable_lines = split_lines(readable_art)
    for line in readable_lines:
        if len(line) > max_width:
            return "Error: El arte ASCII en el archivo excede los 50 caracteres por línea."
    return readable_lines

def reconstruct_art_from_lines(lines):
    return '\n'.join(str(l) for l in lines)

def write_file(filename, lines):
    try:
        with open(filename, 'w') as f:
            #merge the lines into a single string
            f.write(reconstruct_art_from_lines(lines))
        return f"Archivo '{filename}' guardado exitosamente en la carpeta Actual del proyecto."
    except Exception as e:
        return f"Error escribiendo el archivo: {e}"

def request_description_to_gemini(art_string):
    """
    Sends the ASCII art to Gemini for a description.
    """
    print("\n🤖 Consultando a Gemini...")

    try:
        # FIX 1: Initialize client empty (or with api_key="...")
        client = genai.Client(api_key="AIzaSyAmueVeMT1hhE_e7ZH0MV56iXXC6iYHy0g")

        # FIX 2: Use a valid model (2.5 doesn't exist yet, using 2.0-flash-exp)
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents="Describe the next ASCII art: \n" + art_string,
        )

        print("\n--- Respuesta de Gemini ---")
        # FIX 3: Fixed Indentation here
        print(response.text)
        print("---------------------------")

    except Exception as e:
        print(f"❌ Error: {e}")

def interactive_menu():
    """Simple looped menu (Spanish labels as requested)."""

    new_lines= None

    while True:
        print("\nMenu:")
        print("1. Mostrar un ASCII ART")
        print("2. Rotar 90 grados en sentido horario")
        print("3. Rotar 90 grados en sentido anti horario")
        print("4. Rotar 180 grados")
        print("5. Mostrar frecuencia de caracteres")
        print("6. Leer arte ASCII desde un archivo")
        print("7. Guardar la vista actual del arte ASCII en un archivo")
        print("8. Describir el arte ASCII usando Gemini-2.5-Flash")
        print("0. Salir")
        choice = input("Elige una opción: ").strip()

        if choice == '1':
            new_lines = lines
            print_lines(new_lines)
        elif choice == '2':
            new_lines = rotate_90_clockwise(new_lines)
            print_lines(new_lines)
        elif choice == '3':
            new_lines = rotate_90_counterclockwise(new_lines)
            print_lines(new_lines)
        # elif choice == '4':
        #     print_lines(reversed(lines))
        elif choice == '4':
            new_lines=rotate_180(new_lines)
            print_lines(new_lines)

        elif choice == '5':
            frequency = show_frecuency_of_characters(lines)
            print(frequency)

        elif choice == '6':
            filename = input("Ingresa el nombre del archivo: ").strip()
            new_lines=read_file(filename)
            print_lines(new_lines)

        elif choice == '7':
            filename = input("Ingresa el nombre del archivo para guardar: ").strip()
            result = write_file(filename, new_lines)
            print(result)

        elif choice == '8':
            request_description_to_gemini(reconstruct_art_from_lines(new_lines))

        elif choice in ('0', 'q', 'Q'):
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


interactive_menu()
