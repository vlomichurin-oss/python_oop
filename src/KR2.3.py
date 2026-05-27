import random
from abc import ABC, abstractmethod
from typing import List

class InsufficientManaError(Exception):
    pass

class AttackStrategy(ABC):
    @abstractmethod
    def attack(self, attacker, target) -> int:
        pass
    
    def __call__(self, attacker, target) -> int:
        return self.attack(attacker, target)

class SwordAttack(AttackStrategy):
    def __init__(self, damage: int):
        if damage <= 0: raise ValueError("damage > 0")
        self.damage = damage
    
    def attack(self, attacker, target) -> int:
        target.take_damage(self.damage)
        return self.damage

class BowAttack(AttackStrategy):
    def __init__(self, damage: int, accuracy: float):
        if damage <= 0: raise ValueError("damage > 0")
        if not (0 <= accuracy <= 1): raise ValueError("accuracy от 0 до 1")
        self.damage, self.accuracy = damage, accuracy
    
    def attack(self, attacker, target) -> int:
        if random.random() < self.accuracy:
            target.take_damage(self.damage)
            return self.damage
        return 0

class MagicAttack(AttackStrategy):
    def __init__(self, damage: int, mana_cost: int):
        if damage <= 0: raise ValueError("damage > 0")
        if mana_cost <= 0: raise ValueError("mana_cost > 0")
        self.damage, self.mana_cost = damage, mana_cost
    
    def attack(self, attacker, target) -> int:
        if attacker.experience < self.mana_cost:
            raise InsufficientManaError(f"Нужно {self.mana_cost}, есть {attacker.experience}")
        attacker._experience -= self.mana_cost
        target.take_damage(self.damage)
        return self.damage

class CriticalAttack(AttackStrategy):
    def __init__(self, base_damage: int, crit_multiplier: float = 2.0):
        if base_damage <= 0: raise ValueError("base_damage > 0")
        self.base_damage, self.crit_multiplier = base_damage, crit_multiplier
    
    def attack(self, attacker, target) -> int:
        damage = self.base_damage * (self.crit_multiplier if attacker.level % 2 == 0 else 1)
        damage = int(damage)
        target.take_damage(damage)
        return damage

class Character:
    def __init__(self, name, max_health, level=1, experience=0):
        self._attack_strategy = None
        self.name = name.strip()
        if not self.name: raise ValueError("имя пустое")
        if max_health <= 0: raise ValueError("max_health > 0")
        self._max_health = max_health
        self._health = max_health
        if not (1 <= level <= 100): raise ValueError("уровень от 1 до 100")
        self._level = level
        if experience < 0: raise ValueError("опыт >= 0")
        self._experience = experience
    
    @property
    def name(self): return self._name
    @name.setter
    def name(self, v): self._name = v.strip()
    
    @property
    def health(self): return self._health
    @health.setter
    def health(self, v): self._health = max(0, min(v, self._max_health))
    
    @property
    def max_health(self): return self._max_health
    
    @property
    def level(self): return self._level
    @level.setter
    def level(self, v): self._level = v
    
    @property
    def experience(self): return self._experience
    @experience.setter
    def experience(self, v): self._experience = v
    
    def take_damage(self, amount):
        if amount <= 0: raise ValueError("amount > 0")
        self.health = self.health - amount
    
    def heal(self, amount):
        if amount <= 0: raise ValueError("amount > 0")
        self.health = self.health + amount
    
    def gain_xp(self, amount):
        if amount <= 0: raise ValueError("amount > 0")
        self._experience += amount
        while self._experience >= self._level * 100 and self._level < 100:
            self._experience -= self._level * 100
            self._level += 1
        if self._level >= 100: self._experience = 0
    
    def is_alive(self): return self._health > 0
    
    def set_attack_strategy(self, strategy):
        if not isinstance(strategy, AttackStrategy):
            raise ValueError("нужен экземпляр AttackStrategy")
        self._attack_strategy = strategy
    
    def attack(self, target):
        if self._attack_strategy is None:
            raise ValueError("не установлена стратегия атаки")
        if not self.is_alive(): raise ValueError("мёртвый не атакует")
        if not target.is_alive(): raise ValueError("цель мертва")
        return self._attack_strategy.attack(self, target)
    
    def __str__(self):
        return f"Воин (уровень {self._level}): {self._health}/{self._max_health} HP, XP {self._experience}"
    
    def __eq__(self, other):
        return isinstance(other, Character) and self.name == other.name

class Party:
    def __init__(self, characters: List[Character] = None):
        self._members = list(characters) if characters else []
    
    def add(self, character: Character):
        self._members.append(character)
    
    def alive_members(self) -> List[Character]:
        return [m for m in self._members if m.is_alive()]
    
    def battle(self, other_party):
        while self.alive_members() and other_party.alive_members():
            for attacker in self.alive_members():
                targets = other_party.alive_members()
                if not targets: break
                try:
                    attacker.attack(random.choice(targets))
                except (InsufficientManaError, ValueError):
                    pass
            
            if not other_party.alive_members(): break
            
            for attacker in other_party.alive_members():
                targets = self.alive_members()
                if not targets: break
                try:
                    attacker.attack(random.choice(targets))
                except (InsufficientManaError, ValueError):
                    pass


if __name__ == "__main__":
    hero = Character('Воин', 100, 5, 200)
    mage = Character('Маг', 80, 3, 350)
    orc = Character('Орк', 120, 4, 100)
    
    hero.set_attack_strategy(SwordAttack(20))
    hero.attack(orc)
    print(f"Здоровье орка: {orc.health}")  # 100
    
    mage.set_attack_strategy(MagicAttack(50, 100))
    mage.attack(orc)
    print(f"Здоровье орка: {orc.health}")  # 50
    print(f"Опыт мага: {mage.experience}")  # 250
    
    try:
        mage.set_attack_strategy(MagicAttack(50, 9999))
        mage.attack(orc)
    except InsufficientManaError as e:
        print(f"Ошибка: {e}")
    
    hero.set_attack_strategy(SwordAttack(25))
    mage.set_attack_strategy(MagicAttack(40, 80))
    orc.set_attack_strategy(SwordAttack(30))
    
    good = Party([hero, mage])
    evil = Party([orc])
    good.battle(evil)
    print(f"Орк жив? {orc.is_alive()}")  # False