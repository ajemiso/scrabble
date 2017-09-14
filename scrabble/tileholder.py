import random


class Tileholder:

    def __init__(self, config):
        self.config = config
        self.tiles = dict()
        self.create_letter_values()
        self.tile_count = self.get_tile_count()
        self.turn_number = 1
        self.start_letter = None

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def get_tile_count(self):
        """ returns tile count for tileholder """
        tile_count = 0
        for tiles in self.tiles.values():
            tile_count += len(tiles)
        return tile_count

    def create_letter_values(self):
        """ creates lists inside of tiles dictionary to hold tiles (alpha keys) """
        for i in self.config['bag']['letters'].keys():
            self.tiles[i.upper()] = list()
        return None
