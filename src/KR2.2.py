class Character:
    def __init__(self, name, max_health, level=1, experience=0):
        self._name = None
        self._max_health = None
        self._health = None
        self._level = None
        self._experience = None
        
        self.name = name
        self.max_health = max_health
        self.health = max_health  
        self.level = level
        self.experience = experience
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        name_stripped = value.strip()
        if not name_stripped:
            raise ValueError("имя пустое")
        self._name = name_stripped
    
    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, value):
        self._health = value
    
    @property
    def max_health(self):
        return self._max_health
    
    @max_health.setter
    def max_health(self, value):
        if value <= 0:
            raise ValueError("max_health > 0")
        self._max_health = value
    
    @property
    def level(self):
        return self._level
    
    @level.setter
    def level(self, value):
        if not (1 <= value <= 100):
            raise ValueError("уровень должен быть от 1 до 100")
        self._level = value
    
    @property
    def experience(self):
        return self._experience
    
    @experience.setter
    def experience(self, value):
        if value < 0:
            raise ValueError("опыт не может быть отрицательным")
        self._experience = value
    
    def take_damage(self, amount):
        if amount <= 0:
            raise ValueError("amount > 0")
        self.health = max(0, self.health - amount)
    
    def heal(self, amount):
        if amount <= 0:
            raise ValueError("amount > 0")
        self.health = min(self.max_health, self.health + amount)
    
    def gain_xp(self, amount):
        if amount <= 0:
            raise ValueError("amount > 0")
        self.experience += amount
        
        while self.experience >= self.level * 100:
            if self.level >= 100:
                self.experience = 0
                break
            self.experience -= self.level * 100
            self.level += 1
    
    def is_alive(self):
        return self.health > 0
    
    def __str__(self):
        return f"Воин (уровень {self.level}): {self.health}/{self.max_health} HP, XP {self.experience}"
    
    def __eq__(self, other):
        if not isinstance(other, Character):
            return False
        return self.name == other.name


if __name__ == "__main__":
    hero = Character('Воин', 100, 1, 0)
    hero.take_damage(30)
    print(hero.health)  # 70
    hero.heal(20)
    print(hero.health)  # 90
    hero.gain_xp(150)
    print(hero.level)   # 2 (преодолел 100)
    print(hero.experience)  # 50
    
    # Проверка валидации:
    Character('', 100)  # ValueError: имя пустое
    Character('Воин', 0)  # ValueError: max_health > 0
    hero.take_damage(-5)  # ValueError: amount > 0