class Square:

    def __init__(self, is_dls=None, is_tls=None, is_dws=None, is_tws=None, tile=None):
        self.dls = is_dls
        self.tls = is_tls
        self.dws = is_dws
        self.tws = is_tws
        self.tile = tile
        self.value = self.get_value()

    def __str__(self):
        pass

    def __repr__(self):
        return "{0.value}".format(self)

    def get_value(self):
        if self.dls:
            value = 'Double Letter Score'
        elif self.tls:
            value = 'Triple Letter Score'
        elif self.dws:
            value = 'Double Word Score'
        elif self.tws:
            value = 'Triple Word Score'
        else:
            value = None
        return value
