import os
import fitz  # PyMuPDF
from docx import Document


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


def obtener_hipervinculo(ruta_archivo):
    # Utiliza os.path.abspath para obtener la ruta absoluta del archivo
    # y devuelve la ruta formateada entre comillas dobles
    return f'"{os.path.abspath(ruta_archivo)}"'


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
