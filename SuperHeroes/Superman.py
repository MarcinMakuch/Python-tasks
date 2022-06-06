from SuperHeroes.Hero import Hero


class Superman(Hero):
    def __init__(self, name, damage, health, mana, money):
        super().__init__(name, damage, health, mana, money)
