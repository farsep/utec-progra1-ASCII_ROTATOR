# 🎨 Generador y Manipulador de Arte ASCII

Una herramienta interactiva de línea de comandos (CLI) desarrollada por el **Grupo 5**. Este proyecto permite manipular, analizar y rotar arte ASCII existente, además de integrar capacidades de **Inteligencia Artificial Generativa** para crear nuevo arte ASCII basado en temáticas personalizadas utilizando los modelos más recientes de Google Gemini.

## ✨ Características Principales

  * **🔄 Motor de Rotación:** Algoritmos propios para rotar arte ASCII:
      * 90° Sentido Horario.
      * 90° Sentido Anti-horario.
      * 180° (Inversión completa).
  * **📊 Análisis de Datos:** Herramienta estadística para contar la frecuencia de caracteres utilizados en el dibujo.
  * **💾 Gestión de Archivos:**
      * Lectura de archivos `.txt` (con validación de ancho máximo de 50 caracteres para mantener el formato).
      * Guardado de las modificaciones realizadas en nuevos archivos dentro de la carpeta del proyecto.
  * **🤖 Generación con IA:** Integración con la API de Google (`gemini-3-pro-preview`) para generar arte ASCII único y navideño (o temático) basado en una solicitud ingresada por el usuario.

## 🚀 Requisitos e Instalación

### 1\. Prerrequisitos

Necesitas tener Python instalado (versión 3.10 o superior recomendada).

### 2\. Archivo de Dependencias

Asegúrate de crear un archivo llamado `requirements.txt` en la misma carpeta del script con el siguiente contenido:

google-genai

### 3\. Instalación

Abre tu terminal en la carpeta del proyecto y ejecuta:

pip install -r requirements.txt

-----

## 🔑 Configuración de la API Key

Para utilizar la **Opción 8 (Crear arte con IA)**, es necesario contar con una API Key de Google.

1.  Obtén tu clave gratuita en: [Google AI Studio](https://aistudio.google.com/app/apikey).
2.  **Importante:** No necesitas configurar variables de entorno complejas. El programa te solicitará que pegues tu clave directamente en la consola cuando elijas la opción de crear arte.

-----

## 🎮 Guía de Uso

Para iniciar el programa, ejecuta el archivo principal:

python main.py

### Menú Interactivo

El sistema desplegará las siguientes opciones:

1.  **Mostrar un ASCII ART:** Carga el arte por defecto (El Mago).
2.  **Rotar 90 grados en sentido horario:** Gira a la derecha.
3.  **Rotar 90 grados en sentido anti horario:** Gira a la izquierda.
4.  **Rotar 180 grados:** Voltea la imagen completamente (de cabeza).
5.  **Mostrar frecuencia de caracteres:** Muestra un conteo de cuántas veces aparece cada símbolo.
6.  **Leer arte ASCII desde un archivo:** Carga un archivo `.txt` externo.
      * *Nota:* El arte no debe superar los 50 caracteres de ancho.
7.  **Guardar la vista actual:** Guarda el resultado de tus rotaciones en un archivo nuevo.
8.  **Crear arte ASCII usando Gemini:**
      * El programa te pedirá tu **API KEY**.
      * Luego te pedirá un **personaje** (ej: "sonic", "goku").
      * La IA generará un dibujo nuevo y único para ti.
9.  **Salir:** Cierra el programa.

-----

## 🛠️ Solución de Problemas

  * **Error: `ModuleNotFoundError`**:
      * Causa: No has instalado las librerías necesarias.
      * Solución: Ejecuta `pip install -r requirements.txt`.
  * **Error: `Error: El arte ASCII en el archivo excede los 50 caracteres...`**:
      * Causa: Intentaste cargar un archivo de texto con líneas muy largas.
      * Solución: Usa archivos de arte más pequeños o edita el archivo `.txt` para acortar las líneas.
  * **Error en la Opción 8 (IA)**:
      * Si recibes un error de conexión o de modelo, verifica que tu API Key sea correcta y que tengas acceso a internet. El código utiliza el modelo `gemini-3-pro-preview` (o `gemini-2.0-flash-exp` dependiendo de la disponibilidad).

-----

## 📝 Créditos

Desarrollado con ❤️ por **GRUPO 5**.

  * **Curso:** Programación 1
  * **Tecnologías:** Python, Google GenAI SDK.
