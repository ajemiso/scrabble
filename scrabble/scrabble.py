from board import Board
from bag import Bag
from scoreboard import Scoreboard
from tileholder import Tileholder
from yaml import load

import random

# TODO: complete scoreboard
# TODO: add functionality to record score when tiles placed on board
# TODO: test for consecutive tile placement in add_word()
# TODO: develop AI opponent


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
                th = Tileholder(self.config)
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

    def add_word(self, player, name, word, coords):  # word: 'CAT', coords: [(7, 7), (7, 8), (7, 9)]
        """ adds player's word to board & records score to DB """
        square_scores = { # used for recording type of additional board score if applicable
            "dls": 0,
            "dws": 0,
            "tls": 0,
            "tws": 0,
        }

        if player <= 4 and len(word) <= 7:  # player limit: 4, word limit

            # initialize point values
            points = 0
            word_score = list()

            # check to see if letters are available in tileholder
            tileholder = self.tileholders[player]

            for word_ind, req_letter in enumerate(word):  # ex: 'C'
                # for pop_ind, tile in enumerate(tileholder.tiles):  # ex: ['A', 'B', 'C', 'T', 'D', etc..]
                    # if req_letter.isalpha() and req_letter == tile.letter:
                word_list = tileholder.tiles[req_letter]
                if req_letter.isalpha() and len(word_list) > 0:

                    # take tile from tileholder and place onto board (square)
                    coord = coords[word_ind]  # get indexed x,y coordinate
                    tile = tileholder.tiles[req_letter].pop()
                    self.board.contents['board'][coord].tile = tile

                    # get multiplier value for any double letter/triple letter scores
                    square = self.board.contents['board'][coord]
                    letter_score = self._get_square_score(tile, square, 'letter')

                    # record dls or tls for DB
                    if letter_score == 2:
                        square_scores['dls'] += 1

                    if letter_score == 3:
                        square_scores['tls'] += 1

                    point_val = tile.point_val
                    points += (point_val * letter_score)  # letter score multiplier will equal 1 if ! ls

                    # get multiplier value for any double word/triple word scores, append value(s) to list for later
                    word_score.append(self._get_square_score(tile, square, 'word'))

                elif not req_letter.isalpha():
                    raise ValueError("{} is not a letter of the alphabet.  Please re-enter word."
                                     .format(req_letter))

            # apply word score multiplier (multiplier will equal 1 unless dws or tws applies)
            for multiplier in word_score:
                points *= multiplier

                # record dws or tws for DB
                if multiplier == 2:
                    square_scores['dws'] += 1

                if multiplier == 3:
                    square_scores['tws'] += 1

            # add score to db
            turn = tileholder.turn_number

            last_coord_ind = len(coords) - 1
            start_coord = '{};{}'.format(coords[0][0], coords[0][1])
            end_coord = '{};{}'.format(coords[last_coord_ind][0], coords[last_coord_ind][1])

            self.scoreboard.add_score(
                player=player,
                name=name,
                word=word,
                points=points,
                turn=turn,
                start_coord=start_coord,
                end_coord=end_coord,
                dls=square_scores['dls'],
                tls=square_scores['tls'],
                dws=square_scores['dws'],
                tws=square_scores['tws']
            )

            tileholder.turn_number += 1
            tileholder.get_tile_count()
        return True

    @classmethod
    def _get_square_score(self, tile, square, score_type):
        """ returns letter score multiplier for tile """
        double_score = square.dls if score_type == 'letter' else square.dws
        triple_score = square.tls if score_type == 'letter' else square.tws
        if double_score:
            square_score = 2
        elif triple_score:
            square_score = 3
        else:
            square_score = 1
        return square_score

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
            # tileholder.tiles.append(tile)
            tileholder.tiles[tile.letter].append(tile)
            amount_needed -= 1

        tileholder.get_tile_count()
        return True if amount_needed > 0 else None








