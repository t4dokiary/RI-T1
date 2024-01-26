import tkinter as tk
from tkinter import scrolledtext
import os
import platform
import subprocess
from src import tarea_1


def cargar_contenido_seleccionado(event):
    # Obtener los índices de los elementos seleccionados en la lista de archivos
    seleccion = lista_archivos.curselection()
    '''
    lista_archivos: Esto es el nombre del widget de lista del cual estás obteniendo las selecciones.

    curselection(): Este es un método del widget de lista que devuelve una tupla con las posiciones de los elementos seleccionados. En el contexto de una lista, la "posición" se refiere al índice del elemento en la lista.
    '''

    # Verificar si hay al menos un elemento seleccionado
    if seleccion:
        # Obtener el primer índice seleccionado
        indice_seleccionado = seleccion[0]

        # Obtener el nombre del archivo correspondiente al índice seleccionado
        # nombre_archivo = archivos[indice_seleccionado]

        # Obtener el contenido del archivo correspondiente al índice seleccionado
        contenido_archivo = contenidos[indice_seleccionado]

        # Obtener el hipervínculo del archivo correspondiente al índice seleccionado
        hipervinculo_archivo = hipervinculos[indice_seleccionado]

        # Borrar el contenido existente en el widget de texto
        '''
        texto_contenido: Esto parece ser el nombre de un widget de texto en tu interfaz gráfica. Puede ser un objeto de la clase tk.Text de la biblioteca tkinter.

        delete(1.0, tk.END): Este es un método de los widgets de texto en tkinter que se utiliza para eliminar contenido dentro del widget de texto. Aquí está desglosado:

            delete: Este es el método que se utiliza para eliminar contenido en el widget de texto.

            (1.0, tk.END): Estos son los argumentos que indican qué parte del contenido se debe eliminar. En este caso, 1.0 significa la posición del carácter en la línea 1, columna 0 (el índice comienza desde 1, no desde 0) y tk.END significa hasta el final del widget de texto. Entonces, básicamente, se está eliminando todo el contenido del widget de texto.
        '''
        texto_contenido.delete(1.0, tk.END)

        # Insertar el nuevo contenido en el widget de texto
        '''
        texto_contenido: Este es el nombre de un widget de texto en tu interfaz gráfica. Al igual que en el ejemplo anterior, parece ser un objeto de la clase tk.Text de la biblioteca tkinter.

        insert(tk.END, contenido_archivo): Este es un método de los widgets de texto en tkinter que se utiliza para insertar contenido en el widget de texto. Aquí está desglosado:

            insert: Este es el método que se utiliza para insertar contenido en el widget de texto.

            (tk.END, contenido_archivo): Estos son los argumentos que indican dónde y qué contenido se debe insertar. En este caso, tk.END significa que el contenido se insertará al final del widget de texto, y contenido_archivo es el texto que se va a insertar.
        '''
        texto_contenido.insert(tk.END, contenido_archivo)

        # Almacenar el hipervínculo en una variable global
        cargar_contenido_seleccionado.hipervinculo_actual = hipervinculo_archivo


