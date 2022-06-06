class Hero:
    def __init__(self, name, damage, health, mana, money):
        self.name = name
        self.damage = damage
        self.health = health
        self.mana = mana
        self.money = money

    def rest(self):
        self.health + 20

    def attack(self, other):
        self.damage = other.health - 20

    def __str__(self):
        return f"My name is {self.name}"
