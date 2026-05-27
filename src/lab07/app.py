from typing import List, Optional, Callable, Any
from .base import Player
from .models import Warrior, Mage, Archer
from .collection import PlayerCollection
from .exceptions import PlayerNotFoundError, DuplicatePlayerError


class GameApp:
    
    def __init__(self):
        self._collection = PlayerCollection()
    
    def add_player(self, nickname: str, player_class: str, 
                   level: int = 1, health: int = 100, 
                   experience: int = 0) -> None:
        if self._collection.find_by_nickname(nickname):
            raise DuplicatePlayerError(f"Игрок '{nickname}' уже существует!")
        
        if player_class == 'warrior':
            player = Warrior(nickname, level, health, experience)
        elif player_class == 'mage':
            player = Mage(nickname, level, health, experience)
        elif player_class == 'archer':
            player = Archer(nickname, level, health, experience)
        else:
            raise ValueError(f"Неизвестный класс: {player_class}")
        
        self._collection.add(player)
    
    def remove_player(self, nickname: str) -> None:
        player = self._collection.find_by_nickname(nickname)
        if not player:
            raise PlayerNotFoundError(f"Игрок '{nickname}' не найден!")
        
        self._collection.remove(player)
    
    def find_player(self, nickname: str) -> Optional[Player]:
        return self._collection.find_by_nickname(nickname)
    
    def find_by_class(self, player_class: str) -> List[Player]:
        return self._collection.find_by_class(player_class)
    
    def get_all_players(self) -> List[Player]:
        return self._collection.get_all()
    
    def get_alive_players(self) -> List[Player]:
        alive_collection = self._collection.get_alive()
        return alive_collection.get_all()
    
    def filter_players(self, filter_func: Callable[[Player], bool]) -> List[Player]:
        return [p for p in self._collection.get_all() if filter_func(p)]
    
    def sort_players(self, key_func: Callable[[Player], Any], reverse: bool = False) -> List[Player]:
        players = self._collection.get_all()
        players.sort(key=key_func, reverse=reverse)
        return players
    
    def get_player_stats(self) -> dict:
        players = self._collection.get_all()
        if not players:
            return {"total": 0}
        
        class_counts = {}
        for p in players:
            class_counts[p.player_class] = class_counts.get(p.player_class, 0) + 1
        
        return {
            "total": len(players),
            "avg_level": sum(p.level for p in players) / len(players),
            "avg_health": sum(p.health for p in players) / len(players),
            "alive_count": sum(1 for p in players if p.is_alive()),
            "classes": class_counts
        }
    
    # def damage_player(self, nickname: str, damage: int) -> None:
    #     """
    #     Нанести урон игроку.
        
    #     Args:
    #         nickname: никнейм игрока
    #         damage: количество урона
            
    #     Raises:
    #         PlayerNotFoundError: если игрок не найден
    #     """
    #     player = self._collection.find_by_nickname(nickname)
    #     if not player:
    #         raise PlayerNotFoundError(f"Игрок '{nickname}' не найден!")
        
    #     player.take_damage(damage)
    
    # def add_experience(self, nickname: str, exp: int) -> bool:
    #     """
    #     Добавить опыт игроку.
        
    #     Args:
    #         nickname: никнейм игрока
    #         exp: количество опыта
            
    #     Returns:
    #         True если уровень повысился
            
    #     Raises:
    #         PlayerNotFoundError: если игрок не найден
    #     """
    #     player = self._collection.find_by_nickname(nickname)
    #     if not player:
    #         raise PlayerNotFoundError(f"Игрок '{nickname}' не найден!")
        
    #     return player.gain_experience(exp)
    
    def clear(self) -> None:
        self._collection._players.clear()
    
    @property
    def count(self) -> int:
        return len(self._collection)
    
    def load_players(self, players_data: List[dict]) -> None:
        for data in players_data:
            try:
                self.add_player(
                    nickname=data['nickname'],
                    player_class=data['type'],
                    level=data['level'],
                    health=data['health'],
                    experience=data['experience']
                )
            except (DuplicatePlayerError, ValueError):
                continue