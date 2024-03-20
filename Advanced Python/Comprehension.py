# Eksempel:
# Kør programmet og leg med koden
# dictionary_comprehension = {i: i * i for i in range(10)}
# list_comprehension = [i * i for i in range(10)]
# set_comprehension = {i%3 for i in range(10)}
# generator_comprehension = (2 * i + 5 for i in range(10))  # see explanation for generators in this document
# print(f'{dictionary_comprehension = }')
# print(f'{list_comprehension = }')
# print(f'{set_comprehension = }')
# print(f'{generator_comprehension = }')
# dictionary_comprehension = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
# list_comprehension = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# set_comprehension = {0, 1, 2}
# generator_comprehension = <generator object <genexpr> at 0x000001E3EF326CE0>


# Opgave:
# Skab denne liste med comprehension: [10, 15, 20, 25, 30, 35]
# Skriv din kode her

# my_list1 = [n*5 for n in range(8) if n*5 >= 10]
# print(my_list1)

# Opgave:
# Skab denne liste med comprehension: [0, 1, 2, 3, 40, 41, 42, 43, 44, 45]
# Brug "if" i din løsning!
# Skriv din kode her

# my_list2 = [n for n in range(46) if n < 4 or n > 39]
# print(my_list2)


# Opgave:
# Skab denne dictionary med comprehension: {3: 33, 4: 44, 5: 55, 6: 66}
# Skriv din kode her

# single = [3, 4, 5, 6]
# double = [33, 44, 55, 66]
#
# my_dict = {single: double for single, double in zip (single, double)}
# print(my_dict)


# Opgave:
# Tilføj en magisk funktion til klassen Dog så "huge_dog > tiny_dog" interpreteres på en fornuftig måde.

class Dog:
    def __init__(self, size):
        self.size = size

    def __lt__(self, other):
        return self.size < other.size


huge_dog = Dog(80)
tiny_dog = Dog(25)

# Uncomment this in order to test your solution!
if huge_dog > tiny_dog:
    print("You solved the exercise :)")