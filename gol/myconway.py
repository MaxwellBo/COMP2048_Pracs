import numpy as np
import scipy.ndimage as ndimage

def evolve(footprint):
    center = footprint[4]
    footprint[4] = 0 # zero the center out so it doesn't influence our neighbor sum

    # 1. Underpopulation: A live cell that has < 2 live neighbouring cells will die
    # 2. Survival: A live cell that has 2-3 live neighbouring cells will remain alive
    # 3. Overpopulation: A live cell with more than 3 live neighbours will die
    if center == 1:
        if sum(footprint) < 2:
            return 0
        elif 2 <= sum(footprint) <= 3:
            return 1
        elif 3 < sum(footprint):
            return 0
    else:
        # 4. Reproduction: A dead cell with exactly 3 live neighbours will become alive
        if sum(footprint) == 3:
            return 1
        return 0

x = np.array([[0,0,0],[1,1,1],[0,0,0]])

footprint = np.array([[1,1,1],
                      [1,1,1],
                      [1,1,1]])

results = x

results = ndimage.generic_filter(results, evolve, footprint=footprint, mode="constant", cval=0)
print(results)
results = ndimage.generic_filter(results, evolve, footprint=footprint, mode="constant", cval=0)
print(results)
results = ndimage.generic_filter(results, evolve, footprint=footprint, mode="constant", cval=0)
print(results)

