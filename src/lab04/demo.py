from models import Player, NPC, PlayerCollection
from interfaces import Printable, Comparable, Identifiable


print("Лабораторная работа №4 - Интерфейсы и абстрактные классы")

# ===== ЧАСТЬ 1: РАЗНАЯ РЕАЛИЗАЦИЯ =====
print("\n1. Разная реализация методов")

player = Player("Hero", "Warrior", 10, 1)
npc = NPC("Merchant", "merchant", 7)

print("\nМетод to_string():")
print("  Player: " + player.to_string())
print("  NPC:    " + npc.to_string())

print("\nМетод get_id():")
print("  Player: " + player.get_id())
print("  NPC:    " + npc.get_id())

# ===== ЧАСТЬ 2: ПРОВЕРКА isinstance =====
print("\n2. Проверка isinstance")

print("  Player is Printable? " + str(isinstance(player, Printable)))
print("  NPC is Printable? " + str(isinstance(npc, Printable)))

# ===== ЧАСТЬ 3: РАБОТА С КОЛЛЕКЦИЕЙ =====
print("\n3. Работа с коллекцией")

collection = PlayerCollection()
collection.add(Player("Max", "Warrior", 30, 85))
collection.add(Player("Fernando", "Mage", 25, 100))
collection.add(Player("Lando", "Archer", 20, 45))

print("  Всего игроков: " + str(len(collection)))

print("\n  Printable объекты в коллекции:")
for item in collection.get_printable_items():
    print("    " + item.to_string())

# ===== ЧАСТЬ 4: СОРТИРОВКА =====
print("\n4. Сортировка через Comparable")

print("  До сортировки:")
for p in collection.get_all():
    print("    " + p.nickname + " - уровень " + str(p.level))

collection.sort_by_comparable()

print("  После сортировки:")
for p in collection.get_all():
    print("    " + p.nickname + " - уровень " + str(p.level))

# ===== ЧАСТЬ 5: ПОЛИМОРФИЗМ =====
print("\n5. Полиморфизм через интерфейс")

def show_all(items):
    for item in items:
        print("  " + item.to_string())

objects = [
    Player("Kimi", "Warrior", 15, 100),
    NPC("Blacksmith", "merchant", 6),
    Player("Cristian", "Mage", 20, 100),
    NPC("Elder", "quest", 9)
]

show_all(objects)
