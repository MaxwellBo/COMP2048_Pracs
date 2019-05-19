# -*- coding: utf-8 -*-
"""
The Game of Life (GoL) module named in honour of John Conway

This module defines the classes required for the GoL simulation.

Created on Tue Jan 15 12:21:17 2019

@author: shakes
"""
import numpy as np
from scipy import signal, ndimage
np.set_printoptions(threshold=99999)



BINARY_TRANSITION_TABLE = {
    0: (1, 'L'),
    1: (0, 'R')
}

DIRECTION = 'NESW'

OFFSET_TABLE = offset = {
    'N': (0, 1),
    'S': (0, -1),
    'E': (1, 0),
    'W': (-1, 0)
}

class Ant:
    def __init__(self, N=256, ant_location=(32,32), transition_table=BINARY_TRANSITION_TABLE):
        self.grid = np.zeros((N,N), np.uint)
        self.ant_location = ant_location
        self.ant_direction = DIRECTION[0]
        self.transition_table = transition_table
        
        self.set_under_ant(1)
    
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

    def insertChaos(self, index=(0, 0)):
        self.grid[index[0], index[1]] = 1
        self.grid[index[0]+1, index[1]] = 1
        self.grid[index[0]+2, index[1]] = 1

class GameOfLife:
    '''
    Object for computing Conway's Game of Life (GoL) cellular machine/automata
    '''
    def __init__(self, N=256, finite=False, fastMode=True):
        self.grid = np.zeros((N,N), np.uint)
        self.neighborhood = np.ones((3,3), np.uint) # 8 connected kernel
        self.neighborhood[1,1] = 0 #do not count centre pixel
        self.finite = finite
        self.fastMode = fastMode
        self.aliveValue = 1
        self.deadValue = 0
        
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

    def evolve(self):
        '''
        Given the current states of the cells, apply the GoL rules:
        - Any live cell with fewer than two live neighbors dies, as if by underpopulation.
        - Any live cell with two or three live neighbors lives on to the next generation.
        - Any live cell with more than three live neighbors dies, as if by overpopulation.
        - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction
        '''

        if self.fastMode: 
            neighbors = signal.convolve2d(
                self.grid, 
                self.neighborhood, 
                # The output is the same size as in1, centered with respect to the ‘full’ output.
                mode='same', 
                boundary='fill', 
                fillvalue=0
            )

            only_2_neighbors = np.equal(neighbors, 2)
            only_3_neighbors = np.equal(neighbors, 3)

            # if (center == self.aliveValue and alive == 2) or (alive == 3):
            self.grid = np.logical_or(np.logical_and(self.grid, only_2_neighbors), only_3_neighbors).astype(int)
        else:
            def evolve_cell(footprint):
                center = footprint[4]
                footprint[4] = 0 # zero the center out so it doesn't influence our neighbor sum
                alive = np.sum(footprint)

                # 1. Underpopulation: A live cell that has < 2 live neighbouring cells will die
                # 2. Survival: A live cell that has 2-3 live neighbouring cells will remain alive
                # 3. Overpopulation: A live cell with more than 3 live neighbours will die
                # 4. Reproduction: A dead cell with exactly 3 live neighbours will become alive
                # is equivalent to
                if (center == self.aliveValue and alive == 2) or (alive == 3):
                    return 1
                
                return 0

            self.grid = ndimage.generic_filter(
                input=self.grid, 
                function=evolve_cell, 
                footprint=np.array([[1,1,1],
                                    [1,1,1],
                                    [1,1,1]]), 
                # The mode parameter determines how the array borders are handled, 
                mode="constant", 
                # where cval is the value when mode is equal to 'constant'.
                cval=self.deadValue
            )

               
    def insertBlinker(self, index=(0,0)):
        '''
        Insert a blinker oscillator construct at the index position
        '''
        self.grid[index[0], index[1]+1] = self.aliveValue
        self.grid[index[0]+1, index[1]+1] = self.aliveValue
        self.grid[index[0]+2, index[1]+1] = self.aliveValue
        
    def insertGlider(self, index=(0,0)):
        '''
        Insert a glider construct at the index position
        '''
        self.grid[index[0], index[1]+1] = self.aliveValue
        self.grid[index[0]+1, index[1]+2] = self.aliveValue
        self.grid[index[0]+2, index[1]] = self.aliveValue
        self.grid[index[0]+2, index[1]+1] = self.aliveValue
        self.grid[index[0]+2, index[1]+2] = self.aliveValue
        
    def insertGliderGun(self, index=(0,0)):
        '''
        Insert a glider construct at the index position
        '''
        self.grid[index[0]+1, index[1]+26] = self.aliveValue
        
        self.grid[index[0]+2, index[1]+24] = self.aliveValue
        self.grid[index[0]+2, index[1]+26] = self.aliveValue
        
        self.grid[index[0]+3, index[1]+14] = self.aliveValue
        self.grid[index[0]+3, index[1]+15] = self.aliveValue
        self.grid[index[0]+3, index[1]+22] = self.aliveValue
        self.grid[index[0]+3, index[1]+23] = self.aliveValue
        self.grid[index[0]+3, index[1]+36] = self.aliveValue
        self.grid[index[0]+3, index[1]+37] = self.aliveValue
        
        self.grid[index[0]+4, index[1]+13] = self.aliveValue
        self.grid[index[0]+4, index[1]+17] = self.aliveValue
        self.grid[index[0]+4, index[1]+22] = self.aliveValue
        self.grid[index[0]+4, index[1]+23] = self.aliveValue
        self.grid[index[0]+4, index[1]+36] = self.aliveValue
        self.grid[index[0]+4, index[1]+37] = self.aliveValue
        
        self.grid[index[0]+5, index[1]+1 + 1] = self.aliveValue
        self.grid[index[0]+5, index[1]+2 + 1] = self.aliveValue
        self.grid[index[0]+5, index[1]+12] = self.aliveValue
        self.grid[index[0]+5, index[1]+18] = self.aliveValue
        self.grid[index[0]+5, index[1]+22] = self.aliveValue
        self.grid[index[0]+5, index[1]+23] = self.aliveValue
        
        self.grid[index[0]+6, index[1]+1 + 1] = self.aliveValue
        self.grid[index[0]+6, index[1]+2 + 1] = self.aliveValue
        self.grid[index[0]+6, index[1]+12] = self.aliveValue
        self.grid[index[0]+6, index[1]+16] = self.aliveValue
        self.grid[index[0]+6, index[1]+18] = self.aliveValue
        self.grid[index[0]+6, index[1]+19] = self.aliveValue
        self.grid[index[0]+6, index[1]+24] = self.aliveValue
        self.grid[index[0]+6, index[1]+26] = self.aliveValue
        
        self.grid[index[0]+7, index[1]+12] = self.aliveValue
        self.grid[index[0]+7, index[1]+18] = self.aliveValue
        self.grid[index[0]+7, index[1]+26] = self.aliveValue
        
        self.grid[index[0]+8, index[1]+13] = self.aliveValue
        self.grid[index[0]+8, index[1]+17] = self.aliveValue
        
        self.grid[index[0]+9, index[1]+14] = self.aliveValue
        self.grid[index[0]+9, index[1]+15] = self.aliveValue

    def insertFromFile(self, filename, index=((0,0))):
        with open(filename, 'r') as f:
            data = f.read()
            lines = data.split('\n')
            non_comment_lines = [ i for i in lines if not i.startswith("!") ]

            for (x, line) in enumerate(non_comment_lines):
                for (y, cell) in enumerate(line):
                    self.grid[index[0] + x, index[1] + y] = self.aliveValue if cell == 'O' else self.deadValue
