import os
from datetime import datetime

extensiones_por_categoria = {
    "descargas": [".zip", ".rar", ".7z", ".tar.gz", ".iso", ".deb", ".exe", ".msi", ".dmg"],
    "imagenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".tiff", ".psd", ".raw"],
    "audios": [".mp3", ".wav", ".ogg", ".flac", ".aac", ".m4a", ".wma", ".mid"],
    "documentos": [".pdf", ".docx", ".xlsx", ".pptx", ".txt", ".odt", ".rtf", ".csv", ".md", ".epub"]
}
ruta = "Descargas-prueba"

""" Creacion de directorios no creados """
for elemento in directorios:
    if not os.path.exists(elemento):
        os.mkdir(os.path.join(ruta_acrear, elemento))
    else:
        print(f"La carpeta {elemento} ya ha sido creado.")


