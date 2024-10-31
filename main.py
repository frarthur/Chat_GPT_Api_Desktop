import tkinter as tk
from tkinter import scrolledtext, filedialog
import openai
from dotenv import load_dotenv
import os

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Configurez votre clé API OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_response(event=None):
    user_input = user_input_text.get("1.0", tk.END).strip()
    if user_input:
        response = openai.ChatCompletion.create(
            model=gpt_version.get(),
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        response_text.insert(tk.END, f"User: {user_input}\n", "user")
        display_text_word_by_word(response.choices[0].message['content'])

        user_input_text.delete("1.0", tk.END)

def display_text_word_by_word(text, index=0):
    words = text.split()
    if index < len(words):
        response_text.insert(tk.END, words[index] + " ", "assistant")
        index += 1
        root.after(200, display_text_word_by_word, text, index)
    else:
        response_text.insert(tk.END, "\n\n")

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if file_path:
        send_image(file_path)

def send_image(file_path):
    with open(file_path, "rb") as image_file:
        image_data = image_file.read()
        response = openai.Image.create(
            model=gpt_version.get(),
            images=[image_data]
        )
        response_text.insert(tk.END, f"Image sent: {file_path}\n", "user")
        display_text_word_by_word(response.choices[0].message['content'])

# Fonction pour basculer entre les thèmes
def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    if dark_mode:
        root.configure(bg="#282c34")
        user_input_text.configure(bg="#282c34", fg="#abb2bf", insertbackground="#abb2bf")
        response_text.configure(bg="#282c34", fg="#abb2bf", insertbackground="#abb2bf")
        gpt_menu.configure(bg="#282c34", fg="#abb2bf")
        send_button.configure(bg="#282c34", fg="#abb2bf")
        theme_button.configure(bg="#282c34", fg="#abb2bf")
        image_button.configure(bg="#282c34", fg="#abb2bf")
    else:
        root.configure(bg="#ffffff")
        user_input_text.configure(bg="#ffffff", fg="#000000", insertbackground="#000000")
        response_text.configure(bg="#ffffff", fg="#000000", insertbackground="#000000")
        gpt_menu.configure(bg="#ffffff", fg="#000000")
        send_button.configure(bg="#ffffff", fg="#000000")
        theme_button.configure(bg="#ffffff", fg="#000000")
        image_button.configure(bg="#ffffff", fg="#000000")

# Créer la fenêtre principale
root = tk.Tk()
root.title("ChatGPT Interface")

# Variable pour stocker la version de GPT sélectionnée
gpt_version = tk.StringVar(value="gpt-4")

# Initialiser le mode sombre
dark_mode = False  # Initialiser à False pour que toggle_theme le bascule à True

# Créer les widgets
user_input_text = tk.Text(root, height=5, width=50, font=("Helvetica", 14))
user_input_text.pack(pady=10)

response_text = scrolledtext.ScrolledText(root, height=20, width=50, font=("Helvetica", 14))
response_text.pack(pady=10)

# Ajouter des tags pour les couleurs de texte
response_text.tag_configure("user", foreground="#61afef")  # Bleu pastel
response_text.tag_configure("assistant", foreground="#98c379")  # Vert pastel

# Menu déroulant pour sélectionner la version de GPT
gpt_options = ["gpt-3.5-turbo", "gpt-4", "gpt-4o-mini"]
gpt_menu = tk.OptionMenu(root, gpt_version, *gpt_options)
gpt_menu.pack(pady=10)

send_button = tk.Button(root, text="Envoyer", command=get_response)
send_button.pack(pady=10)

# Bouton pour envoyer une image
image_button = tk.Button(root, text="Envoyer une image", command=select_image)
image_button.pack(pady=10)

# Bouton pour basculer entre les thèmes
theme_button = tk.Button(root, text="Passer au thème clair", command=toggle_theme)
theme_button.pack(pady=10)

# Lier Ctrl + Return à la fonction get_response
root.bind('<Control-Return>', get_response)

# Appliquer le thème initial (sombre)
toggle_theme()

# Lancer l'application
root.mainloop()