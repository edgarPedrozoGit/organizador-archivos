# File Organizer with Python
import os, shutil
from logging import exception

#This script organizes files automatically into folders based on their type.

# Features
#- Supports images, videos, documents, audio
#- Automatically creates folders
#- Easy to customize

# How to use
#1. Change the path
#2. Run the script

ruta = r"C:\CursoPython\proyectos\1.organizadorDeArchivos\archivosPrueba"

archivos = os.listdir(ruta)

#Currently allowed file types
tipos = {
    "imagenes": [".jpg", ".png"],
    "videos": [".mp4"],
    "PDFs": [".pdf"]
}

#This function returns the type of folder that should be created based on the file extension.
def tipo_archivo(archivo):
    for carpeta, extensiones in tipos.items():
        if archivo.endswith(tuple(extensiones)): # .ednswith only suport str or tuples
            return carpeta
    return None

#only one folder per name
carpetas_creadas = set()

for archivo in archivos:
    tipo = tipo_archivo(archivo)

    if tipo:
        if tipo not in carpetas_creadas:
            carpeta_tipo = os.path.join(ruta, tipo) #A new path is created with the folder type
            os.makedirs(carpeta_tipo, exist_ok=True) #A new folder is created
            carpetas_creadas.add(tipo)

        origen = os.path.join(ruta, archivo)
        destino = os.path.join(ruta, tipo, archivo)
        try:
            if not os.path.exists(destino):
                shutil.move(origen, destino) # This moves the file from the source path to the new path.
        except Exception as e:
            print(f"Error con {archivo}: {e}")

        print(f"Tipo: {tipo.upper()}: Archivo: {archivo}")
