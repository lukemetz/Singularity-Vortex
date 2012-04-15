import scipy
import scipy.ndimage.interpolation
from PIL import Image
import numpy

import pdb

im = Image.open("bunny.jpg")
array = scipy.misc.fromimage(im)

identity = numpy.zeros([max(array.shape),max(array.shape)])
z = max(array.shape)-1
for k in range(max(array.shape)):
	identity[k][z-k] = 1

#scipy.ndimage.interpolation.rotate(identity, 30)
print identity
#identity = identity[:array.shape[1],0:array.shape[0]]




rarray = array[:,:,0]
garray = array[:,:,1]
barray = array[:,:,2]

rmatrix = numpy.matrix(rarray)
gmatrix= numpy.matrix(garray)
bmatrix = numpy.matrix(barray)

gmatrix = gmatrix*identity
bmatrix = bmatrix*identity

array = numpy.array([rmatrix,gmatrix,bmatrix])

#print identity
#pdb.set_trace()


scipy.misc.imsave('bunnyout.png', array)


#print array
