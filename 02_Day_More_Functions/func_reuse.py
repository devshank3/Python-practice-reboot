# def mix_and_cook():
#     print('Mixing the ingredients')
#     print('Heating the pan')
#     print('Pouring the mixture into a frying pan')
#     print('Cooking the first side')
#     print('Flipping it!')
#     print('Cooking the other side\n')

# def make_pancake():
#     mix_and_cook()
#     pancake = "A delicious pancake"
#     return pancake

# def make_omelette():
#     mix_and_cook()
#     omelette = "A tasty omelette"
#     return omelette


# barron_breakfast = make_omelette()
# olivia_breakfast = make_pancake()

# print(f'Barron is having {barron_breakfast}\n')
# print(f'Olivia is having {olivia_breakfast}\n')

def mix_and_cook():
    print('Mixing the ingredients')
    print('Heating the pan')
    print('Pouring the mixture into a frying pan')
    print('Cooking the first side')
    print('Flipping it!')
    print('Cooking the other side\n')

def make_pancake(ingredients=None):
    mix_and_cook()
    pancake = "A delicious pancake made with " + (ingredients if ingredients else "standard ingredients")
    return pancake

def make_omelette(ingredients=None):
    mix_and_cook()
    omelette = "A tasty omelette made with " + (ingredients if ingredients else "standard ingredients")
    return omelette

#takes in tuple arguments
def make_fancy_omelette(*ingredients):
    mix_and_cook()
    omelette = "A fancy omelette with " + ", ".join(ingredients)
    return omelette

barron_breakfast = make_fancy_omelette("smoked salmon", "cream cheese", "chives")
olivia_breakfast = make_pancake("blueberries")

print(f'Barron is having {barron_breakfast}\n')
print(f'Olivia is having {olivia_breakfast}\n')