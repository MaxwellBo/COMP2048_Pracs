# -*- coding: utf-8 -*-
"""
Ant script with animated evolution

Created on Tue Jan 15 12:37:52 2019

@author: shakes
"""
import ant

N = 128

# https://en.wikipedia.org/wiki/Langton%27s_ant#Extension_to_multiple_colors
# table = ant.ANT_TRANSITION_TABLE
# table = ant.SYMMETRIC_TRANSITION_TABLE
# table = ant.SQUARE_TRANSITION_TABLE
table = ant.FILLED_TRIANGLE_TABLE

#create the game of life object 
life = ant.Ant(N, transition_table=table)
# life.insertChaos(index=life.ant_location)

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

interval = 1 #ms

#animate 24 frames with interval between them calling animate function at each frame
ani = animation.FuncAnimation(fig, animate, frames=60, interval=interval, blit=True)

plt.show()