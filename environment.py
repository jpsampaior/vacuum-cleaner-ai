import random
from agent import Agent


class Environment:
    def __init__(self):
        self.cols = 5
        self.rows = 5
        self.matrix = [[random.choice(['clean', 'dirty']) for _ in range(self.cols)] for _ in range(self.rows)]
        self.agent = Agent(self.cols, self.rows)

    def percept(self):
        return (self.agent.location.i, self.agent.location.j), self.matrix[self.agent.location.i][self.agent.location.j]

    def execute_action(self, action):
        if action == 'right':
            if self.agent.location.j < self.cols - 1:
                self.agent.location.j += 1
                self.agent.performance -= 1
        elif action == 'left':
            if self.agent.location.j > 0:
                self.agent.location.j -= 1
                self.agent.performance -= 1
        elif action == 'up':
            if self.agent.location.i > 0:
                self.agent.location.i -= 1
                self.agent.performance -= 1
        elif action == 'down':
            if self.agent.location.i < self.rows - 1:
                self.agent.location.i += 1
                self.agent.performance -= 1
        elif action == 'suck':
            if self.matrix[self.agent.location.i][self.agent.location.j] == 'dirty':
                self.agent.performance += 10
            self.matrix[self.agent.location.i][self.agent.location.j] = 'clean'

        location = (self.agent.location.i, self.agent.location.j)
        if location not in self.agent.visited_squares:
            self.agent.visited_squares.append(location)

    def start_cleaning_random(self):
        while len(self.agent.visited_squares) != self.rows * self.cols:
            move = random.choice(['up', 'down', 'left', 'right'])
            is_dirty = self.percept()[1] == 'dirty'

            if is_dirty:
                self.execute_action('suck')

            self.execute_action(move)

        is_dirty = self.percept()[1] == 'dirty'

        if is_dirty:
            self.execute_action('suck')

    def print_squares(self):
        for row in self.matrix:
            print(' '.join(map(str, row)))