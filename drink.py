class Drink:
    def __init__(self, size="small", water=10):
        self.size = size
        self.suger = 2
        self.water = water

    def change_size(self, size):
        self.size = size

    def add_suger(self, amount):
        self.suger += amount
