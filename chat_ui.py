import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
from chat_controller import ChatController

class ChatUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ChatGPT Interface")
        self.controller = ChatController()
        self.dark_mode = True  # Mode sombre par défaut

        # Variable pour le modèle GPT
        self.gpt_version = tk.StringVar(value="gpt-4")

        self._setup_ui()

    def _setup_ui(self):
        # Zone pour afficher les réponses
        self.response_text = scrolledtext.ScrolledText(self.root, height=20, width=50, font=("Helvetica", 14))
        self.response_text.pack(pady=10)
        self.response_text.tag_configure("user", foreground="#61afef")
        self.response_text.tag_configure("assistant", foreground="#98c379")

        # Zone pour entrer du texte
        self.user_input_text = tk.Text(self.root, height=5, width=50, font=("Helvetica", 14))
        self.user_input_text.pack(pady=10)

        # Menu déroulant pour choisir le modèle GPT
        gpt_options = ["gpt-3.5-turbo", "gpt-4", "gpt-4o-mini"]
        self.gpt_menu = tk.OptionMenu(self.root, self.gpt_version, *gpt_options)
        self.gpt_menu.pack(pady=10)


        # Bouton pour envoyer un message
        send_button = tk.Button(self.root, text="Envoyer", command=self._send_message)
        send_button.pack(pady=10)

        # Bouton pour basculer le thème
        theme_button = tk.Button(self.root, text="Thème clair/sombre", command=self._toggle_theme)
        theme_button.pack(pady=10)

        # Lier Ctrl+Enter à l'envoi
        self.root.bind('<Control-Return>', lambda event: self._send_message())

        # Appliquer le thème sombre par défaut
        self._apply_dark_theme()

    def _send_message(self):
        user_input = self.user_input_text.get("1.0", tk.END).strip()
        if user_input:
            self.response_text.insert(tk.END, f"Vous : {user_input}\n", "user")
            self.user_input_text.delete("1.0", tk.END)

            # Appeler le contrôleur pour obtenir la réponse
            response = self.controller.get_response(user_input, self.gpt_version.get())
            self._display_response_word_by_word(response)

    def _display_response_word_by_word(self, response, index=0):
        words = response.split()
        if index < len(words):
            self.response_text.insert(tk.END, words[index] + " ", "assistant")
            self.root.after(200, self._display_response_word_by_word, response, index + 1)
        else:
            self.response_text.insert(tk.END, "\n\n")

    def _toggle_theme(self):
        self.dark_mode = not self.dark_mode
        if self.dark_mode:
            self._apply_dark_theme()
        else:
            self._apply_light_theme()

    def _apply_dark_theme(self):
        self.root.configure(bg="#282c34")
        self.response_text.configure(bg="#282c34", fg="#abb2bf", insertbackground="#abb2bf")
        self.user_input_text.configure(bg="#282c34", fg="#abb2bf", insertbackground="#abb2bf")
        
        # Appliquer le style sombre aux boutons
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button):
                widget.configure(bg="#3c4048", fg="#ffffff", activebackground="#4b5260", activeforeground="#ffffff")

        # Appliquer le style sombre au menu déroulant
        self.gpt_menu.configure(bg="#3c4048", fg="#ffffff", activebackground="#4b5260")
        self.gpt_menu["menu"].configure(bg="#3c4048", fg="#ffffff")  # Menu interne


    def _apply_light_theme(self):
        self.root.configure(bg="#ffffff")
        self.response_text.configure(bg="#ffffff", fg="#000000", insertbackground="#000000")
        self.user_input_text.configure(bg="#ffffff", fg="#000000", insertbackground="#000000")
        
        # Appliquer le style clair aux boutons
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button):
                widget.configure(bg="#f0f0f0", fg="#000000", activebackground="#dcdcdc", activeforeground="#000000")

        # Appliquer le style clair au menu déroulant
        self.gpt_menu.configure(bg="#f0f0f0", fg="#000000", activebackground="#dcdcdc")
        self.gpt_menu["menu"].configure(bg="#f0f0f0", fg="#000000")  # Menu interne



    def run(self):
        self.root.mainloop()
