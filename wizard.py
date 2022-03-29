# Assignment
# Complete the cast_fireball method.

# Casting a fireball costs 20 mana
# If the wizard doesn't have enough mana, raise the exception {} cannot cast fireball
# Otherwise, {1} casts fireball at {2} where {1} is the caster's name and {2} is the target's name, then make sure the target is "fireballed"

class Wizard:
    def cast_fireball(self, target):
        if self.__mana < 20:
            raise Exception(f"{self.name} cannot cast fireball")
        print(f"{self.name} casts fireball at {target.name}")
        self.__mana -= 20
        target.get_fireballed()
            

    # -- TEST SUITE, DONT TOUCH BELOW THIS LINE --

    def __init__(self, name):
        self.__mana = 45
        self.__health = 65
        self.name = name

    def get_mana(self):
        return self.__mana

    def get_health(self):
        return self.__health

    def get_fireballed(self):
        fireball_damage = 30
        self.__health -= fireball_damage
        print("{} is hit by a fireball".format(self.name))
        if self.__health <= 0:
            print("{} is dead".format(self.name))

    def drink_mana_potion(self):
        print("{} drinks a mana potion".format(self.name))
        self.__mana += 40


def main():
    merlin = Wizard("Merlin")
    madame_mim = Wizard("Madame Mim")

    while madame_mim.get_health() > 0:
        if merlin.get_mana() < 10:
            merlin.drink_mana_potion()

        try:
            print_status(merlin)
            print_status(madame_mim)
            merlin.cast_fireball(madame_mim)
        except Exception as e:
            print(e)


def print_status(wizard):
    print(
        "{} has {} health and {} mana".format(
            wizard.name, wizard.get_health(), wizard.get_mana()
        )
    )


main()