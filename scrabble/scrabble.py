from board import Board
from bag import Bag
from scoreboard import Scoreboard
from tileholder import Tileholder
from yaml import load

import random

# TODO: complete scoreboard
# TODO: add functionality to record score when tiles placed on board


class Scrabble:
    """ main game object """
    def __init__(self, config_file_path='config/scrabble_config.yml', players=1):
        self.config = self.load_config(config_file_path)
        self.board = Board()  # creates board object along with values for each square
        self.bag = Bag(config=self.config)
        self.scoreboard = Scoreboard()
        self.players = players
        self.tileholders = dict()
        self.add_tileholders()

    def __str__(self):
        return "Scrabble Game Instance"

    def __repr__(self):
        return "{0.__class__.__name__}".format(self)

    def load_config(self, config_file_path):
        """ loads configuration file """
        stream = open(config_file_path, 'r')
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
            return True
        else:
            return None

    def pick_first_tiles(self):
        """ picks first seven tiles for every player via grab_more_tiles method """
        for i in self.tileholders.keys():
            self.get_tiles(player=i)
        return None

    def add_word(self, player, word, coords):  # word: 'CAT', coords: [(7, 7), (7, 8), (7, 9)]
        if player <= 4 and len(word) <= 7:  # player limit: 4, word limit

            # check to see if letters are available in tileholder
            tileholder = self.tileholders[player].tiles

            for word_ind, req_letter in enumerate(word):  #'C'
                for pop_ind, tile in enumerate(tileholder):  # ['A', 'B', 'C', 'T']
                    if req_letter.isalpha() and req_letter == tile.letter:
                        # take tile from tileholder and place onto board (square)
                            coord = coords[word_ind]  # get indexed x,y coordinate
                            self.board.contents['board'][coord].tile = tileholder.pop(pop_ind)
                    elif not req_letter.isalpha():
                        raise ValueError("{} is not a letter of the alphabet.  Please re-enter word."
                                         .format(req_letter))

            # add score
            # points =
            # player, word, points, turn, dls, tls, dws, tws
        return True

    def get_tiles(self, player=None):
        """adds more tiles to tileholder (max: 7)"""
        try:
            self.tileholders[player]
        except IndexError:
            return 0

        tileholder = self.tileholders[player]
        amount_needed = 7 - tileholder.get_tile_count()  # reset tile count before adding tiles

        while amount_needed > 0:
            tile_index = len(self.bag.contents) - 1

            # pick random number
            rand_ind = random.randint(0, tile_index)

            # get tile by index
            tile = self.bag.contents.pop(rand_ind)

            # add to tileholder
            tileholder.tiles.append(tile)
            amount_needed -= 1
        return True if amount_needed > 0 else None






