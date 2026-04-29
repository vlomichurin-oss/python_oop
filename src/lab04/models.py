from typing import List
from interfaces import Printable, Comparable, Identifiable


class Player(Printable, Comparable, Identifiable):
    def __init__(self, nickname: str, player_class: str, level: int = 1, health: int = 100):
        self.nickname = nickname
        self.player_class = player_class
        self.level = level
        self.health = health
        self._max_health = 100
    
    # ===== Реализация Printable =====
    def to_string(self) -> str:
        status = "Жив" if self.is_alive() else "Мёртв"
        return f"Игрок: {self.nickname} | Класс: {self.player_class} | Уровень: {self.level} | HP: {self.health}/{self._max_health} | {status}"
    
    # ===== Реализация Comparable =====
    def compare_to(self, other) -> int:
        if not isinstance(other, Player):
            raise TypeError(f"Нельзя сравнить Player с {type(other)}")
        
        if self.level < other.level:
            return -1
        elif self.level > other.level:
            return 1
        return 0
    
    # ===== Реализация Identifiable =====
    def get_id(self) -> str:
        return f"player_{self.nickname.lower()}"
    
    # ===== Собственные методы =====
    def is_alive(self) -> bool:
        return self.health > 0
    
    def take_damage(self, damage: int):
        self.health = max(0, self.health - damage)
    
    def heal(self, amount: int):
        if self.is_alive():
            self.health = min(self._max_health, self.health + amount)
    
    def level_up(self):
        self.level += 1
        self.health = self._max_health
    
    def __str__(self):
        return self.to_string()


class NPC(Printable, Comparable, Identifiable):
    def __init__(self, name: str, npc_type: str, importance: int = 1):
        self.name = name
        self.npc_type = npc_type  # merchant, quest, guard, etc.
        self.importance = importance  # 1-10
    
    # ===== Реализация Printable =====
    def to_string(self) -> str:
        importance_stars = "★" * self.importance + "☆" * (10 - self.importance)
        return f"NPC: {self.name} | Тип: {self.npc_type} | Важность: {importance_stars} ({self.importance}/10)"
    
    # ===== Реализация Comparable =====
    def compare_to(self, other) -> int:
        if not isinstance(other, NPC):
            raise TypeError(f"Нельзя сравнить NPC с {type(other)}")
        
        if self.importance < other.importance:
            return -1
        elif self.importance > other.importance:
            return 1
        return 0
    
    # ===== Реализация Identifiable =====
    def get_id(self) -> str:
        return f"npc_{self.name.lower()}"
    
    def __str__(self):
        return self.to_string()


class PlayerCollection:
    def __init__(self):
        self._players = []
    
    def _check_type(self, player):
        if not isinstance(player, Player):
            raise TypeError(f"Ожидается Player, получен {type(player)}")
    
    # ===== Базовые методы =====
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
    
    # ===== Поиск =====
    def find_by_nickname(self, nickname):
        for p in self._players:
            if p.nickname.lower() == nickname.lower():
                return p
        return None
    
    def find_by_class(self, player_class):
        return [p for p in self._players if p.player_class == player_class]
    
    # ===== Методы для работы с интерфейсами (фильтрация) =====
    def get_printable_items(self) -> List[Printable]:
        return [p for p in self._players if isinstance(p, Printable)]
    
    def get_comparable_items(self) -> List[Comparable]:
        return [p for p in self._players if isinstance(p, Comparable)]
    
    def get_identifiable_items(self) -> List[Identifiable]:
        return [p for p in self._players if isinstance(p, Identifiable)]
    
    def filter_by_interface(self, interface_type):
        return [item for item in self._players if isinstance(item, interface_type)]
    
    # ===== Сортировка через Comparable =====
    def sort_by_comparable(self, reverse=False):
        self._players.sort(key=lambda p: p.level, reverse=reverse)
    
    def sort_by_nickname(self, reverse=False):
        self._players.sort(key=lambda p: p.nickname.lower(), reverse=reverse)
    
    # ===== Фильтрация =====
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
    
    # ===== Магические методы =====
    def __len__(self):
        return len(self._players)
    
    def __iter__(self):
        return iter(self._players)
    
    def __getitem__(self, index):
        return self._players[index]
    
    def __str__(self):
        return "\n".join(str(p) for p in self._players)