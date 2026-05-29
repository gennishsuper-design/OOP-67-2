# Принципы ООП  - Наследование, Полиморфизм. Гит-коммиты



#Наследование:
#Супер | Родительский класс


class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f'{self.name} base action!!'



#Полиморфизм


class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp




    def action(self):
        return f"please don't die {self.name}"

    def cast_ckill(self):
        return f"{self.name} Don't die"


Lando =  Hero('Lando', 99, 100500)
michael_schumacher = MageHero('Michael Schumacher', 100, -100500, 100500)




# print(Lando.action())
# print(michael_schumacher.action())

class Fly:
    def f_action(self):
        return f"Fly"

class Swim:
    def s_action(self):
        return f"Swim"

class Animal(Swim, Fly):
    def action(self):
        return f"action"


donald_trump = Animal()

# print(donald_trump.action())
# print(donald_trump.s_action())
# print(donald_trump.f_action())



class A:
    def action(self):
        print('A')

class B(A):
    def action(self):
        super().action()
        print('B')

class C(A):
    def action(self):
        super().action()
        print('C')

class D(B, C):
    def action(self):
        super().action()
        print('D')

test_obj = D()

test_obj.action()
print(D.mro())