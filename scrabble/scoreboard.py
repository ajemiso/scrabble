import sqlite3

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
        sql = '''CREATE TABLE scoreboard
        (
            ID INT PRIMARY KEY NOT NULL,
            PLAYER INT NOT NULL,
            NAME CHAR(30),
            WORD CHAR(15),
            POINTS INT,
            TURN INT,
            COORDS ,
            DLS INT,
            TLS INT,
            DWS INT,
            TWS INT
        );'''

        self.dbh.execute(sql)
        return True

    def add_score(self, player=None, word=None, points=None, turn=None, dls=None, tls=None, dws=None, tws=None):
        sql = '''
        INSERT INTO scoreboard (PLAYER, WORD, POINTS, TURN, DLS, TLS, DWS, TWS)
        VALUES ({}, {}, {}, {}, {}, {}, {}, {});
        '''.format(player, word, points, turn, dls, tls, dws, tws)

        self.dbh.execute(sql)
        return True
