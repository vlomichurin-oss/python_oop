import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab03.base import Player
from lab03.models import Warrior, Mage, Archer
from lab02.collection import PlayerCollection


def main():
    print("Лабораторная работа №3 - Наследование и Полиморфизм")
    
    # ===== СЦЕНАРИЙ 1: Создание объектов разных типов =====
    print("\n[Сценарий 1] Создание объектов")
    w = Warrior("Торин", level=5, strength=40, defense=20)
    m = Mage("Гэндальф", level=5, mana=150, spell_power=45)
    a = Archer("Леголас", level=5, agility=35, critical_chance=20)
    print(w)
    print(m)
    print(a)
    
    # ===== СЦЕНАРИЙ 2: Использование методов =====
    print("\n[Сценарий 2] Новые методы")
    print(f"Тяжелая атака: {w.heavy_attack()} урона")
    print(f"Заклинание: {m.cast_spell()} урона (мана: {m.mana})")
    print(f"Точный выстрел: {a.precision_shot()} урона")
    
    # ===== СЦЕНАРИЙ 3: Переопределенные методы =====
    print("\n[Сценарий 3] Переопределенные методы")
    w.take_damage(60)
    print(f"Воин после урона: {w.health} HP")
    m.gain_experience(5000)
    print(f"Маг после опыта: ур.{m.level}, мана {m.mana}")
    
    # ===== СЦЕНАРИЙ 4: Полиморфизм =====
    print("\n[Сценарий 4] Полиморфизм (один метод - разное поведение)")
    for p in [w, m, a]:
        print(f"  {p.nickname:10} сила: {p.calculate_power()}")
    
    # ===== СЦЕНАРИЙ 5: Проверка типов =====
    print("\n[Сценарий 5] isinstance()")
    print(f"Торин - Warrior: {isinstance(w, Warrior)}")
    print(f"Торин - Player: {isinstance(w, Player)}")
    print(f"Гэндальф - Mage: {isinstance(m, Mage)}")
    
    # ===== СЦЕНАРИЙ 6: Коллекция из ЛР-2 =====
    print("\n[Сценарий 6] Интеграция с коллекцией")
    col = PlayerCollection()
    col.add(w)
    col.add(m)
    col.add(a)
    col.add(Warrior("Артас", level=8, strength=50))
    col.add(Mage("Мерлин", level=7, mana=180))
    print(f"Коллекция содержит {len(col)} персонажей")
    
    # ===== СЦЕНАРИЙ 7: Фильтрация по типу =====
    print("\n[Сценарий 7] Фильтрация коллекции")
    warriors = [p for p in col if isinstance(p, Warrior)]
    mages = [p for p in col if isinstance(p, Mage)]
    archers = [p for p in col if isinstance(p, Archer)]
    print(f"Воины ({len(warriors)}): {[p.nickname for p in warriors]}")
    print(f"Маги ({len(mages)}): {[p.nickname for p in mages]}")
    print(f"Лучники ({len(archers)}): {[p.nickname for p in archers]}")
    
    # ===== СЦЕНАРИЙ 8: Один метод для всей коллекции =====
    print("\n[Сценарий 8] calculate_power() для всех")
    for p in col:
        print(f"  {p.nickname:10} сила: {p.calculate_power():3} | {p.get_specialization()}")
    


if __name__ == "__main__":
    main()