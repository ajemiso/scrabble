from scrabble import Scrabble

s = Scrabble(players=1)

s.pick_first_tiles()

coords = [
    (7, 7),
    (7, 8),
    (7, 9),
]

word = list()
for tile in s.tileholders[1].tiles[0:3]:
    letter = tile.letter if tile.letter != 'BLANK' else 'A'
    word.append(letter)

word = ''.join(word)

s.add_word(1, word, coords)
            # CAT
           # { player: [1], word: { C: (7, 7), A: (7, 8), T: (7, 9) }

s.get_tiles(player=1)

stop = None