import sqlite3


# (PLAYER, WORD, POINTS, TURN, XCOORD, YCOORD, DLS, TLS, DWS, TWS)


class Scoreboard:

    def __init__(self, db_name='db/scoreboard.db'):
        self.dbh = self.db_connect(db_name)
        self.create_table()

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def db_connect(self, db_name):
        return sqlite3.connect(db_name)

    def create_table(self):
        sql = '''CREATE TABLE IF NOT EXISTS scoreboard
        (
            PLAYER INT NOT NULL,
            NAME CHAR(30),
            WORD CHAR(15),
            POINTS INT,
            TURN INT NOT NULL,
            START_COORD CHAR(5) NOT NULL,
            END_COORD CHAR(5) NOT NULL,
            DLS INT,
            TLS INT,
            DWS INT,
            TWS INT,
            TIME_PLAYED TIMESTAMP
        );'''

        self.dbh.execute(sql)
        self.dbh.commit()
        return True

    def add_score(self, player=None, name=None, word=None, points=None, turn=None, start_coord=None, end_coord=None, dls=None, tls=None,
                  dws=None, tws=None, time_played=None):

        sql = "INSERT INTO scoreboard (PLAYER, NAME, WORD, POINTS, TURN, START_COORD, END_COORD, DLS, TLS, DWS, TWS," \
              " TIME_PLAYED) \
          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

        self.dbh.execute(sql, (player, name, word, points, turn, start_coord, end_coord, dls, tls, dws, tws, time_played))
        self.dbh.commit()
        return True

    def get_word_score(self, player=None, turn=None):

        sql = '''
            SELECT * \
            FROM scoreboard
        '''
        c = self.dbh.cursor()
        c.execute("SELECT points FROM scoreboard WHERE player = ? AND turn = ?", (player, turn))
        result = c.fetchall()
        return result
