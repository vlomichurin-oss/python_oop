from container import TypedCollection, Displayable, Scorable


class Player:
    available_classes = ("warrior", "mage", "archer", "healer")
    max_level = 100
    base_experience = 1000
    
    def __init__(self, nickname: str, player_class: str, level: int = 1, health: int = 100):
        self._nickname = nickname
        self._player_class = player_class
        self._level = level
        self._health = health
        self._experience = 0
    
    @property
    def nickname(self) -> str:
        return self._nickname
    
    @property
    def level(self) -> int:
        return self._level
    
    def is_alive(self) -> bool:
        return self._health > 0
    
    def calculate_power(self) -> int:
        return self._level * 10
    
    def display(self) -> str:
        return f"{self._nickname} [{self._player_class}] ур.{self._level}"
    
    def score(self) -> float:
        return float(self.calculate_power())
    
    def __str__(self) -> str:
        return self.display()


class Warrior(Player):
    def __init__(self, nickname: str, level: int = 1, strength: int = 20, defense: int = 15):
        super().__init__(nickname, "warrior", level, 150)
        self._strength = strength
        self._defense = defense
    
    def calculate_power(self) -> int:
        return self.level * 10 + self._strength + self._defense
    
    def display(self) -> str:
        return f"[Воин] {self.nickname} ур.{self.level}"
    
    def score(self) -> float:
        return float(self.calculate_power())


class Mage(Player):
    def __init__(self, nickname: str, level: int = 1, mana: int = 100, spell_power: int = 25):
        super().__init__(nickname, "mage", level, 80)
        self._mana = mana
        self._spell_power = spell_power
    
    def calculate_power(self) -> int:
        return self.level * 8 + self._spell_power + self._mana // 2
    
    def display(self) -> str:
        return f"[Маг] {self.nickname} ур.{self.level}"
    
    def score(self) -> float:
        return float(self.calculate_power())


class Archer(Player):
    def __init__(self, nickname: str, level: int = 1, agility: int = 25, critical_chance: int = 15):
        super().__init__(nickname, "archer", level, 100)
        self._agility = agility
        self._critical_chance = critical_chance
    
    def calculate_power(self) -> int:
        return self.level * 9 + self._agility * 2 + self._critical_chance
    
    def display(self) -> str:
        return f"[Лучник] {self.nickname} ур.{self.level}"
    
    def score(self) -> float:
        return float(self.calculate_power())



def main():
    print("Лабораторная работа №6")
    

    print("\nБазовая работа TypedCollection")
    print("-" * 35)
    
    warriors: TypedCollection[Warrior] = TypedCollection()
    
    warriors.add(Warrior("Исак", 5, 30, 20))
    warriors.add(Warrior("Шарль", 8, 40, 25))
    warriors.add(Warrior("Оливер", 3, 15, 10))
    
    print("Добавлены воины:")
    for w in warriors.get_all():
        print(f"  {w.display()}")
    
    print(f"\nВсего воинов: {len(warriors)}")
    warriors.remove_at(1)
    print(f"После удаления: {len(warriors)} воинов")
    

    print("\nМетоды find, filter, map")
    print("-" * 35)
    
    mages: TypedCollection[Mage] = TypedCollection()
    mages.add(Mage("Макс", 10, 200, 50))
    mages.add(Mage("Фернандо", 9, 180, 45))
    mages.add(Mage("Льюис", 5, 140, 30))
    mages.add(Mage("Оскар", 7, 160, 38))
    
    # find
    found = mages.find(lambda m: m.level > 8)
    print(f"find (уровень > 8): {found.display() if found else 'None'}")
    
    not_found = mages.find(lambda m: m.level > 15)
    print(f"find (уровень > 15): {not_found}")
    
    # filter
    high_level = mages.filter(lambda m: m.level >= 7)
    print(f"\nfilter (уровень >= 7): {len(high_level)} магов")
    for m in high_level:
        print(f"  {m.nickname} (ур.{m.level})")
    
    # map со сменой типа
    names: list[str] = mages.map(lambda m: m.nickname)
    levels: list[int] = mages.map(lambda m: m.level)
    powers: list[float] = mages.map(lambda m: m.calculate_power())
    
    print(f"\nmap -> имена (list[str]): {names}")
    print(f"map -> уровни (list[int]): {levels}")
    print(f"map -> сила (list[float]): {powers}")
    
    
    print("\nПротоколы Displayable и Scorable")
    print("-" * 35)
    
    # Сценарий 1: TypedCollection[D] с разными типами
    displayable_col: TypedCollection[Displayable] = TypedCollection()
    
    displayable_col.add(Warrior("Кими", 6, 25, 18))
    displayable_col.add(Mage("Джордж", 5, 150, 35))
    displayable_col.add(Archer("Тото", 4, 30, 20))
    displayable_col.add(Player("Нагибатор", "warrior", 2))
    
    print("Коллекция Displayable (разные типы):")
    for obj in displayable_col.get_all():
        print(f"  {obj.display()}")
    
    # Сценарий 2: TypedCollection[S]
    scorable_col: TypedCollection[Scorable] = TypedCollection()
    scorable_col.add(Warrior("Кими", 6, 25, 18))
    scorable_col.add(Mage("Джордж", 5, 150, 35))
    scorable_col.add(Archer("Тото", 4, 30, 20))
    
    print("\nКоллекция Scorable - вызов score():")
    for obj in scorable_col.get_all():
        print(f"  {type(obj).__name__}.score() = {obj.score()}")
    
    # Использование find с протоколом
    best = scorable_col.find(lambda obj: obj.score() > 60)
    if best:
        print(f"\nОбъект с score > 60: {best.display()} (score: {best.score()})")
    
    # Использование map с протоколом
    all_scores = scorable_col.map(lambda obj: obj.score())
    print(f"Все значения score: {all_scores}")
    

if __name__ == "__main__":
    main()