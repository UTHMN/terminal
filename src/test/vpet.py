import random
import time

class vPet:
    def __init__(self) -> None:
        random.seed(input("Input a seed: "))
        self.emotions = ["happy", "sad", "angry", "annoyed", "neutral"]
        self.hunger = random.randint(40, 100)
        self.mood = random.choice(self.emotions)
        self.age = 0
        self.thirst = random.randint(40, 100)
        self.name = input("Name of pet: ")
        self.items = []
        self.shop = ["insert", "items"]
        self.money = 750
    
    def render(self):
        self.edict = {
            "happy":"(^-^)",
            "sad":"(>_<)",
            "angry":"(v-v)",
            "annoyed":"(-_-)",
            "neutral":"(*-*)"
        }
        print(self.edict[self.mood])
    
    def stats(self):
        print("")
        print(f"hunger: {self.hunger}")
        print(f"thirst: {self.thirst}")
        print(f"mood:   {self.mood}")
        print(f"age:    {self.age}")
        print(f"name:   {self.name}")
        print(f"money:  {self.money}")
        print("")

# Create new object
vpet = vPet()

while True:
    vpet.render()
    print("")
    inp = input("enter an option: ")
    print("")

    if inp == "help":
        pass
    elif inp == "stats":
        vpet.stats()
    elif inp == "feed":
        pass
    elif inp == "drink":
        pass
    elif inp == "play":
        pass
    elif inp == "shop":
        pass