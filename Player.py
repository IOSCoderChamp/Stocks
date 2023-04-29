class Person:
    def __init__(self, name: str):
        self.name = name

    def say(self, speech: str):
        print(speech)
    
    

class Character(Person):
    def __init__(self, name: str, stamina: float, health: float, items: list):
        super().__init__(name)
        self.stamina = stamina
        self.health = health
        self.items = items
        self.cii = 0
        self.ci = ""
        if self.items[0] != None:
            self.ci = str(self.items[self.cii])

    def damage(self, times: int):
        self.health = self.health - 0.01 * times

    def swapitem(self):
        a = len(self.items)
        self.cii = self.cii + 1
        if a == self.cii:
            self.cii = 0
        self.ci = str(self.items[self.cii])

class Enemy(Person):
    def __init__(self, name: str, level: str):
        super().__init__(name)
        self.stamina = 0.0
        self.health = 0.0

        if level == "Easy":
            self.health = 0.5
            self.stamina = 0.5
        if level == "Medium":
            self.health = 1.0
            self.stamina = 1.0
        if level == "Hard":
            self.health = 1.5
            self.stamina = 1.5
        if level == "Extreme":
            self.health = 2.0
            self.stamina = 2.0
        if level == "Final Boss":
            self.health = 3.0
            self.stamina = 3.0
    def damage(self, times: int):
        self.health = self.health - 0.01 * times
    
    def run(self):
        self.stamina = self.stamina - 0.01
        
        
Preston = Character("Preston", 1.00, 1.00, ["Pickaxe", "Torch", "Sword", "Belt"])

Preston.damage(5)
Preston.say("OWWWW")
print(Preston.health * 100)
Preston.swapitem()
Preston.swapitem()
Preston.swapitem()
Preston.swapitem()
Preston.swapitem()
print(Preston.cii)
print(Preston.ci)