from loadImage import *
import numpy
import scipy
import pdb
def greyscale(imagefilepath):
	colors=load_image(imagefilepath)
	r=colors[0]
	g=colors[1]
	b=colors[2]
	r=numpy.matrix(r, dtype=int)
	g=numpy.matrix(g, dtype=int)
	b=numpy.matrix(b, dtype=int)
	grey=(r+g+b)/3
	save_image(grey,grey,grey)
	
	

