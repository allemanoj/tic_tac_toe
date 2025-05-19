# main.py

from dataBase.dB_manager import DBManager
from models.player import Player
from services.game_engine import GameEngine

def start_game(db):
    print("=== Welcome to Tic Tac Toe ===")
    p1_name = input("Enter Player 1 name: ").strip()
    p2_name = input("Enter Player 2 name: ").strip()

    p1 = Player(p1_name, "X", db)
    p1.register()

    p2 = Player(p2_name, "O", db)
    p2.register()

    while True:
        game = GameEngine(p1, p2, db)
        game.play_game()

        while True:
            choice = input("🔁 Play again? (y = yes, h = history, n = quit): ").strip().lower()
            if choice == 'y':
                break  # replay loop continues
            elif choice == 'h':
                game.view_game_history()
            elif choice == 'n':
                print("👋 Thanks for playing!")
                return
            else:
                print("⚠️ Invalid choice. Please enter 'y', 'h', or 'n'.")

def main():
    db = DBManager()
    try:
        start_game(db)
    finally:
        db.close()

if __name__ == "__main__":
    main()
