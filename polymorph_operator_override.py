# Operator Overloading
# Another kind of built-in polymorphism in Python is the ability to override an operator in Python depending upon the operands used.
# Arithmetic operators work for built-in types like integers and strings.
# Custom classes on the other hand don't have any built-in support for those operators:
# However, we can add our own support! The __add__ method is used by the Python interpreter when instances of a class are being added with the + operator.
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, point):
#         x = self.x + point.x
#         y = self.y + point.y
#         return Point(x, y)
# p1 = Point(4, 5)
# p2 = Point(2, 3)
# p3 = p1 + p2
# # p3 is (6, 8)
# When you call p1 + p2 under the hood the interpreter just calls p1.__add__(p2).
# 
# Operation	Operator	Method
# Addition	+	add
# Subtraction	-	sub
# Multiplication	*	mul
# Power	**	pow
# Division	/	truediv
# Floor Division	//	floordiv
# Remainder (modulo)	%/	mod
# Bitwise Left Shift	<<	lshift
# Bitwise Right Shift	>>	rshift
# Bitwise AND	&	and
# Bitwise OR	|	or
# Bitwise XOR	^	xor
# Bitwise NOT	~	invert

# Assignment 1
# In Age of Dragons, players can upgrade the weaponry of their armies. If a player has two "bronze" swords, they can actually craft them together 
# to create a "iron" sword. Likewise, two iron swords crafted together create a "steel" sword. 
# If a player tries to craft anything other than 2 bronze swords or 2 iron swords, a can not craft exception is raised.
# # To make crafting simple for other developers, we'll use operator overloading on the Sword class. The + operator should craft the swords.
# type is a string, either bronze, iron or steel.

class Sword:
    def __init__(self, type):
        self.type = type

    def __add__(self, sword):
        if self.type == sword.type:
            if self.type == "bronze":
                return Sword("iron")
            elif self.type == "iron":
                return Sword("steel")
            raise Exception("can not craft")
        raise Exception("can not craft")



# -- TEST SUITE, DONT TOUCH BELOW THIS LINE --


def main():
    try:
        sword1 = Sword("bronze")
        sword2 = Sword("bronze")
        print(
            "creating sword1 that is {} and sword2 that is {}".format(
                sword1.type, sword2.type
            )
        )
        print("crafting sword1 and sword2 into a new sword3...")
        sword3 = sword1 + sword2
        print("sword3 is {}".format(sword3.type))
        sword4 = Sword("iron")
        print("creating sword4 that is {}".format(sword4.type))
        print("crafting sword3 and sword3 into a new sword5...")
        sword5 = sword3 + sword4
        print("sword5 is {}".format(sword5.type))

        sword6 = Sword("steel")
        print("creating sword6 that is {}".format(sword6.type))
        print("crafting sword5 and sword6 into a new sword7...")
        sword7 = sword5 + sword6
    except Exception as e:
        print(e)


main()
