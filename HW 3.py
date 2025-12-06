import random

class Dog:
    def __init__(self, name):
        self.name = name

    def actions(self):
        action = random.randint(0, 3)
        if action == 0:
            print(f"{self.name} is lying")
        elif action == 1:
            print(f"{self.name} is sleeping")
        elif action == 2:
            print(f"{self.name} is running")
        elif action == 3:
            print(f"{self.name} is eating")

    def emotes(self):
        mood = random.randint(0, 3)
        if mood == 0:
            print(f"{self.name} is happy")
        elif mood == 1:
            print(f"{self.name} is sad")
        elif mood == 2:
            print(f"{self.name} is angry")
        else:
            print(f"{self.name} is tired")

    def energy(self):
        energy = random.randint(0, 100)
        print(f"energy: {energy}")

        if 0 <= energy <= 20:
            print(f"{self.name} is tired")
        elif 20 < energy <= 50:
            print(f"{self.name} is low tired")
        elif 50 < energy <= 70:
            print(f"{self.name} is low active")
        elif 70 < energy < 100:
            print(f"{self.name} is active")
        elif energy == 100:
            print(f"{self.name} has full energy")


rex = Dog("Rex")

rex.actions()
rex.emotes()
rex.energy()