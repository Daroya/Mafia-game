# 🕵️ Mafia Game (Python + Pygame)

A desktop implementation of the classic **Mafia** game built with **Python** and **Pygame**.  
The project focuses on game logic, UI screens, and basic client–server networking.

This project is educational and experimental, created to practice:
- game architecture
- networking basics
- modular Python code
- Pygame UI handling

---

## 🎮 Features
- Graphical interface using Pygame
- Classic Mafia game mechanics
- Day and night phases
- Role-based gameplay (mafia, civilians, etc.)
- Basic client–server networking
- Modular and scalable project structure

---

## 🛠 Technologies Used
- **Python 3**
- **Pygame**
- Built-in `socket` library for networking

---

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/mafia-game.git
```
2. Navigate to the project directory:
```
cd mafia-game
```
3. Install dependencies:
```
pip install pygame
```

▶ Running the Game
Start the game using:
```
python main.py
```
For network mode, make sure the server is running before connecting clients.

📁 Project Structure
Mafia-game/
│
├── game/                 # Core game logic
│   ├── __init__.py
│   ├── logic.py          # Main game rules and flow
│   ├── roles.py          # Player roles and abilities
│   └── state.py          # Game states (day, night, voting)
│
├── network/              # Networking (client-server)
│   ├── __init__.py
│   ├── client.py         # Client-side networking logic
│   └── server.py         # Server-side game handling
│
├── ui/                   # User interface
│   ├── __init__.py
│   ├── menu.py           # Main menu and navigation
│   └── screens.py        # Game screens and rendering
│
├── utils/                # Helper utilities
│   ├── __init__.py
│   ├── config.py         # Game configuration and constants
│   └── helpers.py        # Utility functions
│
├── main.py               # Entry point
└── README.md

##🚧 Project Status
- The project is under active development.
- Planned improvements:
- Additional roles (Doctor, Sheriff, etc.)
- Improved UI and animations
- Better error handling
- Game lobby system
- Multiplayer improvements

##👥 Authors
Daroya
Overleas

