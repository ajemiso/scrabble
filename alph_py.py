from board import Board
from bag import Bag
from yaml import load


class Scrabble:

    def __init__(self, config_file_path='config/scrabble_config.yml'):
        self.config_file_path = config_file_path
        self.config = self.load_config()
        self.board = Board()
        self.bag = Bag(config=self.config)

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def load_config(self):
        stream = open(self.config_file_path, 'r')
        config = load(stream)
        return config

