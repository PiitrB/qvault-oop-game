# Assignment 1
# A Human class with a constructor has already been created for you. 
# We don't the other game developers using our Human class to have to worry about how humans move, 
# we'll abstract that data away from them by encapsulating the private __pos_x, __pos_y, and __speed variables.
# Let's add the methods our users will actually call.

# move_right(): Adds the human's speed to its x position
# move_left(): Subtracts the human's speed from its x position
# move_up(): Adds the human's speed to its y position
# move_down(): Subtracts the human's speed from its y position
# get_position(): Returns the x position and y position as a tuple

# Assignment 2
# Complete the missing methods. The __raise_if_cannot_sprint and __use_sprint_stamina are 
# private methods that are only intended to be used within the class. In your case, you'll use them to build the four sprinting methods.

# __raise_if_cannot_sprint
# This method should raise the exception "not enough stamina to sprint" if the human is out of stamina.

# __use_sprint_stamina
# Remove one stamina from the human.

# Sprint methods
# Raise an error if there isn't enough stamina to sprint.
# Use the stamina needed to sprint
# Move twice in the direction of the sprint

class Human:
    def sprint_right(self):
        if self.__stamina <= 0:
            self.__raise_if_cannot_sprint()
        self.__use_sprint_stamina()
        self.__pos_x += 2*self.__speed

    def sprint_left(self):
        if self.__stamina <= 0:
            self.__raise_if_cannot_sprint()
        self.__use_sprint_stamina()
        self.__pos_x -= 2*self.__speed

    def sprint_up(self):
        if self.__stamina <= 0:
            self.__raise_if_cannot_sprint()
        self.__use_sprint_stamina()
        self.__pos_y += 2*self.__speed

    def sprint_down(self):
        if self.__stamina <= 0:
            self.__raise_if_cannot_sprint()
        self.__use_sprint_stamina()
        self.__pos_y -= 2*self.__speed

    def __raise_if_cannot_sprint(self):
        raise Exception("not enough stamina to sprint")

    def __use_sprint_stamina(self):
        self.__stamina -= 1
        

    # -- TEST SUITE, DONT TOUCH BELOW THIS LINE --

    def move_right(self):
        self.__pos_x += self.__speed

    def move_left(self):
        self.__pos_x -= self.__speed

    def move_up(self):
        self.__pos_y += self.__speed

    def move_down(self):
        self.__pos_y -= self.__speed

    def get_position(self):
        return self.__pos_x, self.__pos_y

    def __init__(self, pos_x, pos_y, speed, stamina):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__speed = speed
        self.__stamina = stamina


def main():
    try:
        print("creating a human. x=0 y=0 speed=5")
        human = Human(0, 0, 5, 3)
        print_position(human)
    except Exception as e:
        print(e)

    try:
        print("sprinting left...")
        human.sprint_left()
        print_position(human)
    except Exception as e:
        print(e)

    try:
        print("sprinting left...")
        human.sprint_left()
        print_position(human)
    except Exception as e:
        print(e)

    try:
        print("moving right...")
        human.move_right()
        print_position(human)
    except Exception as e:
        print(e)

    try:
        print("moving up...")
        human.move_up()
        print_position(human)
    except Exception as e:
        print(e)

    try:
        print("sprinting up...")
        human.sprint_up()
        print_position(human)
    except Exception as e:
        print(e)

    try:
        print("sprinting down...")
        human.sprint_down()
        print_position(human)
    except Exception as e:
        print(e)


def print_position(human):
    x, y = human.get_position()
    print("Your human is at x={}, y={}".format(x, y))


main()