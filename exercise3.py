
# the baker's dilemma: how many cakes can we make with 2.5 kilos of flour
flour_per_cake = 250
total_flour = 2.5 * 1000
number_of_cakes = int(total_flour // flour_per_cake)
print(f"we can make {number_of_cakes} cakes with {total_flour} grams of flour")


# laiming territories: use assignment operator to 
# claim a variable kingdom with value Pythonland
kingdom = "Pythonland"
print(f"the kingdom is claimed for {kingdom}")

# fashion contest: use comparison operator to check 
# if shirt1 is cheaper than shirt 2
shirt1, shirt2 = 45, 50

if shirt1 < shirt2:
    print("shirt1 is cheaper than shirt2")
else:
    print("shirt1 is not cheaper than shirt2")

# rainy day dilemma: write logical operation to 
# determine if you should bring an umbrella if 
# it's going to rain or going to rain heavily

weather = "rain"
if weather == "rain" or weather == "heavy rain":
    print("it's gonna rain, make sure to bring an umbrella")

# determine order of precedence, prediction: multiplication then other
x = str(3 + 5 * 2 - 8)
print("3 + 5 * 2 - 8 = " + x)

# pastry fraction: divide 10 pastries equally among 3 friends, how many are left
pastries = 10
friends = 3
pastries_per_friend = pastries // friends
leftovers = pastries % friends
print(f"we each can eat {pastries_per_friend} pastries, and there is {leftovers} leftover")

# kingdom expansion: reassign kingdom's value from "Pythonland" to "Pythonland is wonderful"
kingdom = "Pythonland is wonderful"
print(kingdom)

# royal due: use comparison operator to check 
# if knight1 is is as strong as knight2
knight1, knight2 = 45, 50

if knight1 == knight2:
    print("knight1 & knight2 are well-matched adversaries")
else:
    print("knight1 & knight2 are not well-matched adversaries")

# chef special: determine if chef can make pancakes

eggs = True
flour = False

if eggs and flour == True:
    print("the chef can make pancakes :)")
else:
    print("the chef does not have the right ingredients to make pancakes :(")

# medieval architecture: what are the castles dimensions if doubling the castles height and halving it's width

castle_height = 100
moat_width = 50

print(f"the castle's new height is {castle_height * 2} units and its moat's new width is {moat_width / 2} units")