""" A Functional Breakfast """
""" As per instructions """
def mix_and_cook():
    print('Mixing the ingredients')
    print('greasing the frying pan')
    print('Pouring the mixture into a frying pan')
    print('Cooking the first side')
    print('Flipping it!')
    print('Cooking the other side')

def make_omelette():
    mix_and_cook()
    omelette = 'a tasty omelette'
    return omelette

def make_pancake():
    mix_and_cook()
    pancake = 'a tasty pancake'
    return pancake

""" Figuring out variables in functions on my own """

def make_dish(x):
    print('Mixing the ingredients')
    print('greasing the frying pan')
    print('Pouring the mixture into a frying pan')
    print('Cooking the first side')
    print('Flipping it!')
    print('Cooking the other side')
    y = 'a tasty ' + x
    return y

def cook_omelette():
    return make_dish('omelette')

def cook_pancake():
    return make_dish('pancake')
