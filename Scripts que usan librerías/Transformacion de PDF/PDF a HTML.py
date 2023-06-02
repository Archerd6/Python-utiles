import aspose.words as aw

def convert_pdf_to_html(input_file, output_file):
    # Cargar el archivo PDF
    doc = aw.Document(input_file)

    # Crear opciones de guardado en formato HTML
    save_options = aw.saving.HtmlSaveOptions()

    # Guardar el documento en formato HTML
    doc.save(output_file, save_options)

# Rutas de los archivos de entrada y salida
import pathlib
pdf_path = str(pathlib.Path(__file__).parent.resolve()) +'\\1.pdf'
html_path = str(pathlib.Path(__file__).parent.resolve()) +'\\1.html'

# Llamar a la función de conversión
convert_pdf_to_html(pdf_path, html_path)



import shutil
import os

# Ruta de la carpeta "HTML"
carpeta_html = str(pathlib.Path(__file__).parent.resolve()) +'\\HTML'
# Crear la carpeta de salida si no existe
os.makedirs(carpeta_html, exist_ok=True)

# Mover archivos de diferentes formatos a la carpeta "HTML"
ruta_archivos = str(pathlib.Path(__file__).parent.resolve())

for archivo in os.listdir(ruta_archivos):
    # Construir la ruta completa del archivo
    ruta_completa = os.path.join(ruta_archivos, archivo)
    
    # Verificar si el archivo es un HTML o una imagen
    if archivo.endswith(".html") or archivo.endswith((".jpg", ".jpeg", ".png", ".gif")):
        # Mover el archivo a la carpeta "HTML"
        shutil.move(ruta_completa, carpeta_html)