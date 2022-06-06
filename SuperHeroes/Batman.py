from SuperHeroes.Hero import Hero


class Batman(Hero):
    def __init__(self, name, damage, health, mana, money):
        super().__init__(name, damage, health, money, mana)
