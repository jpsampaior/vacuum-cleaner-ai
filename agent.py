import random


class Location:
    def __init__(self, i, j):
        self.i = i
        self.j = j


class Agent:
    def __init__(self, cols, rows):
        self.location = Location(random.randint(0, rows - 1), random.randint(0, cols - 1))
        self.performance = 0
        self.visited_squares = []
