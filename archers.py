# Assignment
# Complete the Archer class.

# Constructor
# The constructor should take and set as properties the following parameters in order:

# num_arrows
# health
# name
# get_shot method
# Create a method called get_shot that doesn't take any parameters.

# If the current archer has health left it removes one health from the current archer. Then, if the archer's health is 0 it prints the string: {} is dead where {} is the archer's name.

# shoot method
# Create a method called shoot that takes a target archer as input.

# If the shooter has no arrows left, raise the exception {} can't shoot where {} is the archers name. 
# Otherwise, remove an arrow from the shooter and print {1} shoots {2} where {1} is the shooter's name and {2} is the name of the target. Next, call the target's get_shot() method.



class Archer:
    def __init__(self, num_arrows, health, name):
        self.num_arrows = num_arrows
        self.health = health
        self.name = name
     
    def get_shot(self):
        if self.health > 0:
            self.health -= 1
        if self.health == 0:
            print(f"{self.name} is dead")
    
    def shoot(self, target):
        if self.num_arrows == 0:
            raise Exception(f"{self.name} can't shoot")
        self.num_arrows -= 1
        print(f"{self.name} shoots {target.name}")
        target.get_shot()


# -- TEST SUITE, DONT TOUCH BELOW THIS LINE --


def main():
    bard = Archer(1, 3, "Bard")
    legolas = Archer(10000, 3, "Legolas")

    while bard.health > 0 and legolas.health > 0:
        try:
            print_status(bard)
            print_status(legolas)
            bard.shoot(legolas)
        except Exception as e:
            print(e)

        try:
            print_status(bard)
            print_status(legolas)
            legolas.shoot(bard)
        except Exception as e:
            print(e)


def print_status(archer):
    print(
        "{} has {} health and {} arrows".format(
            archer.name, archer.health, archer.num_arrows
        )
    )


main()
