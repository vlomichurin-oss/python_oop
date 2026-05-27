function use_weapon(weapon, target):
    # Полиморфизм через duck typing:
    # не важно, кто weapon, важно — умеет ли он attack()
    weapon.attack(target)

# Классы без общего предка
class Sword:
    method attack(target):
        print("Меч бьёт " + target + " с силой 10")

class Bow:
    method attack(target):
        print("Лук стреляет в " + target + " на расстоянии 5")

# Использование:
use_weapon(Sword(), "гоблин")   # Меч бьёт гоблин с силой 10
use_weapon(Bow(), "орк")        # Лук стреляет в орк на расстоянии 5


# ПЛОХОЙ КОД: функция, которая знает про каждый тип оружия
function use_weapon_bad(weapon, target):
    if isinstance(weapon, Sword):
        weapon.swing(target)           # у меча метод swing()
    elif isinstance(weapon, Bow):
        weapon.shoot(target)           # у лука метод shoot()
    elif isinstance(weapon, Crossbow):
        weapon.launch(target)          # у арбалета метод launch()
    elif isinstance(weapon, Spear):
        weapon.thrust(target)          # у копья метод thrust()
    elif isinstance(weapon, Axe):
        weapon.chop(target)            # у топора метод chop()
    elif isinstance(weapon, Dagger):
        weapon.stab(target)            # у кинжала метод stab()
    elif isinstance(weapon, Hammer):
        weapon.smash(target)           # у молота метод smash()
    else:
        print("Оружие не поддерживается!")

# Добавили новое оружие
class Whip:
    method whip_attack(target):
        print("Хлыст хлещет " + target)

# Проблема: нужно лезть в функцию и добавлять новую ветку!
# Если забыть — код сломается
use_weapon_bad(new Whip(), "врага")   # "Оружие не поддерживается!"