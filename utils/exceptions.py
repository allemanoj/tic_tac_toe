# utils/exceptions.py

class PlayerAlreadyExistsError(Exception):
    """Raised when trying to create a player that already exists"""
    pass

class InvalidMoveError(Exception):
    """Raised when a move is invalid (like placing on filled spot)"""
    pass
