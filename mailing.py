from adress import Adress


class Mailing:

    def __init__(self, to_adress: Adress, from_adress: Adress, cost, track):
        self.to_adress = to_adress
        self.from_adress = from_adress
        self.cost = cost
        self.track = track
