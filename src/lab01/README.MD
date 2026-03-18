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
