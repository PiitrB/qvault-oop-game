# Dragons
# In Age of Dragons there are Orcs, Humans, Goblins, Dragons, etc. All of those different creatures are called "units". 
# At the moment, the only thing specific to a unit is that it has a position on the game map and a name.

# Dragons, a specific type of unit, can breathe fire in a large area dealing damage to any units that are touched by its fiery blaze.
# The game grid
# The game map is basically just a Cartesian plane.

# Assignment
# Complete the unit's in_area method and the dragon's breathe_fire method.

# in_area
# If the unit's position is in the rectangle defined by the parameters, return True. Otherwise, return False. 
# x_1 and y_1 are the bottom-left point of the rectangle. x_2 and y_2 are the top-right point.

# breathe_fire
# This method causes the dragon to breathe a swath of fire in the target area. The target area is centered at (x,y). 
# The area stretches for __fire_range in either direction inclusively. 
# For each unit in the units array, print {} is hit by the fire if the unit is within the blast, where {} is the name of the unit.

class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        if (self.pos_x >= x_1 and self.pos_x <= x_2) and (self.pos_y >= y_1 and self.pos_y <= y_2):
            return True
        return False


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        for unit in units:
            if unit.in_area(x - self.__fire_range, y - self.__fire_range, x + self.__fire_range, y + self.__fire_range):
                print(f"{unit.name} is hit by the fire")
        pass


# -- TEST SUITE, DONT TOUCH BELOW THIS LINE --


def main():
    print("Creating an army of generic units")
    units = [
        Unit("Yvor", 1, 0),
        Unit("Nicholas", 0, 1),
        Unit("Eoin", 2, 0),
        Unit("Cian", 3, 3),
        Unit("Andrew", -1, 4),
        Unit("Baran", -6, 5),
        Unit("Carbry", 2, 1),
    ]
    for unit in units:
        print("creating {} at position {} {}".format(unit.name, unit.pos_x, unit.pos_y))

    smaug = Dragon("Smaug", 6, 6, 2)
    print("{} breathes fire at position 1,1".format(smaug.name))
    smaug.breathe_fire(1, 1, units)


main()