# coding: utf-8

""" Creating an Items class
to give a name and a position x,y to all the items of the game.
"""


class Items:

    def __init__(self, name, y, x):
        super().__init__()
        self.name = name
        self.x = int(x)
        self.y = int(y)
        self.is_collected = False

    """ Through this booleen method, 
    the item can be collected an added to the hero's inventory
    """
    def go_to_inventory(self):
        self.is_collected = True
