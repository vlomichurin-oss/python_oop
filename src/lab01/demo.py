from model import Player

def main():
    print("Демонстрация работы класса PLayer")

    # --- 1. Создание объектов и вывод через print ---
    print("\n--- 1. Создание объектов и вывод ---")

    try:
        player1 = Player("MaxVerstappen", "mage", level=10, health=200, experience=5000)

        print("Создан игрок")
        print(f"  {player1}")

        # Демонстрация __repr__
        print("\nПредставление для отладки (__repr__):")
        print(f"  {repr(player1)}")

    except Exception as e:
        print(f"Ошибка при создании игроков: {e}")

    # --- 2. Сравнение двух объектов (__eq__) ---
    print("\n--- 2. Сравнение объектов ---")

    player2 = Player("MaxVerstappen", "warrior", level=2, health=80, experience=100)
    player3 = Player("MaxVerstappen", "warrior", level=5, health=150, experience=1200)  # Тот же ник и класс
    player4 = Player("FernandoAlonso", "warrior", level=1, health=50, experience=0)

    print(f"player1: {player1.nickname} ({player1.player_class})")
    print(f"player2: {player2.nickname} ({player2.player_class})")
    print(f"player3: {player3.nickname} ({player3.player_class})")
    print(f"player4: {player4.nickname} ({player4.player_class})")

    print(f"\nplayer1 == player2? {'Да' if player1 == player2 else 'Нет'} (должно быть Да - одинаковые ник и класс)")
    print(f"player1 == player3? {'Да' if player1 == player3 else 'Нет'} (должно быть Да - одинаковые ник и класс)")
    print(f"player1 == player4? {'Да' if player1 == player4 else 'Нет'} (должно быть Нет - разный ник)")

    # --- 3. Пример некорректного создания (через try/except) ---
    print("\n--- 3. Валидация ---")

    test_cases = [
        ("Слишком короткий ник", {"nickname": "A", "player_class": "warrior"}),
        ("Неизвестный класс", {"nickname": "Test", "player_class": "paladin"}),
        ("Отрицательный уровень", {"nickname": "Test", "player_class": "mage", "level": -5}),
        ("Уровень выше максимума", {"nickname": "Test", "player_class": "mage", "level": 101}),
        ("Отрицательное здоровье", {"nickname": "Test", "player_class": "warrior", "health": -10}),
        ("Отрицательный опыт", {"nickname": "Test", "player_class": "archer", "experience": -100}),
        ("Никнейм - число", {"nickname": 12345, "player_class": "healer"}),
    ]

    for description, kwargs in test_cases:
        try:
            print(f"\nПопытка: {description}")
            player = Player(**kwargs)
            print(f"  УСПЕХ (неожиданно): {player}")
        except (TypeError, ValueError) as e:
            print(f"  ОШИБКА (как и ожидалось): {e.__class__.__name__}: {e}")

    # --- 4. Изменение свойства через setter ---
    print("\n--- 4. Изменение свойств через SETTER ---")

    try:
        player = Player("Kimi", "mage", level=1, health=100, experience=0)
        print(f"Начальное состояние: {player}")

        # Корректное изменение
        player.health = 150
        print(f"После изменения здоровья на 150: {player}")

        player.level = 5
        print(f"После изменения уровня на 5: {player}")

        # Попытка некорректного изменения
        print("\nПопытка установить отрицательное здоровье:")
        player.health = -50
    except (TypeError, ValueError) as e:
        print(f"  ОШИБКА (корректно перехвачена): {e.__class__.__name__}: {e}")

    # --- 5. Проверка, что ограничение работает ---
    print("\n--- 5. Проверка ограничений ---")

    try:
        player = Player("ValidName", "warrior", level=1, health=100, experience=0)
        print(f"Исходный игрок: {player}")

        print("\nПытаемся установить уровень 150 (превышает max_level=100):")
        player.level = 150
    except ValueError as e:
        print(f"  ОШИБКА: {e}")

    # --- 6. Доступ к атрибуту класса через класс и экземпляр ---
    print("\n--- 6. ДОСТУП К АТРИБУТАМ КЛАССА ---")

    print(f"Через класс Player.available_classes: {Player.available_classes}")
    print(f"Через класс Player.max_level: {Player.max_level}")

    player = Player("Demo", "healer", level=1, health=100, experience=0)
    print(f"\nЧерез экземпляр player.available_classes: {player.available_classes}")
    print(f"Через экземпляр player.max_level: {player.max_level}")

    # Изменение атрибута класса через класс влияет на все экземпляры
    print(f"\nТекущий max_level: {Player.max_level}")
    Player.max_level = 150
    print(f"После изменения Player.max_level = 150")
    print(f"Новый max_level через класс: {Player.max_level}")
    print(f"Новый max_level через экземпляр player: {player.max_level}")

    # Возвращаем обратно для чистоты
    Player.max_level = 100

    # --- 7. Демонстрация бизнес-методов ---
    print("\n--- 7. Бизнес-методы ---")

    hero = Player("CristianHorner", "warrior", level=1, health=100, experience=0)
    print(f"Новый герой: {hero}")

    # Получение урона
    print("\n--- Получение урона ---")
    hero.take_damage(30)
    print(f"После урона 30: {hero}")
    print(f"Жив? {'Да' if hero.is_alive() else 'Нет'}")

    hero.take_damage(80)
    print(f"После урона 80: {hero}")
    print(f"Жив? {'Да' if hero.is_alive() else 'Нет'}")

    # Получение опыта и повышение уровня
    print("\n--- Получение опыта и повышение уровня ---")
    hero = Player("LevelUpHero", "mage", level=1, health=100, experience=0)
    print(f"Начинаем: {hero}")

    exp_gains = [200, 500, 800, 1500]
    for i, exp in enumerate(exp_gains, 1):
        print(f"\nШаг {i}: получаем {exp} опыта")
        leveled_up = hero.gain_experience(exp)
        if leveled_up:
            print(f"  🎉 УРОВЕНЬ ПОВЫШЕН!")
        print(f"  Текущее состояние: {hero}")

if __name__ == "__main__":
    main()