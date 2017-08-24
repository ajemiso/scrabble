from tiles import Tile


class Bag:

    def __init__(self, config=None):
        self.contents = dict()
        self.config = config
        self.add_tiles()

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def add_tiles(self):
        self.contents['bag'] = list()

        alphabet = self.config['bag']['letters'].keys()

        for letter in alphabet:
            bag_amount = self.config['bag']['letters'][letter]['bag_amount']
            point_val = self.config['bag']['letters'][letter]['point_val']
            count = 0

            while count < bag_amount:
                tile = Tile(letter=letter, point_val=point_val, id=count+1, bag_amount=bag_amount)
                self.contents['bag'].append(tile)
                count += 1

        # check tile amount
        tile_count = len(self.contents['bag'])
        if tile_count < 100:
            raise ValueError("Letter bag only contains {} tiles.  Must contain a total of 100.".format(
                tile_count))

        return None