
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        old_hunger = self.hunger
        self.hunger = max(self.hunger - 3, 0)
        self.happiness = min(self.happiness + 1, 10)
        print(f"{self.name} is eating... 🍽️ (Hunger: {old_hunger} → {self.hunger})")

    def sleep(self):
        old_energy = self.energy
        self.energy = min(self.energy + 5, 10)
        print(f"{self.name} is sleeping... 💤 (Energy: {old_energy} → {self.energy})")

    def play(self):
        if self.energy < 2:
            print(f"{self.name} is too tired to play. 😴")
            return
        self.energy = max(self.energy - 2, 0)
        self.happiness = min(self.happiness + 2, 10)
        self.hunger = min(self.hunger + 1, 10)
        print(f"{self.name} is playing! 🎾")

    def train(self, trick):
        self.tricks.append(trick)
        self.happiness = min(self.happiness + 1, 10)
        print(f"{self.name} learned a new trick: {trick}! 🐾")

    def show_tricks(self):
        if not self.tricks:
            print(f"{self.name} hasn't learned any tricks yet.")
        else:
            print(f"{self.name}'s tricks: {', '.join(self.tricks)}")

    def get_status(self):
        print(f"\n{self.name}'s Current Status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
        print(f"Tricks: {self.tricks if self.tricks else 'None'}\n")
