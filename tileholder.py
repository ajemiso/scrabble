import random


class Tileholder:

    def __init__(self):
        self.tiles = list()
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def add_tiles(self, tiles):
        if sum(len(tiles), len(self.tiles)) <= 7:
            self.tiles.append(tiles)
            return 1
        else:
            return None

    def remove_tiles(self, tiles):
        pass

    def view_tiles(self):
        pass