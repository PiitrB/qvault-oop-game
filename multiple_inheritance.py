# Multiple children
# So far we've worked with linear class inheritance. In reality, inheritance structures often form trees, 
# not lines. A class can have as many direct child classes as the programmer wants.

# Assignment 1
# The Hero class is provided for you. In this assignment you'll be writing the Archer class that inherits from Hero, 
# and in the next assignment you'll be writing its sibling Wizard class.
# Fulfill the following requirements from the game designers:
    # Archer should inherit from Hero
    # Archer should setup the hero's name and health
    # Set a private "number of arrows" that can be passed in as a third parameter to the constructor.
    # Create a shoot method that takes a target human as input. If there are no arrows left, raise a not enough arrows exception. 
    # Otherwise, remove an arrow and deal 10 damage to the target human.

# Assignment 2
# Let's extend the Hero class by adding a second child class: the Wizard. Wizard heroes are more powerful than archer heroes. 
# They cast spells at other humans instead of shooting them, and casting does 25 damage instead of 10, but also costs 25 mana.
# Fulfill the following requirements.
    # Wizard should inherit from Hero
    # Wizard should setup the hero's name and health
    # Set a private "mana" variable that can be passed in as a third parameter to the constructor.
    # Create a cast method that takes a target human as input. If there is not enough mana left, raise a not enough mana exception. 
    # Otherwise, remove 25 mana from the wizard and deal 25 damage to the target human.



class Hero:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def take_damage(self, damage):
        self.__health -= damage


# Create Archer class here
class Archer(Hero):
    def __init__(self, name, health, num_arrows):
        super().__init__(name, health)
        self.__num_arrows = num_arrows
    
    def shoot(self, target):
        if self.__num_arrows <= 0:
            raise Exception("not enough arrows")
        self.__num_arrows -= 1
        target.take_damage(10)

# Create wizard class here
class Wizard(Hero):
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.__mana = mana

    def cast(self, target):
        if self.__mana - 25 < 0:
            raise Exception("not enough mana")
        self.__mana -= 25
        target.take_damage(25)



# -- TEST SUITE, DONT TOUCH BELOW THIS LINE --


def main():
    print("creating a Wizard named Harry with 100 health and 200 mana")
    human1 = Wizard("Harry", 100, 400)
    identify(human1)

    print("creating an Archer named Pericles with 100 health and 2 arrows")
    human2 = Archer("Pericles", 100, 2)
    identify(human2)

    while human1.get_health() > 0 and human2.get_health() > 0:
        try:
            print(
                "{} attempts to shoot {}".format(human2.get_name(), human1.get_name())
            )
            human2.shoot(human1)
            identify(human1)
            identify(human2)
        except Exception as e:
            print(e)

        try:
            print(
                "{} attempts to cast at {}".format(human1.get_name(), human2.get_name())
            )
            human1.cast(human2)
            identify(human1)
            identify(human2)
        except Exception as e:
            print(e)


def identify(human):
    print("Name: {}, health: {}".format(human.get_name(), human.get_health()))


main()