class Square:

    def __init__(self, is_dls=None, is_tls=None, is_dws=None, is_tws=None, tile=None):
        self.dls = is_dls if is_dls != 0 else 0
        self.tls = is_tls if is_tls != 0 else 0
        self.dws = is_dws if is_dws != 0 else 0
        self.tws = is_tws if is_tws != 0 else 0
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
