from scrabble import Scrabble

s = Scrabble(players=1)

s.pick_first_tiles()

coords = [
    (1, 9),
    (1, 10),
    (1, 11),
]

word = list()

word = 'ZOO'

s.add_word(1,'test', word, coords)
            # CAT
           # { player: [1], word: { C: (7, 7), A: (7, 8), T: (7, 9) }

s.get_tiles(player=1)
test = s.scoreboard.get_last_word_score(player=1, turn=1)

stop = None