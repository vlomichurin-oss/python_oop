# ===== Функции-стратегии для сортировки =====

def by_nickname(player):
    return player.nickname.lower()


def by_level(player):
    return player.level


def by_health(player):
    return player.health


def by_power(player):
    return player.calculate_power()


def by_class_then_level(player):
    return (player.player_class, player.level)


def by_experience_per_level(player):
    return player.experience / player.level if player.level > 0 else 0


# ===== Функции-фильтры =====

def is_high_level(player, min_level=5):
    return player.level >= min_level


def is_healthy(player, min_health=50):
    return player.health >= min_health


def is_warrior_or_mage(player):
    return player.player_class in ('warrior', 'mage')


def is_alive_filter(player):
    return player.is_alive()


# ===== Фабрика фильтров =====

def make_level_filter(min_level):
    return lambda p: p.level >= min_level


def make_health_filter(min_health):
    return lambda p: p.health >= min_health


def make_experience_filter(min_exp):
    return lambda p: p.experience >= min_exp


# ===== Функции для map =====

def player_to_string(player):
    return str(player)


def player_to_dict(player):
    return {
        'nickname': player.nickname,
        'class': player.player_class,
        'level': player.level,
        'health': player.health,
        'experience': player.experience,
        'power': player.calculate_power(),
        'specialization': player.get_specialization()
    }


def extract_nickname(player):
    return player.nickname


def extract_power(player):
    return player.calculate_power()


def apply_discount_to_power(discount):
    return lambda p: int(p.calculate_power() * (1 - discount))


# ===== Callable-объекты-стратегии =====

class PowerBoostStrategy:
    def __init__(self, boost_percent):
        self.boost_percent = boost_percent
    
    def __call__(self, player):
        return int(player.calculate_power() * (1 + self.boost_percent))
    
    def __repr__(self):
        return f"PowerBoostStrategy(boost={self.boost_percent*100}%)"


class HealStrategy:
    def __init__(self, heal_amount):
        self.heal_amount = heal_amount
        self.total_healed = 0
    
    def __call__(self, player):
        old_health = player.health
        player.health = min(player.health + self.heal_amount, 200)
        healed = player.health - old_health
        self.total_healed += healed
        return healed


# ===== Функции для apply =====

def heal_all_players(player):
    player.health = min(player.health + 30, 200)