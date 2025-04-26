import random

class Pet:
    def __init__(self, name, pet_type="dog"):
        self.name = name
        self.pet_type = pet_type
        self.hunger = random.randint(3, 7)
        self.energy = random.randint(3, 7)
        self.happiness = random.randint(3, 7)
        self.tricks = []  # Bonus: to store tricks

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"🍖 {self.name} happily munches on some food!")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"😴 {self.name} curls up and sleeps peacefully.")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"🎾 {self.name} is playing and wagging its tail!")
        else:
            print(f"😔 {self.name} is too tired to play. Time for a nap!")

    def dance(self):
        if self.energy >= 3:
            self.energy -= 3
            self.happiness = min(10, self.happiness + 3)
            self.hunger = min(10, self.hunger + 2)
            print(f"💃 {self.name} is dancing joyfully!")
        else:
            print(f"🛌 {self.name} is too tired to dance.")

    def get_status(self):
        print(f"\n🐾 {self.name} the {self.pet_type}'s Current Status 🐾")
        print(f"🍗 Hunger: {self.hunger}/10")
        print(f"⚡ Energy: {self.energy}/10")
        print(f"😊 Happiness: {self.happiness}/10")
        print("-" * 30)

    # Bonus methods
    def train(self, trick):
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 1)
        print(f"🎓 {self.name} has learned a new trick: {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"🐕 Tricks {self.name} knows: {', '.join(self.tricks)}")
        else:
            print(f"😶 {self.name} hasn't learned any tricks yet.")
