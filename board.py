from square import Square


class Board:

    def __init__(self):
        self.size = 15 #TODO: add try/except clause here
        self.grid = self.build_grid()
        self.contents = dict(
            dls_coords=self._get_dls_coords(),
            dws_coords=self._get_dws_coords(),
            tls_coords=self._get_tls_coords(),
            tws_coords=self._get_tws_coords(),
        )
        self.contents['board'] = self.load_board()

    def __str__(self):
        return "Scrabble Board"

    def __repr__(self):
        return "{0.__class__.__name__}".format(self)

    def build_grid(self):

        row = list(range(0, self.size))
        col = list(range(0, self.size))

        grid = [(x, y) for x in row for y in col]
        return grid

    def load_board(self):
        board = dict()
        for coord in self.grid:
            if coord in self.contents['dls_coords']:
                board[coord] = Square(is_dls=1)
            elif coord in self.contents['dws_coords']:
                board[coord] = Square(is_dws=1)
            elif coord in self.contents['tls_coords']:
                board[coord] = Square(is_tls=1)
            elif coord in self.contents['tws_coords']:
                board[coord] = Square(is_tws=1)
            else:
                board[coord] = Square()
        return board

    @staticmethod
    def _get_dls_coords():

        c1 = 0, 3
        c2 = 0, 11
        c3 = 2, 6
        c4 = 2, 8
        c5 = 3, 0
        c6 = 3, 7
        c7 = 3, 14
        c8 = 6, 2
        c9 = 6, 6
        c10 = 6, 8
        c11 = 6, 12
        c12 = 7, 3
        c13 = 7, 11
        c14 = 8, 2
        c15 = 8, 6
        c16 = 8, 8
        c17 = 8, 12
        c18 = 11, 0
        c19 = 11, 7
        c20 = 11, 14
        c21 = 12, 6
        c22 = 12, 8
        c23 = 14, 3
        c24 = 14, 11

        dls_coords = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20,
                      c21, c22, c23, c24]

        return dls_coords

    @staticmethod
    def _get_tls_coords():

        c1 = 1, 5
        c2 = 1, 9
        c3 = 5, 1
        c4 = 5, 5
        c5 = 5, 9
        c6 = 5, 13
        c7 = 9, 1
        c8 = 9, 5
        c9 = 9, 9
        c10 = 9, 13
        c11 = 13, 5
        c12 = 13, 9

        tls_coords = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12]

        return tls_coords

    @staticmethod
    def _get_dws_coords():
        c1 = 1, 1
        c2 = 1, 13
        c3 = 2, 2
        c4 = 2, 12
        c5 = 3, 3
        c6 = 3, 11
        c7 = 4, 4
        c8 = 4, 10
        c9 = 10, 4
        c10 = 10, 10
        c11 = 11, 3
        c12 = 11, 11
        c13 = 12, 2
        c14 = 12, 12
        c15 = 13, 1
        c16 = 13, 13

        dws_coords = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16]

        return dws_coords

    @staticmethod
    def _get_tws_coords():

        c1 = 0, 0
        c2 = 0, 7
        c3 = 0, 14
        c4 = 7, 0
        c5 = 7, 14
        c6 = 14, 0
        c7 = 14, 7
        c8 = 14, 14

        tws_coords = [c1, c2, c3, c4, c5, c6, c7, c8]

        return tws_coords

    def save(self):
        pass

    def reset(self):
        pass

    def move(self):
        pass

