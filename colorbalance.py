from loadImage import *
import numpy
import scipy
import pdb
def color_balance(imagefilepath,channel,num):
	colors=load_image(imagefilepath)
	r=colors[0]
	g=colors[1]
	b=colors[2]
	r=numpy.matrix(r, dtype=int)
	g=numpy.matrix(g, dtype=int)
	b=numpy.matrix(b, dtype=int)
	if channel=='red':
		r=r+num
	if channel=='green':
		g=g+num
	if channel=='blue':
		b=b+num
	if channel=='all':
		r=r+num
		b=b+num
		g=g+num
	r = numpy.clip(r,0,255)
	g = numpy.clip(g,0,255)
	b = numpy.clip(b,0,255)
	save_image(r,b,g)
color_balance('bunny.jpg',"red",100)
