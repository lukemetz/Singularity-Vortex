from loadImage import *
import numpy
import scipy
import pdb
def invert(imagefilepath):
	colors=load_image(imagefilepath)
	r=colors[0]
	g=colors[1]
	b=colors[2]
	r=numpy.matrix(r, dtype=int)
	g=numpy.matrix(g, dtype=int)
	b=numpy.matrix(b, dtype=int)
	r=255-r
	g=255-g
	b=255-b
	save_image(r,b,g)
invert('bunny.jpg')

	
