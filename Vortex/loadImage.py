import scipy
import scipy.ndimage.interpolation
from PIL import Image
import numpy

import pdb
def load_image(imagefilepath):

	im = Image.open(imagefilepath)
	array = scipy.misc.fromimage(im)

	rarray = array[:,:,0]
	garray = array[:,:,1]
	barray = array[:,:,2]
	return [rarray,garray,barray]

def save_image(array, filename):

	#rmatrix = numpy.matrix(rarray)
	#gmatrix= numpy.matrix(garray)
	#bmatrix = numpy.matrix(barray)

	scipy.misc.imsave(filename, array)
