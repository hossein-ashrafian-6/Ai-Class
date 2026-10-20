class Character:
    def __init__(self, name, power, health, coins):
        self.name = name
        self.power = power
        self.health = health
        self.coins = coins
        self.level = 1

    def show_info(self):
        print(
            f"{self.name} | Level: {self.level} | "
            f"Power: {self.power} | Health: {self.health} | "
            f"Coins: {self.coins}"
        )

    def is_alive(self):
        return self.health > 0

    def attack(self, other):
        other.health -= self.power

        if other.health < 0:
            other.health = 0

        print(
            f"{self.name} attacked {other.name}. "
            f"{other.name}'s health: {other.health}"
        )

    def earn_coins(self, amount):
        self.coins += amount

    def buy_potion(self):
        if self.coins >= 20:
            self.coins -= 20
            self.health += 30
            print(f"{self.name} bought a potion. Health: {self.health}")
        else:
            print("Not enough coins")

    def level_up(self):
        self.level += 1
        self.power += 5

        print(
            f"{self.name} reached level {self.level}. "
            f"New power: {self.power}"
        )


# Testing the Character class

arya = Character("Arya", 10, 100, 50)
bran = Character("Bran", 8, 100, 30)

# Characters attack each other
arya.attack(bran)
bran.attack(arya)
arya.attack(bran)
bran.attack(arya)

# Arya buys a potion
arya.buy_potion()

# Bran levels up
bran.level_up()

# Check if characters are alive
print("Is Arya alive?", arya.is_alive())
print("Is Bran alive?", bran.is_alive())

# Show final information
arya.show_info()
bran.show_info()
