import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import os
import pygame
import re
import pyperclip

def read_file(file_path):
    with open(file_path, 'r') as f:
        return [num.strip() for num in f.readlines()]

def filter_numbers(numbers, criteria):
    filtered_numbers = []
    for num in numbers:
        for criterion in criteria:
            if num.startswith(criterion):
                filtered_numbers.append(num)
                break
    return filtered_numbers

def copy_results_to_clipboard(results):
    results_text = "\n".join(results)
    pyperclip.copy(results_text)

def search_numbers():
    def process_numbers():
        folder_path = fd.askdirectory(title="Seleccionar carpeta", initialdir=os.getcwd())
        criteria = entry_criterios.get().split(',')
        results = []
        for file_name in os.listdir(folder_path):
            if file_name.endswith(".txt"):
                file_path = os.path.join(folder_path, file_name)
                numbers = read_file(file_path)
                filtered_numbers = filter_numbers(numbers, criteria)
                results.extend(filtered_numbers)
        results = list(set(results))
        copy_results_to_clipboard(results)
        listbox_resultados.delete(0, tk.END)
        [listbox_resultados.insert(tk.END, resultado) for resultado in results]
        mb.showinfo("Resultados",f"Se encontraron {len(results)} coincidencias. Los resultados han sido copiados al portapapeles.")

    root = tk.Tk()
    root.title("Busqueda Tarjetas Sabadell")
    root.iconbitmap('logo.ico')
    root.geometry("800x600")
    root.minsize(400,300)

    background_image = tk.PhotoImage(file="fondo.png")
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    label_criterios = tk.Label(root, text="Ingresa el código BIN de la tarjeta para la búsqueda separados por comas:", bg="white")
    label_criterios.pack(padx=10, pady=10)

    entry_criterios = tk.Entry(root, width=50)
    entry_criterios.pack(padx=10, pady=10)

    button_procesar = tk.Button(root, text="Buscar", command=process_numbers, bg="blue", fg="white", font=("Arial", 12, "bold"))
    button_procesar.pack(padx=10, pady=10)

    pygame.init()
    pygame.mixer.music.load("Zelda.mp3")
    pygame.mixer.music.play(-1)

    frame_resultados = tk.Frame(root, bg="#F0E68C")
    frame_resultados.pack(padx=10, pady=10, fill="both", expand=True)

    scrollbar = tk.Scrollbar(frame_resultados)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listbox_resultados = tk.Listbox(frame_resultados, yscrollcommand=scrollbar.set, bg="#FFFACD", font=("Arial Unicode MS", 12), selectbackground="#F4A460", selectforeground="white")
    listbox_resultados.pack(side=tk.LEFT, fill="both", expand=True)
    scrollbar.config(command=listbox_resultados.yview)

    def toggle_sound():
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
            button_sound.config(image=mute_icon)
        else:
            pygame.mixer.music.play(-1)
            button_sound.config(image=sound_icon)

    sound_icon = tk.PhotoImage(file="sound.png")
    mute_icon = tk.PhotoImage(file="mute.png")
    button_sound = tk.Button(root, image=sound_icon, bg="#F0E68C", borderwidth=0, command=toggle_sound)
    button_sound.place(relx=0.95, rely=0.05, anchor="ne")

    root.mainloop()

if __name__ == "__main__":
    search_numbers()
