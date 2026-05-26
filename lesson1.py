class Hero:
    # Консктруктор класса Hero, который принимает имя героя, его здоровье и урон.
    def __init__(self, name, lvl, hp):
        # Атрибуты класса
        self.name = name
        self.lvl = lvl
        self.hp = hp
        
        
def rest(self):
    return f"{self.name} отдыхает на чили на расслабоне."

# Обьект Экземпляр на основе класса
kirito = Hero("Kirito", 100, 1000)
asuna = Hero("Asuna", 111, 1111)

# print(kirito.name)  # Выводит имя героя
# print(kirito.lvl)   # Выводит уровень героя
# print(kirito.hp)    # Выводит здоровье героя

# print(asuna.name)
# print(asuna.lvl)
# print(asuna.hp)

print(kirito.rest())
print(asuna.rest())
my_str_1 = "Hello"
my_str_2 = "World"
print(my_str_1 .capitalize())  # Выводит "Hello"
print(my_str_2 .capitalize())  # Выводит "World"