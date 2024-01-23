# Practica 1 de recuperacion de la informacion.

## main.py

### Funcion (cargar_contenido_seleccionado)

```python
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
```

Ahora, explicaré cada parte del código:

1. `def cargar_contenido_seleccionado(event):`: Esta línea define una función llamada `cargar_contenido_seleccionado` que toma un evento como parámetro. Esta función probablemente se llame cuando se selecciona un elemento en la lista de archivos.

2. `seleccion = lista_archivos.curselection()`: Obtiene los índices de los elementos seleccionados en la lista de archivos. `lista_archivos` parece ser un widget de lista en una interfaz gráfica (GUI).

3. `if seleccion:`: Verifica si hay al menos un elemento seleccionado. Si la lista `seleccion` no está vacía, continúa con el siguiente bloque de código.

4. `indice_seleccionado = seleccion[0]`: Obtiene el primer índice seleccionado de la lista. Parece asumir que solo hay un elemento seleccionado.

5. `nombre_archivo = archivos[indice_seleccionado]`: Obtiene el nombre del archivo correspondiente al índice seleccionado.

6. `contenido_archivo = contenidos[indice_seleccionado]`: Obtiene el contenido del archivo correspondiente al índice seleccionado.

7. `hipervinculo_archivo = hipervinculos[indice_seleccionado]`: Obtiene el hipervínculo del archivo correspondiente al índice seleccionado.

8. `texto_contenido.delete(1.0, tk.END)`: Borra el contenido existente en un widget de texto llamado `texto_contenido`. `tk.END` indica el final del texto.

9. `texto_contenido.insert(tk.END, contenido_archivo)`: Inserta el contenido del archivo seleccionado en el widget de texto.

10. `cargar_contenido_seleccionado.hipervinculo_actual = hipervinculo_archivo`: Almacena el hipervínculo en una variable global `hipervinculo_actual` asociada a la función `cargar_contenido_seleccionado`.


### Funcion (abrir_hipervinculo)

```python
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
```

Ahora, desglosemos cada parte:

1. `if hasattr(cargar_contenido_seleccionado, 'hipervinculo_actual'):`
   - Utiliza la función `hasattr` para verificar si la variable global `hipervinculo_actual` está definida en la función `cargar_contenido_seleccionado`.

2. `hipervinculo = cargar_contenido_seleccionado.hipervinculo_actual`
   - Si la variable está definida, obtiene el valor de `hipervinculo_actual` almacenado en la función `cargar_contenido_seleccionado`.

3. `sistema_operativo = platform.system()`
   - Utiliza la biblioteca `platform` para obtener el nombre del sistema operativo en el que se está ejecutando la aplicación.

4. Bloque `if sistema_operativo == 'Windows':`
   - Verifica si el sistema operativo es Windows y, en caso afirmativo, utiliza `os.startfile(hipervinculo)` para abrir el archivo con el programa asociado.

5. Bloque `elif sistema_operativo == 'Linux':`
   - Verifica si el sistema operativo es Linux y, en caso afirmativo, utiliza `subprocess.Popen(['xdg-open', hipervinculo], ...)`. Esto abre el visor predeterminado (`xdg-open`) en segundo plano.

6. Bloque `elif sistema_operativo == 'Darwin':`
   - Verifica si el sistema operativo es macOS y, en caso afirmativo, utiliza `subprocess.Popen(['open', hipervinculo], ...)`. Esto abre el visor predeterminado (`open`) en segundo plano.

En resumen, esta función está diseñada para abrir un hipervínculo asociado a un archivo en función del sistema operativo en el que se está ejecutando la aplicación, utilizando las herramientas específicas de cada sistema operativo (por ejemplo, `os.startfile` en Windows, `xdg-open` en Linux, `open` en macOS).


### Funcion (if __name__ == "__main__":)

```python
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
    ventana.title("Visor de Archivos")

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
```

Explicación detallada:

1. `if __name__ == "__main__":`
   - Esta línea verifica si el script se está ejecutando directamente como un programa, no siendo importado como un módulo en otro script. Es una convención de Python para la ejecución de código específico al script principal.

