# Inheritance hierarchy
# There is no limit to how deeply we can nest an inheritance tree. For example, a Cat can inherit from Animal which inherits from Living_Thing. 
# That said, we should always be careful that each time we inherit from a base class that the child is a strict subset of the parent. 
# You should never think to yourself "my child class needs a couple of the parent's methods, but not these other ones" and still decide to inherit from that parent.

# Assignment 1
# The game designers have decided to add a new unit to the game: Crossbowman. A crossbowman is always an archer, but not all archers are crossbowman. 
# Crossbowman have a number of arrows, but they have an additional method: triple_shot().

# Add a use_arrows(self, num) method to the Archer class. It should remove num arrows. If there isn't enough arrows to remove, it should raise a not enough arrows exception.
# The Crossbowman classes constructor should call it's parent's constructor.
# The crossbowman's triple_shot method takes a target as a parameter and prints {} was shot by 3 crossbow bolts where {} is the name of the Human that was shot.


class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Archer(Human):
    def __init__(self, name, num_arrows):
        super().__init__(name)
        self.__num_arrows = num_arrows

    def get_num_arrows(self):
        return self.__num_arrows

    def use_arrows(self, num):
        if self.__num_arrows - num < 0:
            raise Exception(f"not enough arrows")
        else:
            self.__num_arrows -= num


class Crossbowman(Archer):
    def __init__(self, name, num_arrows):
        super().__init__(name, num_arrows)


    def triple_shot(self, target):
        self.use_arrows(3)
        print(f"{target.get_name()} was shot by 3 crossbow bolts")


# -- TEST SUITE, DONT TOUCH BELOW THIS LINE --


def main():
    try:
        print("creating an archer named Bard")
        human2 = Archer("Bard", 1)
        identify(human2)
        print("Bard has {} arrows".format(human2.get_num_arrows()))

        print("creating a crossbowman named Sir Not-Appearing-In-This-Film")
        human3 = Crossbowman("Sir Not-Appearing-In-This-Film", 4)
        identify(human3)
        print("{} has {} arrows".format(human3.get_name(), human3.get_num_arrows()))
        print("{} attempts to shoot {}".format(human3.get_name(), human2.get_name()))
        human3.triple_shot(human2)
        print("{} has {} arrows".format(human3.get_name(), human3.get_num_arrows()))
        print("{} attempts to shoot {}".format(human3.get_name(), human2.get_name()))
        human3.triple_shot(human2)

    except Exception as e:
        print(e)


def identify(human):
    print("Getting name: {}".format(human.get_name()))


main()