import os
import yt_dlp
from pydub import AudioSegment

CARPETA_SALIDA = "descargas_mp3"
os.makedirs(CARPETA_SALIDA, exist_ok=True)

def convertir_a_mp3(archivo_entrada):
    """Convierte un archivo descargado a MP3 320kbps y elimina el original."""
    try:
        base = os.path.splitext(archivo_entrada)[0]
        salida_mp3 = base + ".mp3"

        # Si ya existe el MP3, no se convierte de nuevo
        if os.path.exists(salida_mp3):
            print(f"➡️  Ya existe: {os.path.basename(salida_mp3)} (omitido)")
            return

        audio = AudioSegment.from_file(archivo_entrada)
        audio.export(salida_mp3, format="mp3", bitrate="320k")

        os.remove(archivo_entrada)
        print(f"✅ Convertido: {os.path.basename(salida_mp3)}")
    except Exception as e:
        print(f"⚠️  Error al convertir {archivo_entrada}: {e}")

def descargar_audio(url):
    """Descarga el audio (de video o playlist) usando yt_dlp."""
    try:
        opciones = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(CARPETA_SALIDA, '%(title)s.%(ext)s'),
            'quiet': True,
            'ignoreerrors': True,
        }

        with yt_dlp.YoutubeDL(opciones) as ydl:
            info = ydl.extract_info(url, download=False)

            # Si es una playlist
            if 'entries' in info:
                print(f"\n📂 Playlist detectada: {info.get('title', 'Sin título')}")
                print(f"🎶 Total de canciones: {len(info['entries'])}\n")

                for i, entry in enumerate(info['entries'], start=1):
                    if not entry:
                        continue
                    print(f"▶️  ({i}/{len(info['entries'])}) {entry['title']}")
                    nombre_archivo = os.path.join(CARPETA_SALIDA, f"{entry['title']}.mp3")

                    # Saltar si ya existe el MP3
                    if os.path.exists(nombre_archivo):
                        print(f"➡️  Ya descargado: {entry['title']}\n")
                        continue

                    # Descargar audio individual
                    ydl.download([entry['webpage_url']])

                print("\n✅ Playlist completada.\n")

            else:
                print(f"\n🎵 Descargando: {info['title']}")
                ydl.download([url])

        # Convertir todo lo que no esté en MP3
        for archivo in os.listdir(CARPETA_SALIDA):
            ruta = os.path.join(CARPETA_SALIDA, archivo)
            if not archivo.lower().endswith(".mp3"):
                convertir_a_mp3(ruta)

    except Exception as e:
        print(f"❌ Error general: {e}\n")

if __name__ == "__main__":
    print("=== DESCARGADOR DE MP3 (YouTube y playlists) ===")
    while True:
        enlace = input("\nPega el enlace del video o playlist (o escribe 'salir'): ").strip()
        if enlace.lower() == "salir":
            print("👋 Saliendo del programa...")
            break
        descargar_audio(enlace)
