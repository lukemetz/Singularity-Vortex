from loadImage import*
import scipy
import scipy.ndimage.interpolation
from PIL import Image
import numpy
import pdb

def flip_Image(imageFilepath, d):

	bunny= load_image(imageFilepath)

	red = bunny[0]
	green = bunny[1]
	blue = bunny[2]
	
	rM= numpy.matrix(red)
	gM= numpy.matrix(green)
	bM= numpy.matrix(blue)

	
	iM= numpy.zeros([red.shape[0], red.shape[1]])
	iM= numpy.matrix(iM)
	
	print iM
	for i in range (red.shape[0]):
		iM[i,(red.shape[1]-1-i)]= 1	
	
	bout=0
	if d == 1:
		#Filps Vertically
		bout= numpy.array([iM*rM, iM*gM, iM*bM])
	if d == 2:
		#Flips Horizontally
		bout= numpy.array([rM*iM, gM*iM, bM*iM])
	return bout

array= flip_Image("bunny.jpg",2)
save_image(array[0], array[1], array[2])
