import tkinter as tk
from PIL import Image, ImageTk
import os

# Fenêtre principale
root = tk.Tk()
root.title("TZ")
root.geometry("400x300")
root.overrideredirect(True)  # Supprime la barre Windows

# Position de la fenêtre
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_pos = (screen_width // 2) - (400 // 2)
y_pos = (screen_height // 2) - (300 // 2)
root.geometry(f"400x300+{x_pos}+{y_pos}")

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

# Chargement du logo (il doit être dans le même dossier que le script)
logo_path = "IMG_2724.jpeg"

if os.path.exists(logo_path):
    logo_img = Image.open(logo_path)
    logo_img = logo_img.resize((80, 80), Image.LANCZOS)
    logo_tk = ImageTk.PhotoImage(logo_img)

    # Affichage du logo
    logo_label = tk.Label(root, image=logo_tk, bg="#ffffff")
    logo_label.place(relx=0.5, y=30, anchor="center")
else:
    print("⚠️ Le fichier logo.png est introuvable. Place-le dans le même dossier que le script.")

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

# Lancement de l'application
root.mainloop()
