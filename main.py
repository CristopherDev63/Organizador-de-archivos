import os
from datetime import datetime

archivos_acrear = ["reporte.pdf", "foto1.jpg", "setup.zip", "cancion.mp3", "datos.xlsx", "contrato.docx", "imagen.png", "backup.rar", "audio_book.wav", "presentacion.pptx", "documento.txt", "logo.svg", "instalador.exe", "ringtone.ogg", "hoja_calculo.ods", "fondo.webp", "musica.flac", "archivo1.7z", "notas.rtf", "captura.bmp", "manual.epub", "sonido.aac", "paquete.deb", "dibujo.psd", "lista.csv", "foto2.jpeg", "comprimido.tar.gz", "podcast.m4a", "planilla.odt", "icono.ico", "instalacion.msi", "grabacion.wma", "informe.doc", "grafico.tiff", "backup2.iso", "melodia.mid", "codigo.py", "foto3.heic", "paquete2.rpm", "documento2.md", "imagen2.raw", "setup2.bin", "audio2.aiff", "libro.mobi", "hoja.123", "foto4.pgm", "respaldo.dmg", "tono.amr", "datos2.json", "firma.pem"]
directorios = ["Descargas", "Documentos", "Imagenes", "Audios"]
ruta_acrear = "archivos-prueba" 

for elemento in directorios:
    if not os.path.exists(elemento):
        os.mkdir(os.path.join(ruta_acrear, elemento))
    else:
        print(f"La carpeta {elemento} ya ha sido creado.")
