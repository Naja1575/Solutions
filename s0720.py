"""
Exercise: Object oriented role playing game, part 1 :

As always, read the whole exercise description carefully before you begin to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.

Define a class "Character" with attributes "name, max_health", "_current_health", "attackpower."
_current_health shall be a private attribute, it is not meant to be changed from outside the class.

Add a constructor (__init__) which accepts the classes' attributes as parameters.
Add a method for printing out class objects (__repr__).

Add a method "hit" which reduces _current_health of another character by attackpower.
Example: _current_health=80 and attackpower=10: a hit reduces _current_health to 70.

The method hit may not change the private attribute _current_health of a (potentially) foreign class.
For this reason we define another method get_hit which reduces _current_health of the object it belongs to by attackpower.

If you get stuck, ask google, the other pupils or the teacher (in this order).

When your program is complete, push it to your github repository
and compare it to the teacher's solution in S0730_rpg1_solution.py
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""


class Character:

    def __init__(self, name, health, attackpower):
        self.name = name
        self.max_health = health
        self.attackpower = attackpower
        self._current_health = health

    def __repr__(self):
        return f"{self.name=} {self.max_health=} {self._current_health=} {self.attackpower=}"

    def hit(self, other):
        other.get_hit(self.attackpower)

    def get_hit(self, attackpower):
        self._current_health -= attackpower

    def get_healed(self, healpower):
        self._current_health += healpower


class Healer(Character):

    def __init__(self, name, health, healpower):
        self.name = name
        self.max_health = health
        self.healpower = healpower
        self._current_health = health

    def __repr__(self):
        return f"{self.name=} {self.max_health=} {self._current_health=} {self.healpower=}"

    def heal(self, other):
        other.get_healed(self.healpower)



hero1 = Character("Bozeto", 100, 20)
hero2 = Character("Andananda", 110, 24)
hero3 = Healer("DoctorX", 75, 15)
print(hero1)
print(hero2)
print(hero3)
hero1.hit(hero2)
print(hero2)
hero3.heal(hero2)
print(hero2)
