# Лабораторная работа №1. Вариант 6.
Реализован класс Player
## Цель работы

* Освоить объявление пользовательских классов.
* Разобраться с инкапсуляцией (атрибуты экземпляра, закрытые поля).
* Реализовать свойства (`@property`).
* Переопределить магические методы (`__str__`, `__repr__`, `__eq__`).
* Осознать разницу между атрибутами класса и экземпляра.
## Атрибуты класса
```
class Player:
    available_classes = ("warrior", "mage", "archer", "healer")
    max_level = 100
    base_experience = 1000


    def __init__(self, nickname: str, player_class: str, level: int = 1, health: int = 100, experience: int = 0):
        self.nickname = nickname
        self.player_class = player_class
        self.level = level
        self.health = health
        self.experience = experience
```
## Декаратор
```
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
```
## Метод валидации
```
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
        # Здоровье может быть больше 100, если есть баффы
        self._health = value

    @experience.setter
    def experience(self, value: int):
        """Сеттер для опыта. Проверяет тип и неотрицательность."""
        if not isinstance(value, int):
            raise TypeError("Опыт должен быть целым числом.")
        if value < 0:
            raise ValueError("Опыт не может быть отрицательным.")
        self._experience = value
```
## Бизнес методы
- **`take_damage`** - Нанесение урона
- **`gain_experience`** - Получение опыта
- **`is_alive`** - Проверка жизни
```
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

        # Проверяем, не пора ли повысить уровень
        # Формула: для повышения с n до n+1 нужно n * base_experience опыта
        while self._experience >= self._level * Player.base_experience and self._level < Player.max_level:
            self._experience -= self._level * Player.base_experience
            self._level += 1
            leveled_up = True
            # При повышении уровня здоровье увеличивается
            self._health += 20

        return leveled_up

    def is_alive(self) -> bool:
        return self._health > 0
```
## Магические методы
- **`__str__`** — вызывается при попытке преобразовать объект в строку (например, функциями print() или str()). Предназначен для создания понятного человеку описания объекта.
- **`__repr__`** — возвращает формальное строковое представление объекта, которое удобно для отладки и логирования. В идеале это представление должно быть таким, чтобы его можно было использовать для воссоздания объекта (или хотя бы чётко понимать его состояние).
- **`__eq__`** — определяет поведение оператора равенства ==. Позволяет задать, при каких условиях два объекта будут считаться равными.

```
    def __str__(self) -> str:
        status = "Жив" if self.is_alive() else "Мертв"
        return (f"👤 {self.nickname} | [{self.player_class}] | Ур. {self._level} | "
                f"❤️ {self._health} HP | ✨ {self._experience} XP | {status}")

    def __repr__(self) -> str:
        return (f"Player(nickname='{self.nickname}', player_class='{self.player_class}', "
                f"level={self._level}, health={self._health}, experience={self._experience})")

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Player):
            return False
        return (self.nickname == other.nickname and 
                self.player_class == other.player_class)
```
## Вывод
```
--- 1. Создание объектов и вывод ---
Создан игрок
  👤 MaxVerstappen | [mage] | Ур. 10 | ❤️ 200 HP | ✨ 5000 XP | Жив

Представление для отладки (__repr__):
  Player(nickname='MaxVerstappen', player_class='mage', level=10, health=200, experience=5000)

--- 2. Сравнение объектов ---
player1: MaxVerstappen (mage)
player2: MaxVerstappen (warrior)
player3: MaxVerstappen (warrior)
player4: FernandoAlonso (warrior)

player1 == player2? Нет (должно быть Да - одинаковые ник и класс)
player1 == player3? Нет (должно быть Да - одинаковые ник и класс)
player1 == player4? Нет (должно быть Нет - разный ник)

--- 3. Валидация ---

Попытка: Слишком короткий ник
  ОШИБКА (как и ожидалось): ValueError: Никнейм должен содержать минимум 3 символа.

Попытка: Неизвестный класс
  ОШИБКА (как и ожидалось): ValueError: Неизвестный класс 'paladin'. Допустимые классы: warrior, mage, archer, healer

Попытка: Отрицательный уровень
  ОШИБКА (как и ожидалось): ValueError: Уровень не может быть меньше 1.

Попытка: Уровень выше максимума
  ОШИБКА (как и ожидалось): ValueError: Уровень не может превышать 100.

Попытка: Отрицательное здоровье
  ОШИБКА (как и ожидалось): ValueError: Здоровье не может быть отрицательным.

Попытка: Отрицательный опыт
  ОШИБКА (как и ожидалось): ValueError: Опыт не может быть отрицательным.

Попытка: Никнейм - число
  ОШИБКА (как и ожидалось): TypeError: Никнейм должен быть строкой.

--- 4. Изменение свойств через SETTER ---
Начальное состояние: 👤 Kimi | [mage] | Ур. 1 | ❤️ 100 HP | ✨ 0 XP | Жив
После изменения здоровья на 150: 👤 Kimi | [mage] | Ур. 1 | ❤️ 150 HP | ✨ 0 XP | Жив
После изменения уровня на 5: 👤 Kimi | [mage] | Ур. 5 | ❤️ 150 HP | ✨ 0 XP | Жив

Попытка установить отрицательное здоровье:
  ОШИБКА (корректно перехвачена): ValueError: Здоровье не может быть отрицательным.

--- 5. Проверка ограничений ---
Исходный игрок: 👤 ValidName | [warrior] | Ур. 1 | ❤️ 100 HP | ✨ 0 XP | Жив

Пытаемся установить уровень 150 (превышает max_level=100):
  ОШИБКА: Уровень не может превышать 100.

--- 6. Доступ к атрибутам класса ---
Через класс Player.available_classes: ('warrior', 'mage', 'archer', 'healer')
Через класс Player.max_level: 100

Через экземпляр player.available_classes: ('warrior', 'mage', 'archer', 'healer')
Через экземпляр player.max_level: 100

Текущий max_level: 100
После изменения Player.max_level = 150
Новый max_level через класс: 150
Новый max_level через экземпляр player: 150

--- 7. Бизнес-методы ---
Новый герой: 👤 CristianHorner | [warrior] | Ур. 1 | ❤️ 100 HP | ✨ 0 XP | Жив

--- Получение урона ---
После урона 30: 👤 CristianHorner | [warrior] | Ур. 1 | ❤️ 70 HP | ✨ 0 XP | Жив
Жив? Да
После урона 80: 👤 CristianHorner | [warrior] | Ур. 1 | ❤️ 0 HP | ✨ 0 XP | Мертв
Жив? Нет

--- Получение опыта и повышение уровня ---
Начинаем: 👤 LevelUpHero | [mage] | Ур. 1 | ❤️ 100 HP | ✨ 0 XP | Жив

Шаг 1: получаем 200 опыта
  Текущее состояние: 👤 LevelUpHero | [mage] | Ур. 1 | ❤️ 100 HP | ✨ 200 XP | Жив

Шаг 2: получаем 500 опыта
  Текущее состояние: 👤 LevelUpHero | [mage] | Ур. 1 | ❤️ 100 HP | ✨ 700 XP | Жив

Шаг 3: получаем 800 опыта
  🎉 УРОВЕНЬ ПОВЫШЕН!
  Текущее состояние: 👤 LevelUpHero | [mage] | Ур. 2 | ❤️ 120 HP | ✨ 500 XP | Жив

Шаг 4: получаем 1500 опыта
  🎉 УРОВЕНЬ ПОВЫШЕН!
  Текущее состояние: 👤 LevelUpHero | [mage] | Ур. 3 | ❤️ 140 HP | ✨ 0 XP | Жив
```
