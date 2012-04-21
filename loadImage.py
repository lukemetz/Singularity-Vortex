import scipy
import scipy.ndimage.interpolation
from PIL import Image
import numpy

import pdb

im = Image.open("bunny.jpg")
array = scipy.misc.fromimage(im)

rarray = array[:,:,0]
garray = array[:,:,1]
barray = array[:,:,2]


#rmatrix = numpy.matrix(rarray)
#gmatrix= numpy.matrix(garray)
#bmatrix = numpy.matrix(barray)

array = numpy.array([rarray, garray, barray])

#print identity
#pdb.set_trace()


scipy.misc.imsave('bunnyout2.png', array)


#print array
