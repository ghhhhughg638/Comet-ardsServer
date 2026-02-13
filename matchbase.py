from typing import Set


class GameManager:
    def __init__(self):
        self.online_players: Set[int] = set()  #在线玩家

