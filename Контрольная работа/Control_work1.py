import random

class Hero:
    def __init__(self, name: str, lvl: int, hp: int):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f"{self.name} готов к бою!"

class MageHero(Hero):
    def __init__(self, name: str, lvl: int, hp: int, mp: int):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        return f"Маг {self.name} кастует заклинание! MP: {self.mp}"

class WarriorHero(MageHero):
    def __init__(self, name: str, lvl: int, hp: int, mp: int = 0):
        super().__init__(name, lvl, hp, mp)

    def action(self):
        return f"Воин {self.name} рубит мечом! Уровень: {self.lvl}"

class BankAccount:
    def __init__(self, hero: Hero, balance: float, password: str, bank_name: str = "Simba"):
        self.hero = hero
        self._balance = balance
        self.__password = password
        self.bank_name = bank_name

    def login(self, password: str) -> bool:
        return self.__password == password


    @property
    def full_info(self) -> str:
        return f"Герой: {self.hero.name}, Класс: {type(self.hero).name}, Баланс: {self._balance} SOM"

    def get_bank_name(self) -> str:
        return self.bank_name

    def bonus_for_level(self) -> int:
        return self.hero.lvl * 10


    def __str__(self) -> str:
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def __add__(self, other):
        if not isinstance(other, BankAccount):
            return "Ошибка: Сложить можно только с другим банковским счетом!"

        if type(self.hero) == type(other.hero):
            return self._balance + other._balance
        else:
            return "Ошибка: Нельзя сложить счета героев разных классов!"

    def __eq__(self, other) -> bool:
        if not isinstance(other, BankAccount):
            return False
        return type(self.hero) == type(other.hero) and self.hero.lvl == other.hero.lvl

class KGSms:
    def send_otp(self, phone: str) -> str:
        return f"<text>Код: 1234</text><phone>{phone}</phone>"

if __name__ == "__main__":
    Ada_Wong = MageHero(name="Ada_Wong", lvl=50, hp=100, mp=150)
    Ashley_Graham = MageHero(name="Ashley_Graham", lvl=50, hp=100, mp=150)
    Leon_Scott_Kennedy = WarriorHero(name="Leon_Scott_Kennedy", lvl=50, hp=200)

    print(Ada_Wong.action())
    print(Leon_Scott_Kennedy.action())

    acc1 = BankAccount(hero=Ada_Wong, balance=5000, password="secure_pass1")
    acc2 = BankAccount(hero=Ashley_Graham, balance=3000, password="secure_pass2")
    acc3 = BankAccount(hero=Leon_Scott_Kennedy, balance=4000, password="secure_pass3")
    print('-' * 40)
    print(acc1)
    print(acc2)

    print("Банк:", acc1.get_bank_name())
    print("Бонус за уровень:", acc1.bonus_for_level(), "SOM")

    print('-' * 40)
    print("Сумма счетов двух магов:", acc1 + acc2)
    print("Сумма мага и воина:", acc1 + acc3)

    print("Mage1 == Mage2 ?", acc1 == acc2)
    print("Mage1 == Warrior ?", acc1 == acc3)

    sms = KGSms()
    print("\n", sms.send_otp("+996700734950"))