import scipy
import scipy.ndimage.interpolation
from PIL import Image
import numpy

import pdb

im = Image.open("smallbunny.jpg")
array = scipy.misc.fromimage(im)


def makeBackDiagonal(z):
	#z = max(array.shape)
	identity = numpy.zeros([z,z])
	for k in range(z):
		identity[k][z-1-k] = 1
	return identity

identity = makeBackDiagonal(max(array.shape))

#scipy.ndimage.interpolation.rotate(identity, 30)

#identity = identity[:array.shape[1],0:array.shape[0]]

maxSize = array.shape
matrix = numpy.zeros([5,maxSize[0]*maxSize[1]])
print matrix
count = 0;
for x in range(maxSize[0]):
	for y in range(maxSize[1]):
		matrix[0][count] = x
		matrix[1][count] = y
		for i in range(3):
			#try:
			matrix[2+i][count] = array[x][y][i]
			#except:	
				#matrix[count][2+i] = 0
		count +=1
		#print count

print matrix
print "premulti"
print matrix.shape
#print numpy.matrix([[0,1],[-1,0],[1,0],[1,0],[1,0]]).shape
rotMat = numpy.matrix(numpy.zeros([5,5]))
rotMat[0,1] = -1
rotMat[1,0] = 1
rotMat[2,2] = 1
rotMat[3,3] = 1
rotMat[4,4] = 1
matrix = numpy.matrix(matrix)
#matrix = numpy.zeros([5,7])
#mat2 = rotMat*matrix
mat2 = matrix

print mat2.shape
print rotMat

imageMat = numpy.zeros([maxSize[0],maxSize[1],3])


from scipy.interpolate import griddata

points = mat2[0:2].T
values = mat2[2:5].T
print points.shape
print values
xi = numpy.zeros([maxSize[0]*maxSize[1],2])
count = 0
for x in range(maxSize[0]):
	for y in range(maxSize[1]):
		xi[count] = numpy.array([x,y])
		count+=1

#xi = numpy.meshgrid(numpy.arange(maxSize[0]), numpy.arange(maxSize[1]))
print xi.shape
data = griddata(points, values, xi, method='linear', fill_value=0)#numpy.array([0,0,0]))


#pdb.set_trace()
#for x in range(maxSize[0]):
#	for y in range(maxSize[1]):
#		print x, y
#		closest = mat2[0] # [x,y,r,g,b]
#
#		for i in range(maxSize[0]*maxSize[1]):
			#diff = (closest-mat[i])
			#diff
#			if int(mat2[0,i]) == x and int(mat2[1,i])==y:
#				
#				imageMat[x,y,0] = mat2[2,i]
#				imageMat[x,y,2] = mat2[4,i]




#identity[1][50:100] = 1
#identity[50:100][50:100] = 1

#rarray = array[:,:,0]
#garray = array[:,:,1]
#barray = array[:,:,2]

#rmatrix = numpy.matrix(rarray)
#gmatrix= numpy.matrix(garray)
#bmatrix = numpy.matrix(barray)

#gmatrix = gmatrix*identity
#bmatrix = bmatrix*identity

array = numpy.array([imageMat])

#print identity
#pdb.set_trace()


#scipy.misc.imsave('bunnyout2.png', array)


#print array
