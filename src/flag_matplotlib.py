#!/usr/bin/env python

from matplotlib import patches, pyplot as plt
from math import sin, cos ,pi


fig = plt.figure(figsize=(6,4))
ax = fig.add_subplot(111)

def star(coord, size, rotate):
	pts = [(size * sin(i*4*pi/5+rotate) + coord[0], 
		size * cos(i*4*pi/5+rotate)+coord[1]) for i in range(5)]
	return patches.Polygon(pts,fc='yellow',ec='yellow')

ax.add_patch(patches.Rectangle([0,-2],3,2,fc='red',ec='red'))
ax.add_patch(star((0.5,-0.5),0.3,0.0))
ax.add_patch(star((1.0,-0.2),0.07,0.3))
ax.add_patch(star((1.2,-0.4),0.07,0.9))
ax.add_patch(star((1.2,-0.7),0.07,0.0))
ax.add_patch(star((1.0,-0.9),0.07,0.3))
ax.set_axis_off()
plt.axis('scaled')
plt.show()