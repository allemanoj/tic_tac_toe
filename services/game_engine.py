# services/game_engine.py
from models.board import Board
from models.player import Player
from dataBase.dB_manager import DBManager
from utils.exceptions import InvalidMoveError
from datetime import datetime

class GameEngine:
    def __init__(self, player1: Player, player2: Player, db: DBManager):
        self.board = Board()
        self.players = [player1, player2]
        self.db = db
        self.current_turn = 0  # 0 -> player1, 1 -> player2

    def switch_turn(self):
        self.current_turn = 1 - self.current_turn

    
    def view_game_history(self):
        print("\n📜 Game History:")
        cursor = self.db.conn.execute("""
            SELECT gh.id, p.name, gh.played_at
            FROM game_history gh
            LEFT JOIN players p ON gh.winner_id = p.id
            ORDER BY gh.played_at DESC
        """)
        rows = cursor.fetchall()

        if not rows:
            print("No games played yet.")
            return

        for row in rows:
            game_id, winner_name, timestamp = row
            winner_text = winner_name if winner_name else "Draw"
            print(f"Game #{game_id} | Winner: {winner_text} | Time: {timestamp}")


    def play_game(self):
        self.board.display()
        while True:
            current_player = self.players[self.current_turn]
            print(f"{current_player.name}'s Turn ({current_player.symbol})")

            try:
                row = int(input("Enter row (1-3): ")) - 1
                col = int(input("Enter col (1-3): ")) - 1
                self.board.make_move(row, col, current_player.symbol)
            except (ValueError, IndexError):
                print("⚠️ Invalid input. Please enter numbers between 1-3.")
                continue
            except InvalidMoveError as e:
                print(f"⚠️ {e}")
                continue

            self.board.display()

            if self.board.check_winner(current_player.symbol):
                print(f"🎉 {current_player.name} wins!")
                self.db.store_game_result(winner_id=current_player.id, timestamp=datetime.now().isoformat())
                break

            if self.board.is_draw():
                print("🤝 It's a draw!")
                self.db.store_game_result(winner_id=None, timestamp=datetime.now().isoformat())
                break

            self.switch_turn()
