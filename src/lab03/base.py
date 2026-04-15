from abc import ABC, abstractmethod


class Player(ABC):
    
    available_classes = ("warrior", "mage", "archer", "healer")
    max_level = 100
    base_experience = 1000

    def __init__(self, nickname: str, player_class: str, level: int = 1, health: int = 100, experience: int = 0):
        self.nickname = nickname
        self.player_class = player_class
        self.level = level
        self.health = health
        self.experience = experiencex

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
    
    @nickname.setter
    def nickname(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Никнейм должен быть строкой.")
        if len(value.strip()) < 3:
            raise ValueError("Никнейм должен содержать минимум 3 символа.")
        if len(value.strip()) > 20:
            raise ValueError("Никнейм не должен превышать 20 символов.")
        self._nickname = value.strip()

    @player_class.setter
    def player_class(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Класс персонажа должен быть строкой.")
        if value not in Player.available_classes:
            raise ValueError(f"Неизвестный класс '{value}'. Допустимые классы: {', '.join(Player.available_classes)}")
        self._player_class = value

    @level.setter
    def level(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Уровень должен быть целым числом.")
        if value < 1:
            raise ValueError("Уровень не может быть меньше 1.")
        if value > Player.max_level:
            raise ValueError(f"Уровень не может превышать {Player.max_level}.")
        self._level = value

    @health.setter
    def health(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Здоровье должно быть целым числом.")
        if value < 0:
            raise ValueError("Здоровье не может быть отрицательным.")
        self._health = value

    @experience.setter
    def experience(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Опыт должен быть целым числом.")
        if value < 0:
            raise ValueError("Опыт не может быть отрицательным.")
        self._experience = value

    def take_damage(self, damage: int) -> int:
        if not isinstance(damage, int):
            raise TypeError("Урон должен быть целым числом.")
        if damage < 0:
            raise ValueError("Урон не может быть отрицательным.")

        self._health = max(0, self._health - damage)
        return self._health

    def gain_experience(self, exp: int) -> bool:
        if not isinstance(exp, int):
            raise TypeError("Опыт должен быть целым числом.")
        if exp < 0:
            raise ValueError("Опыт не может быть отрицательным.")

        self._experience += exp
        leveled_up = False

        while self._experience >= self._level * Player.base_experience and self._level < Player.max_level:
            self._experience -= self._level * Player.base_experience
            self._level += 1
            leveled_up = True
            self._health += 20

        return leveled_up

    def is_alive(self) -> bool:
        return self._health > 0
    
    @abstractmethod
    def calculate_power(self) -> int:
        pass
    
    @abstractmethod
    def get_specialization(self) -> str:
        pass
    
    def __str__(self) -> str:
        status = "Alive" if self.is_alive() else "Dead"
        return (f"{self.nickname} | [{self.player_class}] | Lvl {self._level} | "
                f"HP {self._health} | XP {self._experience} | {status}")

    def __repr__(self) -> str:
        return (f"Player(nickname='{self.nickname}', player_class='{self.player_class}', "
                f"level={self._level}, health={self._health}, experience={self._experience})")

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Player):
            return False
        return (self.nickname == other.nickname and 
                self.player_class == other.player_class)