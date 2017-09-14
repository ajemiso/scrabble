from scrabble import Scrabble

s = Scrabble(players=3)

first = s.who_goes_first()

s.pick_first_tiles()

coords = [
    (0, 0),
    (0, 1),
    (0, 2),
]

word = list()

word = 'ZOO'

s.add_word(s.player_turn_queue,'test', word, coords)
            # CAT
           # { player: [1], word: { C: (7, 7), A: (7, 8), T: (7, 9) }

s.get_tiles(player=1)
test = s.scoreboard.get_word_score(player=1, turn=1)


stop = None