2. `carpeta_archivos = "./input/"`
   - Establece la ruta de la carpeta que contiene los archivos.

3. `hipervinculos, contenidos_leidos = tarea_1.main(carpeta_archivos)`
   - Llama a la función `main` del módulo `tarea_1` para obtener los hipervínculos y contenidos de los archivos en la carpeta especificada.

4. `archivos = os.listdir(carpeta_archivos)`
   - Obtiene la lista de nombres de archivos en la carpeta especificada.

5. `contenidos = contenidos_leidos`
   - Almacena los contenidos leídos en una variable para su posterior uso.

6. `max_width = max(map(len, archivos))`
   - Calcula el ancho máximo basado en la longitud del nombre de archivo más largo.

7. `ventana = tk.Tk()`
   - Crea una ventana principal utilizando la clase `Tk` de la biblioteca Tkinter.

8. `ventana.title("Visor de Archivos")`
   - Establece el título de la ventana.

9. Creación y configuración de la `lista_archivos`:
   - `lista_archivos = tk.Listbox(ventana, selectmode=tk.SINGLE, width=max_width + 2)`: Crea una lista (widget `Listbox`) para mostrar los nombres de los archivos.
   - `lista_archivos.insert(tk.END, archivo)`: Inserta cada nombre de archivo en la lista.
   - `lista_archivos.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)`: Coloca la lista en el lado izquierdo de la ventana.

10. `lista_archivos.bind('<<ListboxSelect>>', cargar_contenido_seleccionado)`: Asocia la función `cargar_contenido_seleccionado` al evento de selección en la lista.

11. Creación y configuración del botón `boton_abrir_hipervinculo`:
   - `boton_abrir_hipervinculo = tk.Button(ventana, text="Abrir Hipervínculo", command=abrir_hipervinculo)`: Crea un botón con un texto y una función asociada.
   - `boton_abrir_hipervinculo.pack(pady=10)`: Coloca el botón debajo de la lista con un pequeño espacio.

12. Creación y configuración de la caja de texto `texto_contenido`:
   - `texto_contenido = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=40, height=10)`: Crea una caja de texto con scrollbar.
   - `texto_contenido.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)`: Coloca la caja de texto en el lado izquierdo de la ventana y permite que se expanda.

13. `ventana.mainloop()`: Inicia el bucle principal de la interfaz gráfica, lo que permite que la ventana sea interactiva y responda a eventos del usuario.

## tarea_1.py

### Funcion (leer_archivo)

```python
def leer_archivo(ruta_archivo):
    # Obtener la ruta y la extensión del archivo
    ruta, extension = os.path.splitext(ruta_archivo)

    # Verificar si la extensión es un archivo PDF
    if extension.lower() == ".pdf":
        # Si es PDF, abrir el archivo y leer el texto de cada página
        with open(ruta_archivo, 'rb') as file:
            documento_pdf = fitz.open(file)
            texto = ""
            for pagina_num in range(documento_pdf.page_count):
                pagina = documento_pdf[pagina_num]
                texto += pagina.get_text()
        return texto

    # Verificar si la extensión es un archivo DOCX (Word)
    elif extension.lower() == ".docx":
        # Si es DOCX, abrir el archivo y leer el texto de cada párrafo
        doc = Document(ruta_archivo)
        texto = ""
        for paragraph in doc.paragraphs:
            texto += paragraph.text + "\n"
        return texto

    # Verificar si la extensión es un archivo de texto plano
    elif extension.lower() == ".txt":
        # Si es TXT, abrir el archivo y leer todo el contenido
        with open(ruta_archivo, 'r', encoding='utf-8') as file:
            return file.read()

    # Si la extensión no es compatible con el manejo de archivos, retornar un mensaje de error
    else:
        return f"Formato no compatible para {ruta_archivo}"
```

Ahora, desglosemos cada parte de la función:

1. `ruta, extension = os.path.splitext(ruta_archivo)`: Divide la ruta del archivo en la ruta y la extensión. Esto se hace utilizando la función `os.path.splitext`.

2. Bloque `if extension.lower() == ".pdf":`
   - Verifica si la extensión del archivo es ".pdf".
   - Si es así, abre el archivo PDF utilizando la biblioteca `PyMuPDF` (anteriormente conocida como Fitz) y recorre cada página para extraer el texto.

