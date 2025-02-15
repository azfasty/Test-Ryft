import tkinter as tk
from PIL import Image, ImageTk
import os
import threading
from playsound import playsound

# Vérification des fichiers
logo_path = "IMG_2724.jpeg"
bg_path = "IMG_2728.jpeg"
sound_path = "checksound.mp3"

if not os.path.exists(logo_path):
    print(f"⚠️ Le fichier {logo_path} est introuvable. Place-le dans le même dossier que le script.")
if not os.path.exists(bg_path):
    print(f"⚠️ Le fichier {bg_path} est introuvable. Place-le dans le même dossier que le script.")
if not os.path.exists(sound_path):
    print(f"⚠️ Le fichier {sound_path} est introuvable. Place-le dans le même dossier que le script.")

# Fenêtre principale
root = tk.Tk()
root.title("TZ Project")
root.geometry("400x300")
root.overrideredirect(True)  # Supprime la barre Windows

# Position de la fenêtre
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_pos = (screen_width // 2) - (400 // 2)
y_pos = (screen_height // 2) - (300 // 2)
root.geometry(f"400x300+{x_pos}+{y_pos}")

# Charger et afficher le fond
if os.path.exists(bg_path):
    bg_img = Image.open(bg_path)
    bg_img = bg_img.resize((400, 300), Image.LANCZOS)
    bg_tk = ImageTk.PhotoImage(bg_img)
    
    bg_label = tk.Label(root, image=bg_tk)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Charger et afficher le logo
if os.path.exists(logo_path):
    logo_img = Image.open(logo_path)
    logo_img = logo_img.resize((80, 80), Image.LANCZOS)
    logo_tk = ImageTk.PhotoImage(logo_img)

    logo_label = tk.Label(root, image=logo_tk, bg="#ffffff")
    logo_label.place(relx=0.5, y=30, anchor="center")

# Fonction pour jouer le son en boucle
def play_sound():
    while True:
        playsound(sound_path)

# Fonction pour vérifier la clé et lancer le son
def check_key():
    if key_entry.get() == "CM_AFEO-LOVD-DJRB-DIES":
        result_label.config(text="✅ Clé valide !", fg="green")
        
        # Lancer le son en boucle dans un thread séparé
        sound_thread = threading.Thread(target=play_sound, daemon=True)
        sound_thread.start()
    else:
        result_label.config(text="❌ Clé invalide", fg="red")

# Cadre principal
frame = tk.Frame(root, bg="#ffffff")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Label du titre
title_label = tk.Label(frame, text="TZ Project", font=("Arial", 16, "bold"), bg="#ffffff", fg="black")
title_label.pack(pady=10)

# Champ de texte (Key)
key_entry = tk.Entry(frame, font=("Arial", 14), bg="#f0f0f0", fg="black", justify="center", insertbackground="black", highlightthickness=1, highlightbackground="#555")
key_entry.pack(pady=10, ipadx=10, ipady=5)

# Bouton CHECK
check_button = tk.Button(frame, text="CHECK", font=("Arial", 14, "bold"), bg="#333", fg="white", bd=0, relief="flat", activebackground="#00ffaa", activeforeground="black", command=check_key)
check_button.pack(pady=10, ipadx=10, ipady=5)

# Label pour le résultat
result_label = tk.Label(frame, text="", font=("Arial", 12), bg="#ffffff")
result_label.pack(pady=5)

# Lancement de l'application
root.mainloop()
