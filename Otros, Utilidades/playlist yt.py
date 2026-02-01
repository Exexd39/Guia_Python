import os
import yt_dlp

def descargar_playlist(url_playlist, carpeta_destino):
    # Asegura que exista la carpeta
    os.makedirs(carpeta_destino, exist_ok=True)

    opciones = {
        'format': 'bestaudio/best',
        'outtmpl': f'{carpeta_destino}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'postprocessor_args': [
            '-ar', '44100',
            '-ac', '2',
            '-b:a', '320k'
        ],
        'prefer_ffmpeg': True,
        'geo_bypass': True,
        'noplaylist': False,
        'quiet': False
    }

    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([url_playlist])

if __name__ == "__main__":
    print("=== Descargador de Playlists de YouTube a MP3 320kbps ===")
    url = input("🔗 Pega el enlace de la playlist: ")
    carpeta = input("📁 Ruta de carpeta de destino (ej. C:/Users/TuUsuario/Música/YouTube): ").strip()

    if not carpeta:
        carpeta = "descargas"
    descargar_playlist(url, carpeta)
    print("\n✅ Descarga completada.")