3. Bloque `elif extension.lower() == ".docx":`
   - Verifica si la extensión del archivo es ".docx".
   - Si es así, utiliza la biblioteca `python-docx` para abrir el archivo y recorre cada párrafo para extraer el texto.

4. Bloque `elif extension.lower() == ".txt":`
   - Verifica si la extensión del archivo es ".txt".
   - Si es así, abre el archivo de texto y lee todo su contenido.

5. Bloque `else:`
   - Si la extensión no es ninguna de las anteriores, devuelve un mensaje de error indicando que el formato no es compatible.

6. `return texto`: Devuelve el texto extraído del archivo, o en el caso de un formato no compatible, el mensaje de error.

La función `obtener_hipervinculo(ruta_archivo)` es bastante sencilla. Aquí está la explicación línea por línea:

### Funcion (obtener_hipervinculo)

```python
def obtener_hipervinculo(ruta_archivo):
    # Utiliza os.path.abspath para obtener la ruta absoluta del archivo
    # y devuelve la ruta formateada entre comillas dobles
    return f'"{os.path.abspath(ruta_archivo)}"'
```

Desglose:

1. `os.path.abspath(ruta_archivo)`: Utiliza la función `os.path.abspath` para obtener la ruta absoluta del archivo. Esto significa que obtendrás la ruta completa desde la raíz del sistema de archivos.

2. `f'"{os.path.abspath(ruta_archivo)}"'`: Formatea la ruta absoluta obtenida entre comillas dobles. Esto puede ser útil en situaciones donde se espera que el hipervínculo sea utilizado en un contexto donde se necesiten comillas dobles, como al abrir un archivo desde un programa externo. La función devuelve esta cadena formateada como resultado.

### Funcion (main)

```python
def main(carpeta_archivos):
    # Listas para almacenar hipervínculos y contenidos leídos
    hipervinculos = []
    contenidos_leidos = []

    # Iterar sobre los archivos en la carpeta especificada
    for nombre_archivo in os.listdir(carpeta_archivos):
        # Obtener la ruta completa del archivo
        ruta_archivo = os.path.join(carpeta_archivos, nombre_archivo)

        # Verificar si es un archivo
        if os.path.isfile(ruta_archivo):
            # Leer el contenido del archivo utilizando la función leer_archivo
            contenido_leido = leer_archivo(ruta_archivo)

            # Obtener el hipervínculo utilizando la función obtener_hipervinculo
            hipervinculo = obtener_hipervinculo(ruta_archivo)

            # Almacenar los resultados en las listas correspondientes
            hipervinculos.append(hipervinculo)
            contenidos_leidos.append(contenido_leido)

    # Devolver las listas de hipervínculos y contenidos leídos
    return hipervinculos, contenidos_leidos
```

Desglose:

1. `hipervinculos = []` y `contenidos_leidos = []`: Inicializa dos listas vacías para almacenar los hipervínculos y los contenidos leídos de los archivos.

2. `for nombre_archivo in os.listdir(carpeta_archivos):`: Itera sobre la lista de archivos en la carpeta especificada.

3. `ruta_archivo = os.path.join(carpeta_archivos, nombre_archivo)`: Combina la carpeta base con el nombre del archivo para obtener la ruta completa del archivo.

4. `if os.path.isfile(ruta_archivo):`: Verifica si el elemento en la carpeta es un archivo (no un directorio).

5. `contenido_leido = leer_archivo(ruta_archivo)`: Llama a la función `leer_archivo` para obtener el contenido del archivo.

6. `hipervinculo = obtener_hipervinculo(ruta_archivo)`: Llama a la función `obtener_hipervinculo` para obtener el hipervínculo del archivo.

7. `hipervinculos.append(hipervinculo)` y `contenidos_leidos.append(contenido_leido)`: Agrega el hipervínculo y el contenido leído a las listas correspondientes.

8. Después de iterar sobre todos los archivos, la función devuelve las listas de hipervínculos y contenidos leídos: `return hipervinculos, contenidos_leidos`.
