class PlayerCollection:
    def __init__(self, players=None):
        self._players = players.copy() if players else []
    
    # ===== Базовые методы =====
    
    def add(self, player):
        if hasattr(self, '_players'):
            self._players.append(player)
        return self
    
    def get_all(self):
        return self._players.copy()
    
    def find_by_nickname(self, nickname):
        for p in self._players:
            if p.nickname.lower() == nickname.lower():
                return p
        return None
    
    # ===== Новые методы для функциональных операций =====
    
    def sort_by(self, key_func, reverse=False):
        """Сортирует коллекцию с использованием стратегии."""
        self._players.sort(key=key_func, reverse=reverse)
        return self
    
    def sorted(self, key_func, reverse=False):
        """Возвращает отсортированную копию."""
        return sorted(self._players, key=key_func, reverse=reverse)
    
    def filter_by(self, predicate):
        """Фильтрует коллекцию с использованием предиката."""
        filtered = list(filter(predicate, self._players))
        return PlayerCollection(filtered)
    
    def filter_in_place(self, predicate):
        """Фильтрует коллекцию на месте."""
        self._players = list(filter(predicate, self._players))
        return self
    
    def map_to(self, transform_func):
        """Преобразует коллекцию с использованием функции."""
        return list(map(transform_func, self._players))
    
    def apply(self, func):
        """Применяет функцию ко всем элементам коллекции."""
        for player in self._players:
            func(player)
        return self
    
    def apply_with_result(self, func):
        """Применяет функцию и возвращает результаты."""
        return [func(player) for player in self._players]
    
    def get_alive(self):
        """Возвращает живых игроков."""
        return self.filter_by(lambda p: p.is_alive())
    
    def get_by_class(self, player_class):
        """Возвращает игроков указанного класса."""
        return self.filter_by(lambda p: p.player_class == player_class)
    
    def get_power_stats(self):
        """Возвращает статистику по силе."""
        powers = [p.calculate_power() for p in self._players]
        if not powers:
            return {'min': 0, 'max': 0, 'avg': 0, 'total': 0}
        return {
            'min': min(powers),
            'max': max(powers),
            'avg': sum(powers) / len(powers),
            'total': sum(powers)
        }
    
    # ===== Магические методы =====
    
    def __len__(self):
        return len(self._players)
    
    def __iter__(self):
        return iter(self._players)
    
    def __getitem__(self, index):
        return self._players[index]
    
    def __str__(self):
        if not self._players:
            return "Коллекция пуста"
        return "\n".join(str(p) for p in self._players)
    
    def __repr__(self):
        return f"PlayerCollection({len(self._players)} players)"