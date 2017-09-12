import random


class Tileholder:

    def __init__(self, config):
        self.config = config
        self.tiles = dict()
        self.create_letter_values()
        self.tile_count = self.get_tile_count()
        self.turn_number = 1

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def get_tile_count(self):
        tile_count = 0
        for tiles in self.tiles.values():
            tile_count += len(tiles)
        return tile_count

    # def add_tiles(self, tiles):
    #     if sum(len(tiles), len(self.tiles)) <= 7:
    #         self.tiles.append(tiles)
    #         return 1
    #     else:
    #         return None

    def create_letter_values(self):
        for i in self.config['bag']['letters'].keys():
            self.tiles[i.upper()] = list()
        return None
