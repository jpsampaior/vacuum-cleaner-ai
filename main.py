from environment import Environment

if __name__ == '__main__':
    env = Environment()
    print('Room before cleaning')
    env.print_squares()
    env.start_cleaning_random()
    print(' ')
    print('Room after cleaning')
    env.print_squares()
    print(' ')
    print('Agent performance: ' + str(env.agent.performance))