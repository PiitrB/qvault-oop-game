# We have written a lot of classes so far, but we haven't written much code that calls classes and uses their methods.

# The code in the test suite is largely the same code that you built in the last assignment. One key difference is the addition of a describe function that you'll be using.

# Assignment
# Let's use the Dragon class we made to have a little dragon fight.

# describe each dragon on the dragon array that has been created for you.
# For each dragon in the array, have it breathe fire at all the other dragons. The center of each blast should always be at (3,3).

def main():
    dragons = [
        Dragon("Green Dragon", 0, 0, 1),
        Dragon("Red Dragon", 2, 2, 2),
        Dragon("Blue Dragon", 4, 3, 3),
        Dragon("Black Dragon", 5, -1, 4),
    ]

    for dragon in dragons:
        describe(dragon)

    for dragon in dragons:
        others = []
        for other in dragons:
            if other != dragon:
                others.append(other)
        dragon.breathe_fire(3, 3, others)

    # alternative to creating list of dragons except the one calling the method:
    # for i in range(0, len(dragons)):
        # dragon = dragons[i]
        # other_dragons = dragons.copy()
        # del other_dragons[i]
        # dragon.breathe_fire(i, i, other_dragons)

# -- TEST SUITE, DONT TOUCH BELOW THIS LINE --


def describe(dragon):
    print("{} is at {}/{}".format(dragon.name, dragon.pos_x, dragon.pos_y))


class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        return (
            self.pos_x >= x_1
            and self.pos_x <= x_2
            and self.pos_y >= y_1
            and self.pos_y <= y_2
        )


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        print(
            "{} breathes fire at {}/{} with range {}".format(
                self.name, x, y, self.__fire_range
            )
        )
        for unit in units:
            in_area = unit.in_area(
                x - self.__fire_range,
                y - self.__fire_range,
                x + self.__fire_range,
                y + self.__fire_range,
            )
            if in_area:
                print("{} is hit by the fire".format(unit.name))


main()
