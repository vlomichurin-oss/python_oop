from strategies import *
from collection import PlayerCollection


# ===== КЛАССЫ ИГРОКОВ =====

class Player:
    available_classes = ("warrior", "mage", "archer", "healer")
    max_level = 100
    base_experience = 1000
    
    def __init__(self, nickname, player_class, level=1, health=100, experience=0):
        self.nickname = nickname
        self.player_class = player_class
        self.level = level
        self.health = health
        self.experience = experience
    
    def is_alive(self):
        return self.health > 0
    
    def calculate_power(self):
        return self.level * 10
    
    def get_specialization(self):
        return self.player_class
    
    def __str__(self):
        return f"{self.nickname} [{self.player_class}] Lvl:{self.level} HP:{self.health}"


class Warrior(Player):
    def __init__(self, nickname, level=1, health=120, experience=0):
        super().__init__(nickname, "warrior", level, health, experience)
    
    def calculate_power(self):
        return self.level * 12 + 20


class Mage(Player):
    def __init__(self, nickname, level=1, health=80, experience=0):
        super().__init__(nickname, "mage", level, health, experience)


class Archer(Player):
    def __init__(self, nickname, level=1, health=90, experience=0):
        super().__init__(nickname, "archer", level, health, experience)


class Healer(Player):
    def __init__(self, nickname, level=1, health=70, experience=0):
        super().__init__(nickname, "healer", level, health, experience)


# ===== СОЗДАНИЕ КОЛЛЕКЦИИ =====

def create_players():
    col = PlayerCollection()
    players = [
        Warrior("Max", 15, 150),
        Warrior("Kimi", 50, 180),
        Mage("Carlos", 30, 80),
        Mage("Oscar", 25, 70),
        Archer("Toto", 20, 90),
        Healer("Niko", 12, 60),
    ]
    for p in players:
        col.add(p)
    return col


# ===== ДЕМОНСТРАЦИЯ =====

def main():
    print("Лабораторная работа №5")
    
    players = create_players()
    
    # 1. СОРТИРОВКА (3 стратегии)
    print("\n1. Сортировка:")
    
    print("  По никнейму:")
    col = PlayerCollection(players.get_all())
    col.sort_by(by_nickname)
    for p in col:
        print(f"    - {p.nickname}")
    
    print("\n  По уровню:")
    col = PlayerCollection(players.get_all())
    col.sort_by(by_level, reverse=True)
    for p in col:
        print(f"    - {p.nickname}: {p.level} lvl")
    
    print("\n  По силе:")
    col = PlayerCollection(players.get_all())
    col.sort_by(by_power)
    for p in col:
        print(f"    - {p.nickname}: сила {p.calculate_power()}")
    
    # 2. ФИЛЬТРАЦИЯ (2 фильтра)
    print("\n2. Фильтрация:")
    
    print("  Игроки с уровнем >= 20:")
    filtered = players.filter_by(lambda p: p.level >= 20)
    for p in filtered:
        print(f"    - {p.nickname} (lvl {p.level})")
    
    print("\n  Игроки класса warrior или mage:")
    filtered = players.filter_by(lambda p: p.player_class in ('warrior', 'mage'))
    for p in filtered:
        print(f"    - {p.nickname} [{p.player_class}]")
    
    # 3. MAP (преобразование)
    print("\n3. Map:")
    
    print("  Никнеймы всех игроков:")
    nicknames = players.map_to(lambda p: p.nickname)
    print(f"    {nicknames}")
    
    print("\n  Сила всех игроков:")
    powers = players.map_to(lambda p: f"{p.nickname}: {p.calculate_power()}")
    for power in powers:
        print(f"    - {power}")
    
    # 4. ФАБРИКА ФУНКЦИЙ
    print("\n4. Фабрика функций:")
    
    filter_lvl_20 = make_level_filter(20)
    filter_lvl_25 = make_level_filter(25)
    
    print(f"  Игроки с уровнем >= 20: {[p.nickname for p in players.filter_by(filter_lvl_20)]}")
    print(f"  Игроки с уровнем >= 25: {[p.nickname for p in players.filter_by(filter_lvl_25)]}")
    
    # 5. МЕТОДЫ КОЛЛЕКЦИИ
    print("\n5. Методы коллекций (sort_by + filter_by):")
    
    result = (PlayerCollection(players.get_all())
              .filter_by(lambda p: p.level >= 15)
              .sort_by(by_power, reverse=True))
    
    print(f"  Игроки с уровнем >= 15, по убыванию силы:")
    for p in result:
        print(f"    - {p.nickname}: lvl {p.level}, сила {p.calculate_power()}")
    
    # 6. CALLABLE-СТРАТЕГИИ
    print("\n6. Callable-стратегии:")
    
    boost = PowerBoostStrategy(0.2)
    print("  Усиление силы на 20%:")
    for p in players[:3]:
        old = p.calculate_power()
        new = boost(p)
        print(f"    - {p.nickname}: {old} → {new}")
    
    # 7. APPLY
    print("\n7. Apply:")
    
    test = PlayerCollection(players.get_all()[:3])
    print("  До лечения:")
    for p in test:
        print(f"    - {p.nickname}: {p.health} HP")
    
    test.apply(lambda p: setattr(p, 'health', p.health + 30))
    
    print("  После лечения (+30 HP):")
    for p in test:
        print(f"    - {p.nickname}: {p.health} HP")
    
    # 8. ЦЕПОЧКА ОПЕРАЦИЙ
    print("\n8. Цепочка операций (filter → sort → apply):")
    
    result = (PlayerCollection(players.get_all())
              .filter_by(lambda p: p.level >= 10)
              .sort_by(by_level)
              .apply(lambda p: setattr(p, 'health', min(p.health + 50, 200))))
    
    print("  После цепочки (level>=10, сортировка, +50 HP):")
    for p in result:
        print(f"    - {p.nickname}: lvl {p.level}, HP {p.health}")
    
    # 9. СРАВНЕНИЕ lambda и именованной функции
    print("\n9. Сравнение lambda vs Именованная функция:")
    
    print("  Через lambda:")
    sorted_lambda = sorted(players, key=lambda p: p.level, reverse=True)
    for p in sorted_lambda[:3]:
        print(f"    - {p.nickname}: {p.level} lvl")
    
    print("  Через именованную функцию by_level:")
    sorted_named = sorted(players, key=by_level, reverse=True)
    for p in sorted_named[:3]:
        print(f"    - {p.nickname}: {p.level} lvl")
    


if __name__ == "__main__":
    main()