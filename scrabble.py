from board import Board
from bag import Bag
from tileholder import Tileholder
from yaml import load

import random


class Scrabble:
    """ main game object """
    def __init__(self, config_file_path='config/scrabble_config.yml', players=None):
        self.config_file_path = config_file_path
        self.config = self.load_config()
        self.board = Board() # creates board object along with values for each square
        self.bag = Bag(config=self.config)
        self.players = players
        self.tileholders = dict()
        self.add_tileholders()

    def __str__(self):
        return "Scrabble Game Instance"

    def __repr__(self):
        return "{0.__class__.__name__}".format(self)

    def load_config(self):
        """ loads configuration file """
        stream = open(self.config_file_path, 'r')
        config = load(stream)
        return config

    def add_tileholders(self):
        """ adds empty tileholders based on number of players """
        if self.players <= 4:
            count = 0
            while count < self.players:
                th = Tileholder()
                self.tileholders[count + 1] = th
                count += 1
            return 1
        else:
            return 0

    def add_first_tiles(self):
        """ adds first seven tiles to tileholder """
        for i, th in enumerate(self.tileholders):
            count = 0
            while count < 7:
                tile_index = len(self.bag.contents) - 1

                # pick random number
                rand_num = random.randint(0, tile_index)

                # get index of tile
                tile = self.bag.contents[rand_num]

                # add to tileholder
                self.tileholders[i+1].tiles.append(tile)
                count += 1
        return None



