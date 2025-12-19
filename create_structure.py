import os

STRUCTURE = {
    "game": [
        "__init__.py",
        "logic.py",
        "roles.py",
        "state.py"
    ],
    "ui": [
        "__init__.py",
        "menu.py",
        "screens.py"
    ],
    "network": [
        "__init__.py",
        "server.py",
        "client.py"
    ],
    "utils": [
        "__init__.py",
        "config.py",
        "helpers.py"
    ],
    "": [
        "main.py",
        "README.md",
        ".gitignore"
    ]
}

GITIGNORE_CONTENT = """venv/
__pycache__/
*.pyc
.env
"""

README_CONTENT = """# Mafia Game (Python)

Навчальний проєкт гри "Мафія" на Python.
Командна робота з використанням Git та GitHub.
"""

def create_structure():
    for folder, files in STRUCTURE.items():
        if folder:
            os.makedirs(folder, exist_ok=True)

        for file in files:
            path = os.path.join(folder, file) if folder else file
            if not os.path.exists(path):
                with open(path, "w", encoding="utf-8") as f:
                    if file == ".gitignore":
                        f.write(GITIGNORE_CONTENT)
                    elif file == "README.md":
                        f.write(README_CONTENT)
                    else:
                        f.write("")

    print("✅ Структура проєкту успішно створена")

if __name__ == "__main__":
    create_structure()
