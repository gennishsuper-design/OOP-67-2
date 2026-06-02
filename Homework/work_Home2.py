import random

class Hero:
    def __init__(self, name, level=1, health=100, strength=10):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет! Я {self.name}, уровень {self.level}.")

    def attack(self):
        print(f"{self.name} наносит удар!")

    def rest(self):
        self.health += 20
        print(f"{self.name} отдыхает и восстанавливает здоровье до {self.health}.")


class Warrior(Hero):
    def __init__(self, name, level=1, health=120, strength=15, stamina=80):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print(f"{self.name} атакует мечом!")


class Mage(Hero):
    def __init__(self, name, level=1, health=90, strength=12, mana=100):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print(f"{self.name} кастует заклинание!")


class Assassin(Hero):
    def __init__(self, name, level=1, health=95, strength=14, stealth=90):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        print(f"{self.name} атакует из-под тишка!")


def determine_winner(player, enemy):
    rules = {
        'Warrior': 'Assassin',
        'Assassin': 'Mage',
        'Mage': 'Warrior',
    }

    if player.name == enemy.name:
        return 'Ничья!'

    if rules[player.name] == enemy.name:
        return f'{player.name} победил!'

    return f'{enemy.name} победил!'


def main():
    warrior = Warrior('Warrior', level=5, stamina=90)
    mage = Mage('Mage', level=5, mana=120)
    assassin = Assassin('Assassin', level=5, stealth=95)

    heroes = {
        'warrior': warrior,
        'mage': mage,
        'assassin': assassin,
    }

    print('Созданы герои:')
    for hero in heroes.values():
        hero.greet()
        hero.attack()
        print()

    choice = input('Выберите героя:\nWarrior / Mage / Assassin\nВаш выбор: ').strip().lower()
    if choice not in heroes:
        print('Неверный выбор героя. Пожалуйста, выберите Warrior, Mage или Assassin.')
        return

    player = heroes[choice]
    opponents = [hero for key, hero in heroes.items() if key != choice]
    enemy = random.choice(opponents)

    print(f"\nВы выбрали: {player.name}")
    print(f"Противник: {enemy.name}")
    print()

    result = determine_winner(player, enemy)
    print(result)


if __name__ == '__main__':
    main()