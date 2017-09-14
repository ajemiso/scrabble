from board import Board
from bag import Bag
from scoreboard import Scoreboard
from tileholder import Tileholder
from yaml import load

import datetime
# import pytz
import random

# TODO: complete scoreboard
# TODO: test who_goes_first() with multiple players
# TODO: test for consecutive tile placement in add_word() - working, test more though
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
        self.player_turn_queue = None

    def __str__(self):
        return "Scrabble Game Instance"

    def __repr__(self):
        return "{0.__class__.__name__}".format(self)

    @staticmethod
    def load_config(config_file_path):
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

    def who_goes_first(self):
        """ executes helper methods to determine who goes first.  Returns tuple: (player, tile_value)"""
        all_player_results = self._assign_start_val()
        winning_player = self._get_max_start_val()
        if all_player_results and winning_player:
            return all_player_results, winning_player

    def pick_first_tiles(self):
        """ picks first seven tiles for every player via grab_more_tiles method """
        for i in self.tileholders.keys():
            self.get_tiles(player=i)
        return None

    def add_word(self, player, name, word, coords):  # word: 'CAT', coords: [(7, 7), (7, 8), (7, 9)]
        """ adds player's word to board & records score to DB """
        if self._coords_are_consecutive(coords):
            square_scores = { # used for recording type of additional board score if applicable
                "dls": 0,
                "dws": 0,
                "tls": 0,
                "tws": 0,
            }

            if player <= 4 and len(word) <= 7 and len(word) == len(coords):  # player limit: 4, word limit

                # initialize point values
                points = 0
                word_score = list()

                # check to see if letters are available in tileholder
                tileholder = self.tileholders[player]

                for word_ind, req_letter in enumerate(word):  # ex: 'C'
                    # for pop_ind, tile in enumerate(tileholder.tiles):  # ex: ['A', 'B', 'C', 'T', 'D', etc..]
                    word_list = tileholder.tiles[req_letter]
                    if req_letter.isalpha() and len(word_list) > 0:

                        # take tile from tileholder and place onto board (square)
                        coord = coords[word_ind]  # get indexed x,y coordinate
                        tile = tileholder.tiles[req_letter].pop()
                        self.board.contents['board'][coord].tile = tile

                        # get multiplier value for any double letter/triple letter scores
                        square = self.board.contents['board'][coord]
                        letter_score = self._get_square_score(square, 'letter')

                        # record dls or tls for DB
                        if letter_score == 2:
                            square_scores['dls'] += 1

                        if letter_score == 3:
                            square_scores['tls'] += 1

                        point_val = tile.point_val
                        points += (point_val * letter_score)  # letter score multiplier will equal 1 if ! ls

                        # get multiplier value for any double word/triple word scores, append value(s) to list for later
                        word_score.append(self._get_square_score(square, 'word'))

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

                # parse coords data for DB entry
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
                    tws=square_scores['tws'],
                    time_played=datetime.datetime.now(),
                )

                tileholder.turn_number += 1
                tileholder.get_tile_count()
                self._set_next_player()
                return True
        else:
            return None
        return None

    def get_tiles(self, player=None):
        """adds more tiles to tileholder (max: 7)"""
        try:
            self.tileholders[player]
        except IndexError:
            return 0

        tileholder = self.tileholders[player]
        amount_needed = 7 - tileholder.get_tile_count()  # reset tile count before adding tiles

        while amount_needed > 0:
            rand_ind = self._get_rand_ind()

            # get tile by index
            tile = self.bag.contents.pop(rand_ind)

            # add to tileholder
            tileholder.tiles[tile.letter].append(tile)
            amount_needed -= 1

        tileholder.get_tile_count()
        return True if amount_needed > 0 else None

    # private methods
    def _get_rand_ind(self):
        """ returns random bag (list) index number """
        tile_index = len(self.bag.contents) - 1
        rand_ind = random.randint(0, tile_index)

        return rand_ind

    def _assign_start_val(self):
        """ assigns start value to each tileholder for later comparison (to see who starts first) """
        results = dict()
        for k, tileholder in self.tileholders.items():
            rand_ind = self._get_rand_ind()
            tile = self.bag.contents[rand_ind]

            # get start value
            start_val = tile.start_val

            # assign start letter to player
            tileholder.start_letter = tile.letter

            # add start value to tileholder
            tileholder.start_val = start_val if start_val else None

            # create dictionary of all players and all start letters
            results[k] = tileholder.start_letter

        output_check = [1 for tileholder in self.tileholders.values() if tileholder.start_val]

        if len(output_check) == len(self.tileholders):
            return results
        else:
            return None

    def _get_max_start_val(self):
        """ returns highest start letter value to determine which tileholder starts the game """
        max_val = 0
        for i, tileholder in enumerate(self.tileholders.values()):
            player = i+1  # player 1, 2, 3, etc.
            tile_start_val = self.tileholders[player].start_val  # 23

            if tile_start_val and tile_start_val > max_val:
                max_val = tile_start_val
                self.player_turn_queue = player
        return self.player_turn_queue

    @staticmethod
    def _coords_are_consecutive(coords):
        """ verifies that tile coordinates are consecutive when placing word on board """
        # split coords
        x_coords = [c[0] for c in coords]  # [0, 0, 0]
        y_coords = [c[1] for c in coords]  # [0, 1, 2]

        a, b, c = 0, 0, 0

        # if x_coords are all the same, test y_coords for consecutiveness, & vice versa
        if len(set(x_coords)) == 1:
            a, b, c = y_coords[0], y_coords[1], y_coords[2]
        elif len(set(y_coords)) == 1:
            a, b, c = x_coords[0], x_coords[1], x_coords[2]
        else:
            return None
        return True if b - a == 1 and c - b == 1 else None

    @staticmethod
    def _get_square_score(square, score_type):
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

    def _set_next_player(self):
        """ sets next player turn """
        if self.player_turn_queue < self.players:
            self.player_turn_queue += 1
            return True
        elif self.player_turn_queue == self.players:
            self.player_turn_queue = 1
            return True
        else:
            return None
