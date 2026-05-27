from .base import Player


class Warrior(Player):
    def __init__(self, nickname: str, level: int = 1, health: int = 150, 
                 experience: int = 0, strength: int = 20, defense: int = 15):
        super().__init__(nickname, "warrior", level, health, experience)
        self.strength = strength
        self.defense = defense
    
    @property
    def strength(self) -> int:
        return self._strength
    
    @property
    def defense(self) -> int:
        return self._defense
    
    @strength.setter
    def strength(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Сила должна быть целым числом")
        if value < 1 or value > 100:
            raise ValueError("Сила должна быть от 1 до 100")
        self._strength = value
    
    @defense.setter
    def defense(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Защита должна быть целым числом")
        if value < 0 or value > 50:
            raise ValueError("Защита должна быть от 0 до 50")
        self._defense = value
    
    def heavy_attack(self) -> int:
        damage = self._strength * 2
        print(f"{self.nickname} использует Тяжелую атаку! Урон: {damage}")
        return damage
    
    def take_damage(self, damage: int) -> int:
        reduced_damage = max(1, damage - self._defense // 2)
        print(f"Защита снизила урон с {damage} до {reduced_damage}")
        return super().take_damage(reduced_damage)
    
    def calculate_power(self) -> int:
        return self.level * 10 + self.strength + self.defense
    
    def get_specialization(self) -> str:
        return f"Воин | Сила: {self.strength} | Защита: {self.defense}"
    
    def __str__(self) -> str:
        return f"{super().__str__()} | Сил:{self.strength} Защ:{self.defense}"


class Mage(Player):    
    def __init__(self, nickname: str, level: int = 1, health: int = 80,
                 experience: int = 0, mana: int = 100, spell_power: int = 25):
        super().__init__(nickname, "mage", level, health, experience)
        self.mana = mana
        self.spell_power = spell_power
    
    @property
    def mana(self) -> int:
        return self._mana
    
    @property
    def spell_power(self) -> int:
        return self._spell_power
    
    @mana.setter
    def mana(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Мана должна быть целым числом")
        if value < 0 or value > 200:
            raise ValueError("Мана должна быть от 0 до 200")
        self._mana = value
    
    @spell_power.setter
    def spell_power(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Сила заклинаний должна быть целым числом")
        if value < 1 or value > 100:
            raise ValueError("Сила заклинаний должна быть от 1 до 100")
        self._spell_power = value
    
    def cast_spell(self) -> int:
        if self._mana < 20:
            print(f"{self.nickname}: Недостаточно маны!")
            return 0
        self._mana -= 20
        damage = self._spell_power + self.level * 2
        print(f"{self.nickname} колдует Огненный шар! Урон: {damage}")
        return damage
    
    def gain_experience(self, exp: int) -> bool:
        leveled_up = super().gain_experience(exp)
        if leveled_up:
            self._mana += 30
            print(f"{self.nickname} повысил уровень! Мана: {self._mana}")
        return leveled_up
    
    def calculate_power(self) -> int:
        return self.level * 8 + self.spell_power + self.mana // 2
    
    def get_specialization(self) -> str:
        return f"Маг | Мана: {self.mana} | Сил.закл: {self.spell_power}"
    
    def __str__(self) -> str:
        return f"{super().__str__()} | Мана:{self.mana} СЗ:{self.spell_power}"


class Archer(Player):    
    def __init__(self, nickname: str, level: int = 1, health: int = 100,
                 experience: int = 0, agility: int = 25, critical_chance: int = 15):
        super().__init__(nickname, "archer", level, health, experience)
        self.agility = agility
        self.critical_chance = critical_chance
    
    @property
    def agility(self) -> int:
        return self._agility
    
    @property
    def critical_chance(self) -> int:
        return self._critical_chance
    
    @agility.setter
    def agility(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Ловкость должна быть целым числом")
        if value < 1 or value > 100:
            raise ValueError("Ловкость должна быть от 1 до 100")
        self._agility = value
    
    @critical_chance.setter
    def critical_chance(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Шанс крита должен быть целым числом")
        if value < 0 or value > 50:
            raise ValueError("Шанс крита должен быть от 0 до 50")
        self._critical_chance = value
    
    def precision_shot(self) -> int:
        damage = self._agility * 2
        if self._critical_chance > 10:
            damage = int(damage * 1.5)
            print(f"{self.nickname} наносит КРИТИЧЕСКИЙ выстрел! Урон: {damage}")
        else:
            print(f"{self.nickname} стреляет из лука! Урон: {damage}")
        return damage
    
    def take_damage(self, damage: int) -> int:
        dodge_chance = self._agility // 10
        if dodge_chance > 20:
            print(f"{self.nickname} уклоняется от атаки!")
            return self.health
        return super().take_damage(damage)
    
    def calculate_power(self) -> int:
        return self.level * 9 + self.agility * 2 + self.critical_chance
    
    def get_specialization(self) -> str:
        return f"Лучник | Ловкость: {self.agility} | Крит: {self.critical_chance}%"
    
    def __str__(self) -> str:
        return f"{super().__str__()} | Лвк:{self.agility} Крит:{self.critical_chance}%"