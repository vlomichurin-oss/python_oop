# Лабораторная работа №1. Вариант 6.
## Атрибуты класса
```
class Player:
    available_classes = ("warrior", "mage", "archer", "healer")
    max_level = 100
    base_experience = 1000


    def __init__(self, nickname: str, player_class: str, level: int = 1, health: int = 100, experience: int = 0):
        self.nickname = nickname
        self.player_class = player_class
        self.level = level
        self.health = health
        self.experience = experience
```
## Декаратор
```
@property
    def nickname(self) -> str:
        return self._nickname

    @property
    def player_class(self) -> str:
        return self._player_class

    @property
    def level(self) -> int:
        return self._level

    @property
    def health(self) -> int:
        return self._health

    @property
    def experience(self) -> int:
        return self._experience
```
## Метод валидации
