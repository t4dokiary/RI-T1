import tkinter as tk
from tkinter import scrolledtext
import os
import platform
import subprocess
from src import tarea_1


def cargar_contenido_seleccionado(event):
    # Obtener los índices de los elementos seleccionados en la lista de archivos
    seleccion = lista_archivos.curselection()

    # Verificar si hay al menos un elemento seleccionado
    if seleccion:
        # Obtener el primer índice seleccionado
        indice_seleccionado = seleccion[0]

        # Obtener el nombre del archivo correspondiente al índice seleccionado
        nombre_archivo = archivos[indice_seleccionado]

        # Obtener el contenido del archivo correspondiente al índice seleccionado
        contenido_archivo = contenidos[indice_seleccionado]

        # Obtener el hipervínculo del archivo correspondiente al índice seleccionado
        hipervinculo_archivo = hipervinculos[indice_seleccionado]

        # Borrar el contenido existente en el widget de texto
        texto_contenido.delete(1.0, tk.END)

        # Insertar el nuevo contenido en el widget de texto
        texto_contenido.insert(tk.END, contenido_archivo)

        # Almacenar el hipervínculo en una variable global
        cargar_contenido_seleccionado.hipervinculo_actual = hipervinculo_archivo


def abrir_hipervinculo():
    # Verifica si la variable global 'hipervinculo_actual' está definida en la función cargar_contenido_seleccionado
    if hasattr(cargar_contenido_seleccionado, 'hipervinculo_actual'):
        # Obtiene el hipervínculo almacenado en la variable global
        hipervinculo = cargar_contenido_seleccionado.hipervinculo_actual

        # Obtiene el sistema operativo en el que se está ejecutando la aplicación
        sistema_operativo = platform.system()

        # Comprueba el sistema operativo y realiza acciones específicas para cada uno
        if sistema_operativo == 'Windows':
            # En Windows, utiliza 'os.startfile' para abrir el archivo con el programa asociado
            os.startfile(hipervinculo)
        elif sistema_operativo == 'Linux':
            # En Linux, utiliza el visor predeterminado (xdg-open) en segundo plano
            subprocess.Popen(['xdg-open', hipervinculo], stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        elif sistema_operativo == 'Darwin':
            # En macOS, utiliza el visor predeterminado (open) en segundo plano
            subprocess.Popen(['open', hipervinculo], stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, stdin=subprocess.PIPE)


if __name__ == "__main__":
    # Carpeta que contiene los archivos
    carpeta_archivos = "./input/"

    # Obtener hipervínculos y contenidos leídos usando la función main
    hipervinculos, contenidos_leidos = tarea_1.main(carpeta_archivos)

    # Listas para almacenar nombres de archivos y contenidos
    archivos = os.listdir(carpeta_archivos)
    contenidos = contenidos_leidos

    # Calcular el ancho máximo basado en la longitud del string más largo
    max_width = max(map(len, archivos))

    # Crear la interfaz gráfica
    ventana = tk.Tk()
    ventana.title("Recuperacion de la Informacion")

    # Crear una lista con el nombre de los archivos
    # Agregar un pequeño espacio adicional
    lista_archivos = tk.Listbox(
        ventana, selectmode=tk.SINGLE, width=max_width + 2)
    for archivo in archivos:
        lista_archivos.insert(tk.END, archivo)
    # Expand=False para mantener el ancho fijo
    lista_archivos.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)

    # Asociar la función cargar_contenido_seleccionado al evento de selección en la lista
    lista_archivos.bind('<<ListboxSelect>>', cargar_contenido_seleccionado)

    # Crear un botón para abrir el hipervínculo
    boton_abrir_hipervinculo = tk.Button(
        ventana, text="Abrir Hipervínculo", command=abrir_hipervinculo)
    # Agregar algún espacio entre el botón y la lista de archivos
    boton_abrir_hipervinculo.pack(pady=10)

    # Crear una caja de texto (Text) con scrollbar
    texto_contenido = scrolledtext.ScrolledText(
        ventana, wrap=tk.WORD, width=40, height=10)
    texto_contenido.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Iniciar el bucle principal de la interfaz gráfica
    ventana.mainloop()
