def load_image(imagefilepath):
	import scipy
	import scipy.ndimage.interpolation
	from PIL import Image
	import numpy

	import pdb

	im = Image.open(imagefilepath)
	array = scipy.misc.fromimage(im)

	rarray = array[:,:,0]
	garray = array[:,:,1]
	barray = array[:,:,2]
	return [rarray,garray,barray]

def save_image(red,green,blue):
	#rmatrix = numpy.matrix(rarray)
	#gmatrix= numpy.matrix(garray)
	#bmatrix = numpy.matrix(barray)

	array = numpy.array([rarray, garray, barray])
	scipy.misc.imsave('bunnyout2.png', array)
