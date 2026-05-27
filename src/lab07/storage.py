import json
from typing import List, Dict, Any
from pathlib import Path

from .exceptions import StorageError


class PlayerStorage:
    
    def __init__(self, filepath: str = "players.json"):
        self.filepath = Path(filepath)
    
    def save(self, players: List[Any]) -> None:
        try:
            data = [self._player_to_dict(player) for player in players]
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            raise StorageError(f"Ошибка сохранения: {e}")
    
    def load(self) -> List[Dict[str, Any]]:
        if not self.filepath.exists():
            return []
        
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data
        except Exception as e:
            raise StorageError(f"Ошибка загрузки: {e}")
    
    def _player_to_dict(self, player: Any) -> Dict[str, Any]:
        return {
            'type': player.player_class,
            'nickname': player.nickname,
            'level': player.level,
            'health': player.health,
            'experience': player.experience
        }