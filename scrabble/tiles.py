class Tile:

    def __init__(self, letter=None, point_val=None, id=None, bag_amount=None):
        self.letter = letter
        self.point_val = point_val
        self.id = id
        self.bag_amount = bag_amount

    def __str__(self):
        return "{0.letter} ({0.id} of {0.bag_amount})".format(self)

    def __repr__(self):
        return "{0.letter}".format(self)