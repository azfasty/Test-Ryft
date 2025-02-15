import tkinter as tk
from PIL import Image, ImageTk
import os

# Fonction pour animer l'entrée de la fenêtre
def animate_window(y_start, y_end, step=10):
    def move():
        nonlocal y_start
        if y_start < y_end:
            y_start += step
            root.geometry(f"400x300+{x_pos}+{y_start}")
            root.after(10, move)
    move()

# Fonction pour effet de survol du bouton
def on_button_hover(event):
    check_button.config(bg="#00ffaa", fg="black")

def on_button_leave(event):
    check_button.config(bg="#333", fg="white")

# Fenêtre principale
root = tk.Tk()
root.title("TZ")
root.geometry("400x300")
root.overrideredirect(True)  # Supprime la barre Windows

# Position de départ et animation d'entrée
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_pos = (screen_width // 2) - (400 // 2)
y_start = -300  # Départ hors de l'écran
y_end = (screen_height // 2) - (300 // 2)
animate_window(y_start, y_end)

# Création d'un canvas pour le dégradé
canvas = tk.Canvas(root, width=400, height=300, highlightthickness=0)
canvas.place(x=0, y=0)

# Création du dégradé violet → blanc
gradient = Image.new("RGB", (400, 300), "#ffffff")
for i in range(400):
    for j in range(300):
        r = int(138 + (255 - 138) * (i / 400))
        g = int(43 + (255 - 43) * (i / 400))
        b = int(226 + (255 - 226) * (i / 400))
        gradient.putpixel((i, j), (r, g, b))

gradient_tk = ImageTk.PhotoImage(gradient)
canvas.create_image(0, 0, anchor="nw", image=gradient_tk)

# Chargement du logo
logo_url = "https://media.discordapp.net/attachments/1339570046338596966/1340307170800963614/IMG_2724.jpg"
logo_path = "tz_logo.png"

if not os.path.exists(logo_path):
    from urllib.request import urlretrieve
    urlretrieve(logo_url, logo_path)

logo_img = Image.open(logo_path)
logo_img = logo_img.resize((80, 80), Image.LANCZOS)
logo_tk = ImageTk.PhotoImage(logo_img)

# Affichage du logo
logo_label = tk.Label(root, image=logo_tk, bg="#ffffff")
logo_label.place(relx=0.5, y=30, anchor="center")

# Cadre principal
frame = tk.Frame(root, bg="#ffffff")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Label du titre
title_label = tk.Label(frame, text="TZ", font=("Arial", 16, "bold"), bg="#ffffff", fg="black")
title_label.pack(pady=10)

# Champ de texte (Key)
key_entry = tk.Entry(frame, font=("Arial", 14), bg="#f0f0f0", fg="black", justify="center", insertbackground="black", highlightthickness=1, highlightbackground="#555")
key_entry.pack(pady=10, ipadx=10, ipady=5)

# Bouton CHECK
check_button = tk.Button(frame, text="CHECK", font=("Arial", 14, "bold"), bg="#333", fg="white", bd=0, relief="flat", activebackground="#00ffaa", activeforeground="black")
check_button.pack(pady=20, ipadx=10, ipady=5)
check_button.bind("<Enter>", on_button_hover)
check_button.bind("<Leave>", on_button_leave)

# Lancement de l'application
root.mainloop()
