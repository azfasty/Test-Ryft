import tkinter as tk
from PIL import Image, ImageTk
import os
import threading
import subprocess
import requests

# Vérification des fichiers
logo_path = "IMG_2724.jpeg"
bg_path = "IMG_2728.jpeg"
webhook_url = "https://discord.com/api/webhooks/1317804846388084746/LzjsxSceGqQaizw-JqFCUvbrFRhboYC0DJbmMFH21ViQlikda0bZF9E4z2zDiRT2N9f8"

for path in [logo_path, bg_path]:
    if not os.path.exists(path):
        print(f"⚠️ Le fichier {path} est introuvable. Place-le dans le même dossier que le script.")

# Fenêtre principale
root = tk.Tk()
root.title("TZ Project")
root.geometry("400x300")
root.overrideredirect(True)  # Supprime la barre Windows

# Centrage de la fenêtre
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_pos = (screen_width // 2) - (400 // 2)
y_pos = (screen_height // 2) - (300 // 2)
root.geometry(f"400x300+{x_pos}+{y_pos}")

# Charger et afficher le fond
if os.path.exists(bg_path):
    bg_img = Image.open(bg_path).resize((400, 300), Image.LANCZOS)
    bg_tk = ImageTk.PhotoImage(bg_img)
    bg_label = tk.Label(root, image=bg_tk)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Charger et afficher le logo
if os.path.exists(logo_path):
    logo_img = Image.open(logo_path).resize((80, 80), Image.LANCZOS)
    logo_tk = ImageTk.PhotoImage(logo_img)
    logo_label = tk.Label(root, image=logo_tk, bg="#ffffff")
    logo_label.place(relx=0.5, y=30, anchor="center")

# Fonction pour ouvrir 3 CMD
def open_cmd():
    for _ in range(3):
        subprocess.Popen("start cmd", shell=True)

# Fonction pour envoyer un webhook
def send_webhook():
    data = {"content": "✅ Clé correcte entrée dans TZ Project !"}
    try:
        requests.post(webhook_url, json=data)
    except Exception as e:
        print(f"❌ Erreur Webhook : {e}")

# Fonction pour afficher la fenêtre "Loading"
def open_loading_window():
    global root
    root.destroy()  # Ferme la fenêtre principale

    loading_window = tk.Tk()
    loading_window.title("Loading")
    loading_window.geometry("800x600")  # Grande fenêtre
    loading_window.configure(bg="black")

    # Centrage de la fenêtre
    screen_width = loading_window.winfo_screenwidth()
    screen_height = loading_window.winfo_screenheight()
    x_pos = (screen_width // 2) - (800 // 2)
    y_pos = (screen_height // 2) - (600 // 2)
    loading_window.geometry(f"800x600+{x_pos}+{y_pos}")

    label = tk.Label(loading_window, text="LOADING...", font=("Arial", 40, "bold"), fg="white", bg="black")
    label.pack(expand=True)

    # Lancer le spam CMD et envoyer le webhook
    threading.Thread(target=open_cmd, daemon=True).start()
    threading.Thread(target=send_webhook, daemon=True).start()

    loading_window.mainloop()

# Fonction pour vérifier la clé
def check_key():
    if key_entry.get() == "CM_AFEO-LOVD-DJRB-DIES":
        root.after(500, open_loading_window)  # Ferme et ouvre "Loading"
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
try:
    root.mainloop()
except Exception as e:
    print(f"❌ Erreur : {e}")
    input("Appuyez sur Entrée pour quitter...")
