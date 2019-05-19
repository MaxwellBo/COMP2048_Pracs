# -*- coding: utf-8 -*-
"""
Ant script with animated evolution

Created on Tue Jan 15 12:37:52 2019

@author: shakes
"""
import conway

N = 64

table = conway.STRANGE_TRANSITION_TABLE

#create the game of life object
life = conway.Ant(N, transition_table=table)
life.insertChaos(index=life.ant_location)

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
ani = animation.FuncAnimation(fig, animate, frames=1, interval=interval, blit=True)

plt.show()