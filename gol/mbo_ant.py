import numpy as np

ANT_TRANSITION_TABLE = {
    0: (1, 'R'),
    1: (0, 'L')
}

SYMMETRIC_TRANSITION_TABLE = {
    0: (1, 'L'),
    1: (2, 'L'),
    2: (3, 'R'),
    3: (0, 'R')
}

SQUARE_TRANSITION_TABLE = {
    0: (1, 'L'),

    1: (2, 'R'),
    2: (3, 'R'),
    3: (4, 'R'),
    4: (5, 'R'),
    5: (6, 'R'),

    6: (7, 'L'),
    7: (8, 'L'),

    8: (0, 'R')
}

FILLED_TRIANGLE_TABLE = {
    0: (1, 'R'),
    1: (2, 'R'),

    2: (3, 'L'),
    3: (4, 'L'),
    4: (5, 'L'),

    5: (6, 'R'),

    6: (7, 'L'),
    7: (8, 'L'),
    8: (9, 'L'),

    9: (10, 'R'),
    10: (11, 'R'),
    11: (0, 'R'),
}

DIRECTION = 'NESW'

OFFSET_TABLE  = {
    'N': (0, 1),
    'S': (0, -1),
    'E': (1, 0),
    'W': (-1, 0)
}

class Ant:
    def __init__(self, N=256, ant_location=(48,48), transition_table=ANT_TRANSITION_TABLE):
        self.grid = np.zeros((N,N), np.uint)
        self.ant_location = ant_location
        self.ant_direction = DIRECTION[0]
        self.transition_table = transition_table
    
    def getStates(self):
        '''
        Returns the current states of the cells
        '''
        return self.grid
    
    def getGrid(self):
        '''
        Same as getStates()
        '''
        return self.getStates()
    
    def get_under_ant(self):
        return self.grid[self.ant_location]

    def set_under_ant(self, x):
        self.grid[self.ant_location] = x

    def turn(self, l_or_r):
        offset = +1 if l_or_r == 'R' else -1
        self.ant_direction = DIRECTION[(DIRECTION.find(self.ant_direction) + offset) % len(DIRECTION)]

    def move(self):
        offset = OFFSET_TABLE[self.ant_direction]

        self.ant_location = (
            self.ant_location[0] + offset[0], 
            self.ant_location[1] + offset[1]
        )


    def evolve(self):
        current_square = self.get_under_ant()

        transition = self.transition_table[current_square] 
        new_square, turn = transition

        self.set_under_ant(new_square)
        self.turn(l_or_r=turn)
        self.move()

    def insert_chaos(self, index=(0, 0)):
        self.grid[index[0], index[1]] = 1
        self.grid[index[0]+1, index[1]] = 1
        self.grid[index[0]+2, index[1]] = 1
        self.grid[index[0]+3, index[1]] = 1
        self.grid[index[0]+4, index[1]] = 1
        self.grid[index[0]+5, index[1]] = 1
        self.grid[index[0]+6, index[1]] = 1

###############################################################################

N = 96

n = int(input("Please select your ruleset: (0 - 3)"))

# https://en.wikipedia.org/wiki/Langton%27s_ant#Extension_to_multiple_colors
table = {
    0: ANT_TRANSITION_TABLE,
    1: SYMMETRIC_TRANSITION_TABLE,
    2: SQUARE_TRANSITION_TABLE,
    3: FILLED_TRIANGLE_TABLE
}[n]


#create the game of life object 
life = Ant(N, transition_table=table)
# life.insert_chaos(index=life.ant_location)

cells = life.getStates() #initial state

#-------------------------------
#plot cells
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()

plt.gray()

img = plt.imshow(cells, animated=True, cmap='gist_ncar', vmin=0, vmax=(len(table) - 1))

def animate(i):
    """perform animation step"""
    global life

    life.evolve()
    cellsUpdated = life.getStates()

    img.set_array(cellsUpdated)

    return img,

interval = 1 #ms - run it as fast as possible# table = ant.ANT_TRANSITION_TABLE

#animate 24 frames with interval between them calling animate function at each frame
ani = animation.FuncAnimation(fig, animate, interval=interval, blit=True)

plt.show()
