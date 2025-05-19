# models/player.py
from dataBase.dB_manager import DBManager
from utils.exceptions import PlayerAlreadyExistsError

class Player:
    def __init__(self, name: str, symbol: str, db: DBManager):
        self.name = name
        self.symbol = symbol
        self.db = db
        self.id = None

    def register(self):
        existing = self.db.get_player(self.name)
        if existing:
            # If player already exists, reuse it
            self.id = existing[0]
            self.symbol = existing[2]  # Override symbol if already registered
        else:
            # Otherwise insert new player
            self.id = self.db.add_player(self.name, self.symbol)

    def __str__(self):
        return f"{self.name} (Symbol: {self.symbol}, ID: {self.id})"
