# src/lab02/demo.py
from model import Player
from collection import PlayerCollection


def demo_basic_operations():
    """базовые операции"""
    print("\n=== Базовые операции ===")
    
    players = PlayerCollection()
    
    p1 = Player("Max", "warrior", 10, 150)
    p2 = Player("Carlos", "mage", 8, 100)
    p3 = Player("Oscar", "warrior", 12, 200)
    
    players.add(p1)
    players.add(p2)
    players.add(p3)
    print(f"Добавлено {len(players)} игроков")
    print(players)
    
    players.remove(p2)
    print(f"После удаления {p2.nickname}: {len(players)} игроков")
    print(players)
    
    # проверка ошибок
    try:
        players.add("not player")
    except TypeError as e:
        print(f"Ошибка: {e}")
    
    try:
        players.add(Player("Arthas", "mage"))
    except ValueError as e:
        print(f"Ошибка: {e}")


def demo_search():
    """поиск"""
    print("\n=== Поиск ===")
    
    players = PlayerCollection()
    players.add(Player("Max", "warrior", 10))
    players.add(Player("Carlos", "mage", 8))
    players.add(Player("Oscar", "warrior", 12))
    
    found = players.find_by_nickname("Carlos")
    print(f"Поиск по никнейму 'Carlos': {found.nickname if found else None}")
    
    warriors = players.find_by_class("warrior")
    print(f"Поиск воинов: {[w.nickname for w in warriors]}")


def demo_sorting():
    """сортировка"""
    print("\n=== Сортировка ===")
    
    players = PlayerCollection()
    players.add(Player("Charles", "archer", 5))
    players.add(Player("Fernando", "warrior", 10))
    players.add(Player("Isack", "mage", 7))
    
    print("До сортировки:")
    print(players)
    
    players.sort_by_level()
    print("По уровню:")
    print(players)
    
    players.sort_by_nickname()
    print("По никнейму:")
    print(players)


def demo_filtering():
    """фильтрация"""
    print("\n=== Фильтрация ===")
    
    players = PlayerCollection()
    players.add(Player("Hero1", "warrior", 10, 100))
    players.add(Player("Hero2", "mage", 8, 0))
    players.add(Player("Hero3", "warrior", 12, 150))
    
    alive = players.get_alive()
    print(f"Живые игроки ({len(alive)}):")
    print(alive)
    
    warriors = players.get_by_class("warrior")
    print(f"Воины ({len(warriors)}):")
    print(warriors)


def demo_magic_methods():
    """магические методы"""
    print("\n=== Магические методы ===")
    
    players = PlayerCollection()
    players.add(Player("First", "warrior", 1))
    players.add(Player("Second", "mage", 2))
    players.add(Player("Third", "archer", 3))
    
    print(f"len() = {len(players)}")
    
    print("Итерация:")
    for p in players:
        print(f"  {p.nickname}")
    
    print(f"players[0] = {players[0].nickname}")
    print(f"players[-1] = {players[-1].nickname}")
    
    removed = players.remove_at(1)
    print(f"Удален по индексу 1: {removed.nickname}")
    print(f"Осталось: {len(players)}")


def main():
    print("ЛАБОРАТОРНАЯ РАБОТА №2")
    
    demo_basic_operations()
    demo_search()
    demo_sorting()
    demo_filtering()
    demo_magic_methods()
    
    print("\n=== Готово ===")


if __name__ == "__main__":
    main()