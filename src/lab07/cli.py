from typing import List, Optional
from .app import GameApp
from .exceptions import *


class GameCLI:
    def __init__(self, app: GameApp):
        self.app = app
    
    def run(self) -> None:
        """Запустить главный цикл приложения."""
        while True:
            self._show_menu()
            choice = self._get_choice()
            
            if choice == 0:
                print("\nДо свидания! Спасибо за игру!\n")
                break
            elif choice == 1:
                self._add_player()
            elif choice == 2:
                self._show_all_players()
            elif choice == 3:
                self._find_player()
            elif choice == 4:
                self._remove_player()
            elif choice == 5:
                self._filter_players()
            elif choice == 6:
                self._sort_players()
            elif choice == 7:
                self._show_stats()
            elif choice == 8:
                self._damage_player()
            elif choice == 9:
                self._add_experience()
            else:
                print("Неверный выбор! Попробуйте снова.")
    
    def _show_menu(self) -> None:
        print("\n" + "="*50)
        print("              GAME MANAGER")
        print("="*50)
        print("1. Добавить игрока")
        print("2. Показать всех игроков")
        print("3. Найти игрока")
        print("4. Удалить игрока")
        print("5. Фильтрация игроков")
        print("6. Сортировка игроков")
        print("7. Статистика")
        # print("8. Нанести урон")
        # print("9. Добавить опыт")
        print("0. Выход")
        print("="*50)
    
    def _get_choice(self) -> int:
        while True:
            try:
                choice = int(input("\nВыберите действие: "))
                return choice
            except ValueError:
                print("Ошибка: введите число!")
    
    def _get_input(self, prompt: str, required: bool = True) -> Optional[str]:
        value = input(prompt).strip()
        if required and not value:
            print("Это поле обязательно!")
            return None
        return value if value else None
    
    def _confirm_action(self, action: str, target: str) -> bool:
        answer = input(f"\n{action} '{target}'? (y/n): ").strip().lower()
        return answer in ('y', 'yes', 'da')
    
    def _add_player(self) -> None:
        print("\n--- Добавление нового игрока ---")
        
        nickname = self._get_input("Никнейм: ")
        if not nickname:
            return
        
        print("Доступные классы: warrior, mage, archer")
        player_class = self._get_input("Класс: ")
        if not player_class:
            return
        
        try:
            level_input = input("Уровень (по умолчанию 1): ").strip()
            level = int(level_input) if level_input else 1
            
            health_input = input("Здоровье (по умолчанию 100): ").strip()
            health = int(health_input) if health_input else 100
            
            exp_input = input("Опыт (по умолчанию 0): ").strip()
            experience = int(exp_input) if exp_input else 0
            
            self.app.add_player(nickname, player_class, level, health, experience)
            print(f"Игрок {nickname} успешно добавлен!")
            
        except DuplicatePlayerError as e:
            print(f"Ошибка: {e}")
        except ValueError as e:
            print(f"Ошибка в данных: {e}")
        except Exception as e:
            print(f"Ошибка: {e}")
    
    def _show_all_players(self) -> None:
        print("\n--- Все игроки ---")
        players = self.app.get_all_players()
        
        if not players:
            print("Нет игроков в коллекции")
            return
        
        self._print_table(players)
    
    def _print_table(self, players: List) -> None:
        if not players:
            return
        
        print("\n" + "-"*80)
        print(f"{'N':<4} {'Nickname':<15} {'Class':<10} {'Level':<8} {'HP':<8} {'Exp':<8} {'Status':<10}")
        print("-"*80)
        
        for i, player in enumerate(players, 1):
            status = "Alive" if player.is_alive() else "Dead"
            print(f"{i:<4} {player.nickname:<15} {player.player_class:<10} "
                  f"{player.level:<8} {player.health:<8} {player.experience:<8} {status:<10}")
        
        print("-"*80)
        print(f"Total players: {len(players)}")
    
    def _find_player(self) -> None:
        print("\n--- Поиск игрока ---")
        print("1. Поиск по никнейму")
        print("2. Поиск по классу")
        
        choice = self._get_choice()
        
        if choice == 1:
            nickname = self._get_input("Введите никнейм: ")
            if nickname:
                player = self.app.find_player(nickname)
                if player:
                    print("\nНайден игрок:")
                    print(str(player))
                else:
                    print(f"Игрок '{nickname}' не найден")
        
        elif choice == 2:
            player_class = self._get_input("Введите класс (warrior/mage/archer): ")
            if player_class:
                players = self.app.find_by_class(player_class)
                if players:
                    print(f"\nНайдено {len(players)} игроков класса {player_class}:")
                    self._print_table(players)
                else:
                    print(f"Игроки класса '{player_class}' не найдены")
        
        else:
            print("Неверный выбор")
    
    def _remove_player(self) -> None:
        print("\n--- Удаление игрока ---")
        nickname = self._get_input("Введите никнейм игрока для удаления: ")
        
        if not nickname:
            return
        
        player = self.app.find_player(nickname)
        if not player:
            print(f"Игрок '{nickname}' не найден")
            return
        
        if not self._confirm_action("Удалить", nickname):
            print("Удаление отменено")
            return
        
        try:
            self.app.remove_player(nickname)
            print(f"Игрок {nickname} удален")
        except PlayerNotFoundError as e:
            print(f"Ошибка: {e}")
    
    def _filter_players(self) -> None:
        print("\n--- Фильтрация игроков ---")
        print("1. Только живые")
        print("2. По минимальному уровню")
        print("3. По минимальному здоровью")
        print("4. По классу")
        
        choice = self._get_choice()
        
        try:
            if choice == 1:
                players = self.app.get_alive_players()
                print(f"\nЖивые игроки ({len(players)}):")
                self._print_table(players)
            
            elif choice == 2:
                min_level = int(input("Минимальный уровень: "))
                players = self.app.filter_players(lambda p: p.level >= min_level)
                print(f"\nИгроки с уровнем >= {min_level} ({len(players)}):")
                self._print_table(players)
            
            elif choice == 3:
                min_health = int(input("Минимальное здоровье: "))
                players = self.app.filter_players(lambda p: p.health >= min_health)
                print(f"\nИгроки с здоровьем >= {min_health} ({len(players)}):")
                self._print_table(players)
            
            elif choice == 4:
                player_class = self._get_input("Класс (warrior/mage/archer): ")
                if player_class:
                    players = self.app.find_by_class(player_class)
                    print(f"\nИгроки класса {player_class} ({len(players)}):")
                    self._print_table(players)
            
            else:
                print("Неверный выбор")
                
        except ValueError as e:
            print(f"Ошибка ввода: {e}")
    
    def _sort_players(self) -> None:
        print("\n--- Сортировка игроков ---")
        print("1. По никнейму (А-Я)")
        print("2. По никнейму (Я-А)")
        print("3. По уровню (возрастание)")
        print("4. По уровню (убывание)")
        print("5. По здоровью (возрастание)")
        print("6. По здоровью (убывание)")
        
        choice = self._get_choice()
        
        if choice == 1:
            players = self.app.sort_players(lambda p: p.nickname.lower(), reverse=False)
        elif choice == 2:
            players = self.app.sort_players(lambda p: p.nickname.lower(), reverse=True)
        elif choice == 3:
            players = self.app.sort_players(lambda p: p.level, reverse=False)
        elif choice == 4:
            players = self.app.sort_players(lambda p: p.level, reverse=True)
        elif choice == 5:
            players = self.app.sort_players(lambda p: p.health, reverse=False)
        elif choice == 6:
            players = self.app.sort_players(lambda p: p.health, reverse=True)
        else:
            print("Неверный выбор")
            return
        
        print(f"\nОтсортированные игроки ({len(players)}):")
        self._print_table(players)
    
    def _show_stats(self) -> None:
        print("\n--- Статистика ---")
        stats = self.app.get_player_stats()
        
        if stats["total"] == 0:
            print("Нет игроков")
            return
        
        print(f"Всего игроков: {stats['total']}")
        print(f"Средний уровень: {stats['avg_level']:.1f}")
        print(f"Среднее здоровье: {stats['avg_health']:.1f}")
        print(f"Живых игроков: {stats['alive_count']}")
        print("\nПо классам:")
       