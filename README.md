# 🎮 Tic-Tac-Toe Game (Python + SQLite)

A modular, extensible, and production-level Tic-Tac-Toe game built in Python using OOP principles, exception handling, and SQLite database for tracking players and game history.

---

## 📦 Features

- 👥 Two-player console-based Tic-Tac-Toe
- 🧠 Object-Oriented design using classes for `Player`, `Board`, and `GameEngine`
- 🛠️ Modular codebase with separation of concerns
- 🧾 SQLite integration to:
  - Store player details
  - Track game winners with timestamps
- 📜 Game History Viewer
- 🔁 Option to Replay or Quit after each game
- ✅ Unit tested with `pytest`

---

## 📁 Project Structure

```bash
tic_tac_toe/
│
├── database/
│   └── db_manager.py          # Handles SQLite setup and queries
│
├── models/
│   ├── player.py              # Player logic and registration
│   └── board.py               # Game board implementation
│
├── services/
│   └── game_engine.py         # Game controller & game loop logic
│
├── tests/
│   ├── test_board.py
│   ├── test_player.py
│   └── test_db.py             # Pytest unit tests
│
├── main.py                    # Entry point: runs the game
└── README.md                  # Project documentation
```

## Create virtual Environment
-python -m venv venv
-source venv/bin/activate  # On Windows: venv\Scripts\activate
## install Requirements
- pip install -r requirements.txt
## Run the Game
python main.py
