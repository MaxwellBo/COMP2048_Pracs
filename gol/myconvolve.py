import numpy as np
from scipy import signal

grid = np.array([
    [0,0,0],
    [1,1,1],
    [0,0,0]]
)


neighborhood = np.array([
    [1,1,1],
    [1,0,1],
    [1,1,1]]
)

neighbors = signal.convolve2d(
    grid, 
    neighborhood, 
    # The output is the same size as in1, centered with respect to the ‘full’ output.
    mode='same', 
    boundary='fill', 
    fillvalue=0
)

only_2_neighbors = np.equal(neighbors, 2)
only_3_neighbors = np.equal(neighbors, 3)

# if (center == self.aliveValue and alive == 2) or (alive == 3):
result = np.logical_or(np.logical_and(grid, only_2_neighbors), only_3_neighbors).astype(int)