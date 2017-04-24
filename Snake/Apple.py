import random


class Apple(object):

    def __init__(self):
        x = random.randint(1, 49)
        y = random.randint(1, 49)

        self.coords = (x, y)

    def __getattr__(self, item=None):
        return self.coords
