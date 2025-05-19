# database/db_manager.py
import sqlite3
from datetime import datetime

class DBManager:
    def __init__(self, db_name="tictactoe.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS players (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    symbol TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')

            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS game_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    winner_id INTEGER,
                    played_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY(winner_id) REFERENCES players(id)
                )
            ''')

    def add_player(self, name, symbol):
        with self.conn:
            cursor = self.conn.execute(
                'INSERT INTO players (name, symbol) VALUES (?, ?)',
                (name, symbol)
            )
            return cursor.lastrowid

    def get_player(self, name):
        cursor = self.conn.execute(
            'SELECT * FROM players WHERE name = ?', (name,)
        )
        return cursor.fetchone()

    def store_game_result(self, winner_id, timestamp):
     with self.conn:
        self.conn.execute(
            'INSERT INTO game_history (winner_id, played_at) VALUES (?, ?)',
            (winner_id, timestamp)
        )

    def close(self):
        self.conn.close()
