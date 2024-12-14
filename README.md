# ✨ Buscador de Tarjetas ✨

Un programa diseñado para identificar y extraer tarjetas bancarias basadas en códigos BIN desde archivos obtenidos con bots en canales de Telegram.

---

## 🗃️ Características Principales

- **Búsqueda por BIN**: Ingresa uno o varios BINs separados por comas, y el programa filtrará las líneas que comiencen con dichos criterios.
- **Interfaz Gráfica**: Con una ventana intuitiva hecha en **Tkinter**, arrastrar y soltar no es necesario, solo selecciona la carpeta y ¡listo!
- **Música Ambiente**: Reproducción automática de una pista de fondo (por defecto, `Zelda.mp3`) para amenizar la espera.
- **Resultados Únicos**: Evita duplicados y copia todos los resultados en tu portapapeles con un solo clic.
- **Control de Sonido**: Silencia o enciende la música con un cómodo botón desde la interfaz.

---

## 🔧 Requisitos

- Python 3.x  
- Dependencias (listadas en `requirements.txt`):

🚀 Instrucciones de Uso
Clona el repositorio o descarga el código.
Instala las dependencias:

pip install -r requirements.txt

Ejecuta el script principal:

python main.py

Interfaz:
Ingresa los BINs en el campo de texto (separados por comas).
Presiona "Buscar" y selecciona la carpeta que contiene tus archivos .txt.
Los resultados se mostrarán en la lista y se copiarán automáticamente al portapapeles.
Puedes pausar la música con el botón de sonido en la esquina superior derecha.

📂 Estructura del Proyecto

📁 Pandita
├─ main.py
├─ requirements.txt
├─ logo.ico
├─ fondo.png
├─ sound.png
├─ mute.png
└─ Zelda.mp3
