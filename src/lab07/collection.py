from .base import Player


class PlayerCollection:
    
    def __init__(self):
        self._players = []

    def _check_type(self, player):
        if not isinstance(player, Player):
            raise TypeError(f"Ожидается Player, получен {type(player)}")
    
    def add(self, player):
        self._check_type(player)
        if self.find_by_nickname(player.nickname):
            raise ValueError(f"Игрок {player.nickname} уже существует")
        self._players.append(player)

    def remove(self, player):
        self._check_type(player)
        self._players.remove(player)

    def remove_at(self, index):
        if 0 <= index < len(self._players):
            return self._players.pop(index)
        raise IndexError("неверный индекс")

    def get_all(self):
        return self._players.copy()
    
    def find_by_nickname(self, nickname):
        for p in self._players:
            if p.nickname.lower() == nickname.lower():
                return p
        return None
    
    def find_by_class(self, player_class):
        return [p for p in self._players if p.player_class == player_class]
    
    def sort_by_level(self, reverse=False):
        self._players.sort(key=lambda p: p.level, reverse=reverse)
    
    def sort_by_nickname(self, reverse=False):
        self._players.sort(key=lambda p: p.nickname.lower(), reverse=reverse)
    
    def get_alive(self):
        new = PlayerCollection()
        for p in self._players:
            if p.is_alive():
                new.add(p)
        return new
    
    def get_by_class(self, player_class):
        new = PlayerCollection()
        for p in self._players:
            if p.player_class == player_class:
                new.add(p)
        return new
    
    def __len__(self):
        return len(self._players)
    
    def __iter__(self):
        return iter(self._players)
    
    def __getitem__(self, index):
        return self._players[index]
    
    def __str__(self):
        return "\n".join(str(p) for p in self._players)