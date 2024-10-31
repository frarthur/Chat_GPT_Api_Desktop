# ChatGPT Interface

Cette application est une interface utilisateur pour interagir avec l'API OpenAI GPT. Elle permet d'envoyer des messages texte et des images à l'API et d'afficher les réponses de manière interactive.

## Prérequis

- Python 3.x
- Un compte OpenAI avec une clé API valide

## Installation

1. Clonez ce dépôt sur votre machine locale :

    ```sh
    git clone https://github.com/votre-utilisateur/votre-repo.git
    cd votre-repo
    ```

2. Installez les dépendances requises :

    ```sh
    pip install -r requirements.txt
    ```

3. Créez un fichier `.env` à la racine du projet et ajoutez votre clé API OpenAI :

    ```sh
    touch .env
    ```

    Ouvrez le fichier [.env](http://_vscodecontentref_/0) et ajoutez la ligne suivante :

    ```properties
    OPENAI_API_KEY=sk-votre-cle-api
    ```

## Utilisation

1. Lancez l'application :

    ```sh
    python main.py
    ```

2. Utilisez l'interface pour envoyer des messages texte ou des images à l'API OpenAI et afficher les réponses.

## Fonctionnalités

- Envoyer des messages texte et afficher les réponses mot par mot.
- Envoyer des images et afficher les réponses.
- Basculer entre le thème sombre et le thème clair.

## Contribuer

Les contributions sont les bienvenues ! Veuillez soumettre une pull request ou ouvrir une issue pour discuter des changements que vous souhaitez apporter.

## Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.
