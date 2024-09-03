


class Ship:
    def __init__(self, locations: list):
        self.locations = locations
        self.destroyed: bool = False

    def hit(self):
        self.destroyed = True