from random import randint

class Die:
    """A class representing a single die"""
    
    def __init__(self, num_side=6):
        "Assume a six-sided die"
        self.num_sides = num_sides
        
    