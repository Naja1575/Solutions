"""
Exercise "Cars":

As always, read the whole exercise description carefully before you begin to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.

Define a function that prints a car's motor sound (for example "roooaar")

In the main program:
    Define variables which represent the number of wheels and the maximum speed of 2 different cars
    Print out these properties of both cars
    Then call the motor sound function

If you have no idea how to begin, open S0420_cars_help.py and start from there.
If you get stuck, ask google, the other pupils or the teacher (in this order).
If you are still stuck, open S0430_cars_solution.py and compare it with your solution.

When your program is complete, push it to your github repository.
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""

def drive_car():
    print("rooooom rooooom")


car1_wheels = 4  # define number of wheels for car1
car1_max_speed = 180  # define maximum speed for car1
car2_wheels = 4 # define number of wheels for car2
car2_max_speed = 250 # define maximum speed for car2

print("Car 1 has", car1_wheels, "wheels and a max speed of", car1_max_speed)  # print out the properties of car1
print("Car 2 has", car2_wheels, "wheels and a max speed of", car2_max_speed)  # print out the properties of car2

drive_car()  # call drive_car