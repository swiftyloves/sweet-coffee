class Drink:
    def __init__(self, size="small"):
        self.size = size
        self.suger = 2

    def change_size(self, size):
        self.size = size

    def add_suger(self, amount):
        self.suger += amount
