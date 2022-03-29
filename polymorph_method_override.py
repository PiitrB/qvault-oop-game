# Assignment 1
# Dragons are big. As it turns out, they're a lot bigger than most other units in Age of Dragons. 
# Let's override the Dragon's in_area() method to account for that.
# First, we'll need a new class that represents a rectangle. Take a look at the main function to see how it's expected to behave. 
# Variables should be passed into the constructor in this order:
# x1
# y1
# x2
# y2

# Assignment 2
# Get edges
# Remember that with normal "units" we were checking if their (x/y) point was within a rectangle (the Dragon's breath) 
# to see if they were hit by the fire. With a dragon, because they're so big, we're going to check if the dragon's body (a rectangle) is within the fire (also a rectangle still).
# In the next assignment we'll be writing the overlap method itself. First, lets set up some helper methods.
# Write the following methods, what they do should be self-explanatory.
# get_left_x()
# get_right_x()
# get_top_y()
# get_bottom_y()
# Remember that x1 OR y1 could be the "left" x based on its value on the Cartesian plane.

# Assignment 3
# Check if rectangles overlap
# Let's write the overlap method! Keep in mind that we want our overlap to be inclusive. If the rectangle's edges are on top of each other, that counts as overlapping.
# The logic for two overlapping rectangles, A and B, is simple.
# A's left edge to left of B's right edge
# A's right edge to right of B's left edge and
# A's top above B's bottom, and
# A's bottom below B's Top

# Assignment 4
# Bringing it together in the Dragon class
# Let's bring all we've done together in the Dragon class. The Dragon class should override the Unit class's in_area method. 
# Instead of checking if the center position of the Dragon is in the given area, we'll check if its big dragon body overlaps with the given area.
# First. complete the Dragon's constructor. The dragon needs one more private data member: __hit_box. The hit box is a Rectangle object. 
# You've been provided with the height, width, and center position of the dragon.
# Next, you'll need to override the in_area method. Create a rectangle object with the given corner positions, and use the rectangle's 
# overlaps method to check if the Dragon is inside it. This method should return a boolean value.



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
    def __init__(self, name, pos_x, pos_y, height, width, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.fire_range = fire_range
        self.height = height
        self.width = width
        self.__hit_box = Rectangle(pos_x-width/2, pos_y-height/2, pos_x+width/2, pos_y+height/2)

    def in_area(self, x_1, y_1, x_2, y_2):
        affected_area = Rectangle(x_1, y_1, x_2, y_2)
        return self.__hit_box.overlaps(affected_area)

    # -- TEST SUITE, DONT TOUCH BELOW THIS LINE --

    def breathe_fire(self, x, y, units):
        print(
            "{} breathes fire at {}/{} with range {}".format(
                self.name, x, y, self.fire_range
            )
        )
        for unit in units:
            in_area = unit.in_area(
                x - self.fire_range,
                y - self.fire_range,
                x + self.fire_range,
                y + self.fire_range,
            )
            if in_area:
                print("{} is hit by the fire".format(unit.name))


class Rectangle:
    def overlaps(self, rect):
        return (
            self.get_left_x() <= rect.get_right_x()
            and self.get_right_x() >= rect.get_left_x()
            and self.get_top_y() >= rect.get_bottom_y()
            and self.get_bottom_y() <= rect.get_top_y()
        )

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_left_x(self):
        if self.x1 < self.x2:
            return self.x1
        return self.x2

    def get_right_x(self):
        if self.x1 > self.x2:
            return self.x1
        return self.x2

    def get_top_y(self):
        if self.y1 > self.y2:
            return self.y1
        return self.y2

    def get_bottom_y(self):
        if self.y1 < self.y2:
            return self.y1
        return self.y2


def describe(dragon):
    print(
        "{} is at position ({},{}). height: {}. width: {}. fire range: {}".format(
            dragon.name,
            dragon.pos_x,
            dragon.pos_y,
            dragon.height,
            dragon.width,
            dragon.fire_range,
        )
    )


def main():
    dragons = [
        Dragon("Green Dragon", -1, -2, 1, 2, 1),
        Dragon("Red Dragon", 2, 2, 2, 2, 2),
        Dragon("Blue Dragon", 4, -3, 2, 1, 1),
        Dragon("Black Dragon", 5, -1, 3, 2, 2),
    ]

    for i in range(0, len(dragons)):
        dragon = dragons[i]
        describe(dragon)

    for i in range(0, len(dragons)):
        dragon = dragons[i]
        other_dragons = dragons.copy()
        del other_dragons[i]
        dragon.breathe_fire(i, i, other_dragons)


main()