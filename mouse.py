'''
Write solutions to 3. New Mouse Release here.

Author: Kayven Chen
SID: 530654658
Unikey: kche4026
'''

'''
Keep this line!
'''
import random
import art

TYPE_OF_MOUSE = (None, "Brown", "Field", "Grey", "White", "Tiny")

def generate_probabilities(cheese_type, enchant=False) -> tuple:
    if cheese_type == "Cheddar":
            probabilities = [0.5, 0.1, 0.15, 0.1, 0.1, 0.05]
    if cheese_type == "Marble":
            probabilities = [0.6, 0.05, 0.2, 0.05, 0.02, 0.08]
    if cheese_type == "Swiss":
        probabilities = [0.7, 0.01, 0.05, 0.05, 0.04, 0.15]
        if enchant:
            probabilities[0] = 0.45
            probabilities[5] = 0.4
    return tuple(probabilities)

def generate_coat(type_of_mouse: str) -> str:
    dict = {TYPE_OF_MOUSE[0]: None,
            TYPE_OF_MOUSE[1]: art.BROWN, 
            TYPE_OF_MOUSE[2]: art.FIELD, 
            TYPE_OF_MOUSE[3]: art.GREY,
            TYPE_OF_MOUSE[4]: art.WHITE, 
            TYPE_OF_MOUSE[5]: art.TINY}
    return dict[type_of_mouse]
    


def generate_mouse(cheese="Cheddar", enchant=False) -> str | None:
    '''
    Spawn a random mouse during a hunt depending on cheese type
    Hint: You should be using TYPE_OF_MOUSE in this function.
    Returns:
        spawn_mouse: str | None, type of mouse
    '''

    probabilities = generate_probabilities(cheese, enchant)
    random_value = random.random()
    
    i = 0
    bounds = []
    lower_bound = 0
    while i < len(probabilities):
        upper_bound = lower_bound + probabilities[i]
        bounds.append((lower_bound, upper_bound))
        lower_bound = upper_bound
        i += 1
    
    i = 0
    while i < len(bounds):
        lower_bound, upper_bound = bounds[i]
        if random_value < upper_bound and random_value >= lower_bound:
            spawn_mouse = TYPE_OF_MOUSE[i]
            i = len(probabilities)
        i += 1
    return spawn_mouse


def loot_lut(mouse_type: str | None) -> tuple:
    '''
    Look-up-table for gold and points for different types of mouse
    Parameter:
        mouse_type: str | None, type of mouse
    Returns:
        gold:       int, amount of gold reward for mouse
        points:     int, amount of points given for mouse
    '''
    dict = {TYPE_OF_MOUSE[0]: (0, 0), TYPE_OF_MOUSE[1]: (125, 115),
            TYPE_OF_MOUSE[2]: (200, 200), TYPE_OF_MOUSE[3]: (125, 90),
            TYPE_OF_MOUSE[4]: (100, 70), TYPE_OF_MOUSE[5]: (900, 200)}
    gold = dict[mouse_type][0]
    points = dict[mouse_type][1]
    return gold, points


class Mouse:
    def __init__(self, cheese="Cheddar", enchant=False):
        self.name = generate_mouse()
        self.gold, self.points = loot_lut(self.name)
        self.coat = generate_coat(self.name)
        
    def get_name(self) -> str:
        return self.name

    def get_gold(self) -> int:
        return self.gold
    
    def get_points(self) -> int:
        return self.points
    
    def __str__(self):
        if self.name == None:
            return "None"
        return self.name


