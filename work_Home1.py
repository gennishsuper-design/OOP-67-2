class Hero:



    def __init__(self, name, lvl, healthpoint, strength):
        self.name = name
        self.lvl = lvl
        self.healthpoint = healthpoint
        self.strength = strength

    def greet(self):
        print(f'Привет, я {self.name}, мой уровень {self.lvl}')

    def attack(self):
        print(f'{self.name} наносит удар')
        self.strength -= 1

    def rest(self):
        print(f'{self.name} отдыхает...')
        self.healthpoint += 1




barbarian= Hero('barbarian', 95, 100, 100)
archer = Hero('archer', 85, 100, 85)

barbarian.greet()
barbarian.attack()
print(f'Сила после аттаки {barbarian.strength}:')
barbarian.rest()
print(f'Здоровье после отдыха {barbarian.healthpoint}')




archer.greet()
archer.attack()
print(f'Сила после аттаки {archer.strength}:')
archer.rest()
print(f'Здоровье после отдыха {archer.healthpoint}')