"""
Exercise "Morris The Miner" (this time object oriented)

As always, read the whole exercise description carefully before you begin to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.

Rewrite your original Morris code into an object oriented version.

Define a class Miner with attributes like sleepiness, thirst, etc.
and methods like sleep, drink, etc.
Create Morris and initialize his attributes by calling the constructor of Miner:
morris = Miner()

If you get stuck, ask google, the other pupils or the teacher (in this order).

When your program is complete, push it to your github repository.
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""

class Miner:
    def __init__(self):
        self.sleepiness = self.thirst = self.hunger = self.whisky = self.gold = 0


    def __repr__(self):
        return f"Miner: {self.sleepiness=} {self.thirst=} {self.hunger=} {self.whisky=} {self.gold=}"


    def sleep(self):
        self.sleepiness -= 10
        self.thirst += 1
        self.hunger += 1
        self.whisky += 0
        self.gold += 0


    def mine(self):
        self.sleepiness += 5
        self.thirst += 5
        self.hunger += 5
        self.whisky += 0
        self.gold += 5


    def eat(self):
        self.sleepiness += 5
        self.thirst -= 5
        self.hunger -= 20
        self.whisky += 0
        self.gold -= 2


    def buy_whisky(self):
        self.sleepiness += 5
        self.thirst += 1
        self.hunger += 1
        self.whisky += 1
        self.gold -= 1


    def drink(self):
        self.sleepiness += 5
        self.thirst -= 15
        self.hunger -= 1
        self.whisky -= 1
        self.gold += 0


    def run(self, turn):
        for t in range(turn):
            if self.sleepiness >= 95:
                morris.sleep()
            elif self.hunger >= 95:
                morris.eat()
            elif self.thirst >= 95:
                morris.drink()
            elif self.whisky < 1 and self.gold > 1:
                morris.buy_whisky()
            else:
                morris.mine()
        print(morris)


morris = Miner()
morris.run(1000)