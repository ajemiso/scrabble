class Tile:

    alphabet = 'abcdefghijklmnopqrstuvwxyz'


    def __init__(self, letter=None, point_val=None, id=None, bag_amount=None):
        self.letter = letter
        self.point_val = point_val
        self.id = id
        self.bag_amount = bag_amount
        self.start_val = self.closest_to_a(self.letter)

    def __str__(self):
        return "{0.letter} ({0.id} of {0.bag_amount})".format(self)

    def __repr__(self):
        return "{0.letter}".format(self)

    @classmethod
    def closest_to_a(cls, letter):
        start_vals = {k: len(cls.alphabet) - i for i, k in enumerate(cls.alphabet)}
        return start_vals[letter.lower()]
