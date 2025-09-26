import tkinter as tk
from tkinter import messagebox
import random
import string
import datetime
from tkinter import simpledialog


def generate_password(length, use_upper, use_digits, use_special):
    """Génère un mot de passe basé sur les critères fournis."""
    char_pool = string.ascii_lowercase
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_digits:
        char_pool += string.digits
    if use_special:
        char_pool += string.punctuation

    if not char_pool:
        return ""

    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

# --- Configuration de l'interface graphique ---
root = tk.Tk()
root.title("Générateur de mot de passe")
root.geometry("450x350")
root.resizable(False, False)

# --- Widgets ---

# Frame pour les options
options_frame = tk.Frame(root, padx=10, pady=10)
options_frame.pack(fill="x")

# Longueur du mot de passe
label_length = tk.Label(options_frame, text="Longueur du mot de passe:")
label_length.pack(anchor="w")

entry_length = tk.Entry(options_frame, width=10)
entry_length.pack(anchor="w", pady=(0, 10))
entry_length.insert(0, "16")

# Options de complexité
var_upper = tk.IntVar(value=1)
check_upper = tk.Checkbutton(options_frame, text="Inclure des majuscules (A-Z)", variable=var_upper)
check_upper.pack(anchor="w")

var_digits = tk.IntVar(value=1)
check_digits = tk.Checkbutton(options_frame, text="Inclure des chiffres (0-9)", variable=var_digits)
check_digits.pack(anchor="w")

var_special = tk.IntVar(value=1)
check_special = tk.Checkbutton(options_frame, text="Inclure des caractères spéciaux (!, @, #, etc.)", variable=var_special)
check_special.pack(anchor="w")

# Champ pour afficher le mot de passe généré
password_frame = tk.Frame(root, padx=10)
password_frame.pack(fill="x", pady=10)

label_result = tk.Label(password_frame, text="Mot de passe généré:")
label_result.pack(anchor="w")

text_password = tk.Entry(password_frame, font=("Courier", 12))
text_password.pack(fill="x")


# --- Fonctions des boutons ---

def on_generate():
    """Génère le mot de passe et l'affiche."""
    try:
        length = int(entry_length.get())
        if length <= 0:
            messagebox.showerror("Erreur", "La longueur doit être un nombre positif.")
            return
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer un nombre valide pour la longueur.")
        return

    password = generate_password(
        length,
        bool(var_upper.get()),
        bool(var_digits.get()),
        bool(var_special.get())
    )

    if not password:
        messagebox.showwarning("Attention", "Veuillez sélectionner au moins un type de caractère.")
        return

    text_password.delete(0, tk.END)
    text_password.insert(0, password)

def on_copy():
    """Copie le mot de passe dans le presse-papiers."""
    password = text_password.get()
    if not password:
        messagebox.showerror("Erreur", "Générez d'abord un mot de passe.")
        return

    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Copié", "Le mot de passe a été copié dans le presse-papiers.")

def on_save():
    """Sauvegarde le mot de passe avec une date complète dans un fichier texte en l'ajoutant à la fin."""
    password = text_password.get()
    if not password:
        messagebox.showerror("Erreur", "Générez d'abord un mot de passe.")
        return
    
    # Ouvre une petite fenêtre pour demander une description à l'utilisateur
    description = simpledialog.askstring("Description", "Pour quel site/service est ce mot de passe ?")

    # Si l'utilisateur clique sur "Annuler" ou ne saisit rien, on arrête l'enregistrement
    if not description:
        messagebox.showwarning("Annulé", "L'enregistrement a été annulé car aucune description n'a été fournie.")
        return    

    # Récupérer la date et l'heure actuelles et les formater
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Préparer la ligne à enregistrer : "DESCRIPTION DATE MOT_DE_PASSE" suivi d'un saut de ligne
    entry_to_save = f"{description} {timestamp} {password}\n"

    try:
        # Toujours utiliser le mode "a" pour ajouter à la fin du fichier
        with open("mot_de_passe_sauvegardé.txt", "a", encoding='utf-8') as f:
            f.write(entry_to_save)
        messagebox.showinfo("Sauvegardé", "Le mot de passe avec la date a été ajouté dans 'mot_de_passe_sauvegardé.txt'.")
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur est survenue lors de la sauvegarde : {e}")


# --- Boutons ---
buttons_frame = tk.Frame(root, pady=10)
buttons_frame.pack()

button_generate = tk.Button(buttons_frame, text="Générer", command=on_generate, width=20, height=2)
button_generate.pack(pady=5)

button_copy = tk.Button(buttons_frame, text="Copier", command=on_copy, width=15)
button_copy.pack(side="left", padx=5)

button_save = tk.Button(buttons_frame, text="Sauvegarder", command=on_save, width=15)
button_save.pack(side="left", padx=5)


# --- Démarrer l'application ---
root.mainloop()

