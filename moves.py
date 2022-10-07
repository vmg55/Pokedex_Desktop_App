class Move:

    def __init__(self, name, power, accuracy, type, category, pp=10, description=None, special_effect=None):
        self.name = name
        self.power = power
        self.accuracy = accuracy
        self.type = type
        self.category = category
        self.pp = pp
        self.description = description
        self.special_effect = special_effect