def abrir_hipervinculo():
    # Verifica si la variable global 'hipervinculo_actual' está definida en la función cargar_contenido_seleccionado
    if hasattr(cargar_contenido_seleccionado, 'hipervinculo_actual'):
        '''
        hasattr(): Esta función integrada en Python se utiliza para verificar si un objeto tiene un atributo específico. Toma dos argumentos: el objeto que se está verificando y el nombre del atributo que se está buscando.

        cargar_contenido_seleccionado: Este es el objeto que estás verificando.

        'hipervinculo_actual': Este es el nombre del atributo que estás buscando.
        '''
        # Obtiene el hipervínculo almacenado en la variable global
        hipervinculo = cargar_contenido_seleccionado.hipervinculo_actual

        # Obtiene el sistema operativo en el que se está ejecutando la aplicación
        sistema_operativo = platform.system()
        '''
        platform: Este es el módulo en Python que proporciona funciones para obtener información sobre la plataforma de ejecución, incluyendo el sistema operativo.

        system(): Este es un método del módulo platform que devuelve una cadena que representa el nombre del sistema operativo en el que se está ejecutando el script.

        sistema_operativo: Esto es una variable que almacena el nombre del sistema operativo.
        '''

        # Comprueba el sistema operativo y realiza acciones específicas para cada uno
        if sistema_operativo == 'Windows':
            # En Windows, utiliza 'os.startfile' para abrir el archivo con el programa asociado
            os.startfile(hipervinculo)
            '''
            os: Este es el módulo en Python que proporciona una interfaz para interactuar con el sistema operativo.

            startfile(): Este es un método del módulo os que se utiliza para abrir un archivo o un hipervínculo con la aplicación predeterminada asociada en sistemas operativos Windows.

            hipervinculo: Esto es la URL o la ubicación del archivo que se abrirá con la aplicación predeterminada.
            '''
        elif sistema_operativo == 'Linux':
            # En Linux, utiliza el visor predeterminado (xdg-open) en segundo plano
            subprocess.Popen(['xdg-open', hipervinculo], stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            '''
            subprocess: Este es el módulo en Python que proporciona funcionalidad para la ejecución de procesos externos.

            Popen(): Este es el constructor de la clase Popen en el módulo subprocess que se utiliza para iniciar un nuevo proceso.

            ['xdg-open', hipervinculo]: Esta es la lista que representa el comando y sus argumentos que se ejecutarán. En este caso, el comando es 'xdg-open', que es un comando utilizado en sistemas basados en Unix para abrir archivos o URL con la aplicación predeterminada asociada al tipo de archivo o URL. hipervinculo es la URL que se abrirá.

            stdout=subprocess.PIPE: Esto redirige la salida estándar del proceso hijo (si la hay) a una tubería, lo que permite capturarla si es necesario.

            stderr=subprocess.PIPE: Esto redirige la salida de error estándar del proceso hijo (si la hay) a una tubería, también para capturarla si es necesario.

            stdin=subprocess.PIPE: Esto redirige la entrada estándar del proceso hijo (si la hay) desde una tubería. Puede no ser necesario en este caso si el proceso no requiere entrada desde el usuario.
            '''
        elif sistema_operativo == 'Darwin':
            # En macOS, utiliza el visor predeterminado (open) en segundo plano
            subprocess.Popen(['open', hipervinculo], stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            '''
            subprocess: Este es el módulo en Python que proporciona funcionalidad para la ejecución de procesos externos.

            Popen(): Este es el constructor de la clase Popen en el módulo subprocess que se utiliza para iniciar un nuevo proceso.

            ['open', hipervinculo]: Esta es la lista que representa el comando y sus argumentos que se ejecutarán. En este caso, el comando es 'open', que es un comando de sistema operativo en sistemas basados en Unix para abrir un archivo o una URL, y hipervinculo es la URL que se abrirá.

            stdout=subprocess.PIPE: Esto redirige la salida estándar del proceso hijo (si la hay) a una tubería, lo que permite capturarla si es necesario.

            stderr=subprocess.PIPE: Esto redirige la salida de error estándar del proceso hijo (si la hay) a una tubería, también para capturarla si es necesario.

            stdin=subprocess.PIPE: Esto redirige la entrada estándar del proceso hijo (si la hay) desde una tubería. Puede no ser necesario en este caso si el proceso no requiere entrada desde el usuario.
            '''


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
    '''
    tk: Es el módulo tkinter en Python, que proporciona clases y funciones para la creación de interfaces gráficas de usuario.

    Tk(): Es la clase principal que representa la ventana principal de la interfaz gráfica. Cuando creas una instancia de esta clase, estás creando la ventana principal de tu aplicación.

    ventana: Es el nombre de la variable que utilizas para referenciar y manipular la ventana principal de la interfaz gráfica.
    '''
    ventana.title("Recuperacion de la Informacion")
    '''
    ventana: Este es el nombre de la variable que representa la ventana principal de la interfaz gráfica.

    title("Recuperacion de la Informacion"): Este método se utiliza para establecer el título de la ventana. El argumento que se pasa a title es el texto que aparecerá como título en la barra de título de la ventana.
    '''
    # Crear una lista con el nombre de los archivos
    # Agregar un pequeño espacio adicional
    lista_archivos = tk.Listbox(
        ventana, selectmode=tk.SINGLE, width=max_width + 2)
    '''
    lista_archivos: Este es el nombre de la variable que representa el widget de lista que estás creando. Puedes usar este nombre para referenciar y manipular la lista en tu programa.

    tk.Listbox: Esto crea un objeto de la clase Listbox de la biblioteca tkinter. Un Listbox es un widget que muestra una lista de elementos.

    ventana: Este es el nombre del objeto de la clase Tk que representa la ventana principal de tu interfaz gráfica. La lista se asocia con esta ventana.

    selectmode=tk.SINGLE: Este argumento configura el modo de selección de la lista. tk.SINGLE indica que solo se puede seleccionar un elemento a la vez. Otros modos de selección incluyen tk.BROWSE, tk.MULTIPLE, y tk.EXTENDED.

    width=max_width + 2: Este argumento establece el ancho del widget de lista. Parece que está configurado para ser un poco más ancho que la longitud máxima (max_width) de los elementos en la lista más 2 unidades adicionales.
    '''
    for archivo in archivos:
        lista_archivos.insert(tk.END, archivo)
        '''
        lista_archivos: Esto es el nombre del widget de lista en el que estás insertando un elemento.

        insert(): Este es el método que se utiliza para insertar elementos en un widget de lista.

        tk.END: Este es el índice en el que se insertará el nuevo elemento. tk.END significa que el nuevo elemento se insertará al final de la lista.

        archivo: Este es el contenido que se va a insertar en la lista. Puede ser cualquier tipo de información que desees mostrar en la lista. Puede ser un nombre de archivo, una cadena de texto, o cualquier otro objeto que desees mostrar en la lista.
        '''
    # Expand=False para mantener el ancho fijo
    lista_archivos.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)
    '''
    lista_archivos: Esto es el nombre del widget de lista que estamos gestionando.

    pack(): Este es un método de gestión de geometría en tkinter que se utiliza para organizar y mostrar widgets en la interfaz gráfica.

    side=tk.LEFT: Este argumento especifica el lado de la ventana en el que se colocará el widget de lista. En este caso, se coloca en el lado izquierdo (tk.LEFT) de la ventana.

    fill=tk.BOTH: Este argumento especifica cómo debe expandirse el widget para llenar el espacio disponible. tk.BOTH significa que el widget se expandirá tanto horizontal como verticalmente.

    expand=False: Este argumento indica si el widget debe expandirse para ocupar cualquier espacio adicional disponible. En este caso, expand=False significa que el widget no se expandirá.
    '''

    # Asociar la función cargar_contenido_seleccionado al evento de selección en la lista
    lista_archivos.bind('<<ListboxSelect>>', cargar_contenido_seleccionado)
    '''
    lista_archivos: Esto es el nombre del widget de lista al que estás asociando el evento.

    bind(): Este es el método que se utiliza para asociar eventos con funciones en tkinter.

    '<<ListboxSelect>>': Este es el evento que estás asociando. <<ListboxSelect>> es un evento que ocurre cuando un elemento en la lista es seleccionado.

    cargar_contenido_seleccionado: Este es el nombre de la función que se llamará cuando se dispare el evento de selección. Puedes definir esta función en tu código para realizar acciones específicas cuando un elemento de la lista es seleccionado.
    '''

    # Crear un botón para abrir el hipervínculo
    boton_abrir_hipervinculo = tk.Button(
        ventana, text="Abrir Hipervínculo", command=abrir_hipervinculo)
    '''
    boton_abrir_hipervinculo: Este es el nombre de la variable que representa el botón que estás creando. Puedes utilizar este nombre para referenciar y manipular el botón en tu programa.

    tk.Button: Esto crea un objeto de la clase Button de la biblioteca tkinter. Un botón es un elemento interactivo que los usuarios pueden hacer clic.

    ventana: Este es el nombre del objeto de la clase Tk que representa la ventana principal de tu interfaz gráfica. El botón se asocia con esta ventana.

    text="Abrir Hipervínculo": Este argumento establece el texto que se mostrará en el botón. En este caso, el texto es "Abrir Hipervínculo".

    command=abrir_hipervinculo: Este argumento establece la función que se llamará cuando se haga clic en el botón. En este caso, la función abrir_hipervinculo se asigna al evento de clic.
    '''
    # Agregar algún espacio entre el botón y la lista de archivos
    boton_abrir_hipervinculo.pack(pady=10)
    '''
    boton_abrir_hipervinculo: Este es el nombre del botón que estás empaquetando.

    pack(): Este es el método de gestión de geometría en tkinter que se utiliza para organizar y mostrar widgets en la interfaz gráfica.

    pady=10: Este argumento establece la cantidad de espacio vertical (en píxeles) que se debe agregar alrededor del botón. En este caso, se establece en 10 píxeles.
    '''

    # Crear una caja de texto (Text) con scrollbar
    texto_contenido = scrolledtext.ScrolledText(
        ventana, wrap=tk.WORD, width=40, height=10)
    '''
    texto_contenido: Esto es el nombre de la variable que representa el widget de texto con desplazamiento que estás creando. Puedes utilizar este nombre para referenciar y manipular el widget en tu programa.

    scrolledtext.ScrolledText: Esto crea un objeto de la clase ScrolledText del módulo scrolledtext de tkinter. Este widget de texto con desplazamiento incluye barras de desplazamiento automáticamente.

    ventana: Este es el nombre del objeto de la clase Tk que representa la ventana principal de tu interfaz gráfica. El widget de texto con desplazamiento se asocia con esta ventana.

    wrap=tk.WORD: Este argumento especifica cómo el texto debe envolverse dentro del widget. tk.WORD significa que el texto se envolverá solo en límites de palabra.

    width=40: Este argumento establece el ancho del widget de texto con desplazamiento en caracteres.

    height=10: Este argumento establece la altura del widget de texto con desplazamiento en líneas.
    '''
    texto_contenido.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    '''
    texto_contenido: Esto es el nombre del widget de texto con desplazamiento que estás empaquetando.

    pack(): Este es el método de gestión de geometría en tkinter que se utiliza para organizar y mostrar widgets en la interfaz gráfica.

    side=tk.LEFT: Este argumento especifica el lado de la ventana en el que se colocará el widget de texto con desplazamiento. En este caso, se coloca en el lado izquierdo (tk.LEFT) de la ventana.

    fill=tk.BOTH: Este argumento especifica cómo debe expandirse el widget para llenar el espacio disponible. tk.BOTH significa que el widget se expandirá tanto horizontal como verticalmente.

    expand=True: Este argumento indica si el widget debe expandirse para ocupar cualquier espacio adicional disponible. En este caso, expand=True significa que el widget se expandirá.
    '''

    # Iniciar el bucle principal de la interfaz gráfica
    ventana.mainloop()
    '''
    ventana: Esto es el nombre del objeto de la clase Tk que representa la ventana principal de tu interfaz gráfica.

    mainloop(): Este es el método que inicia el bucle principal de la interfaz gráfica. Este bucle está constantemente esperando eventos como clics de ratón, pulsaciones de teclas, etc. y responde a ellos ejecutando las funciones correspondientes.
    '''
