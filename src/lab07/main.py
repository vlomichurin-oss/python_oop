import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.lab07.app import GameApp
from src.lab07.cli import GameCLI
from src.lab07.storage import PlayerStorage
from src.lab07.exceptions import StorageError


def main():
    print("="*50)
    print("     ДОБРО ПОЖАЛОВАТЬ В GAME MANAGER")
    print("="*50)
    
    storage = PlayerStorage("players.json")
    app = GameApp()
    1
    try:
        players_data = storage.load()
        if players_data:
            app.load_players(players_data)
            print(f"Загружено {len(players_data)} игроков")
        else:
            print("Нет сохраненных данных")
    except StorageError as e:
        print(f"Не удалось загрузить данные: {e}")
    
    cli = GameCLI(app)
    
    try:
        cli.run()
    except KeyboardInterrupt:
        print("\n\nПрервано пользователем")
    finally:
        try:
            players = app.get_all_players()
            storage.save(players)
            print(f"Сохранено {len(players)} игроков")
        except StorageError as e:
            print(f"Не удалось сохранить данные: {e}")


if __name__ == "__main__":
    main()