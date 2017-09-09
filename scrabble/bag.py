from tiles import Tile
from tileholder import Tileholder

import sys

class Bag:
    """ bag object """
    def __init__(self, config=None):
        self.contents = list()
        self.config = config
        self.construct_bag()
        self.letter_count = len(self.contents)

    def __str__(self):
        return "Scrabble Letter Bag"

    def __repr__(self):
        return "{0} letters remaining"

    def construct_bag(self):
        """ adds tile objects to bag object """
        testing = None

        alphabet = self.config['test']['bag']['letters'].keys() if testing \
            else self.config['bag']['letters'].keys()

        for letter in alphabet:
            bag_amount = self.config['test']['bag']['letters'][letter]['bag_amount'] if testing \
                else self.config['bag']['letters'][letter]['bag_amount']
            point_val = self.config['test']['bag']['letters'][letter]['point_val'] if testing \
                else self.config['bag']['letters'][letter]['point_val']
            count = 0

            while count < bag_amount:
                if testing:
                    c = Tile(letter='C', point_val=point_val, id=count+1, bag_amount=bag_amount)
                    a = Tile(letter='A', point_val=point_val, id=count+1, bag_amount=bag_amount)
                    t = Tile(letter='T', point_val=point_val, id=count+1, bag_amount=bag_amount)
                    cat = [c, a, t]

                    for tile in cat:
                        self.contents.append(tile)
                    break
                else:
                    tile = Tile(letter=letter.upper(), point_val=point_val, id=count+1, bag_amount=bag_amount)
                    self.contents.append(tile)
                    count += 1

        # check tile amount
        tile_count = len(self.contents)
        if tile_count < 100 and not testing:
            raise ValueError("Letter bag only contains {} tiles.  Must contain a total of 100.".format(
                tile_count))

        return None