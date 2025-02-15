import tkinter as tk
from tkinter import ttk

# Fonction pour animer l'entrée de la fenêtre
def animate_window(y_start, y_end, step=10):
    def move():
        nonlocal y_start
        if y_start < y_end:
            y_start += step
            root.geometry(f"400x300+{x_pos}+{y_start}")
            root.after(10, move)
    move()

# Fonction pour changer la couleur du champ de texte au focus
def on_entry_focus_in(event):
    key_entry.config(highlightbackground="#00ffaa", highlightthickness=2)

def on_entry_focus_out(event):
    key_entry.config(highlightbackground="#555", highlightthickness=1)

# Fonction pour effet de survol du bouton
def on_button_hover(event):
    check_button.config(bg="#00ffaa", fg="black")

def on_button_leave(event):
    check_button.config(bg="#333", fg="white")

# Fenêtre principale
root = tk.Tk()
root.title("Ryft Spoofer")
root.geometry("400x300")
root.configure(bg="#222")
root.overrideredirect(True)  # Supprime la barre Windows

# Position de départ et animation d'entrée
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_pos = (screen_width // 2) - (400 // 2)
y_start = -300  # Départ hors de l'écran
y_end = (screen_height // 2) - (300 // 2)
animate_window(y_start, y_end)

# Cadre principal
frame = tk.Frame(root, bg="#222", bd=2, relief="flat")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Label du titre
title_label = tk.Label(frame, text="Ryft Spoofer", font=("Arial", 16, "bold"), bg="#222", fg="white")
title_label.pack(pady=10)

# Champ de texte (Key)
key_entry = tk.Entry(frame, font=("Arial", 14), bg="#333", fg="white", justify="center", insertbackground="white", highlightthickness=1, highlightbackground="#555")
key_entry.pack(pady=10, ipadx=10, ipady=5)
key_entry.bind("<FocusIn>", on_entry_focus_in)
key_entry.bind("<FocusOut>", on_entry_focus_out)

# Bouton CHECK
check_button = tk.Button(frame, text="CHECK", font=("Arial", 14, "bold"), bg="#333", fg="white", bd=0, relief="flat", activebackground="#00ffaa", activeforeground="black")
check_button.pack(pady=20, ipadx=10, ipady=5)
check_button.bind("<Enter>", on_button_hover)
check_button.bind("<Leave>", on_button_leave)

# Lancement de l'application
root.mainloop()
