import scipy
import scipy.ndimage.interpolation
from PIL import Image
import numpy
import math

import pdb

im = Image.open("smallbunny.jpg")
array = scipy.misc.fromimage(im)

def applyTransformationMatrix(array, transform, newSize=None):
	'''
	applies a transformatrix matrix to an arrray. 
	params:
		array is in the form of [x,y,color]. right from fromImage function
		transformm: a 3x3 image. upper 2x2 box is rot and scale. left 2 column is transform. lower 3 should be 0,0,1
		newSize: New size of the image. defaulted to original
	'''

	maxSize = array.shape
	if newSize ==None:
		newSize = maxSize

	matrix = numpy.zeros([5,maxSize[0]*maxSize[1]])


	#convert to very long matrix of size 3x100000
	count = 0;
	for x in range(maxSize[0]):
		for y in range(maxSize[1]):
			matrix[0][count] = x
			matrix[1][count] = y
			for i in range(3):
				matrix[2+i][count] = array[x][y][i]
			count +=1

	#convert 
	mat2 = numpy.matrix(matrix)
	imageMat = numpy.zeros([maxSize[0],maxSize[1],3])


	from scipy.interpolate import griddata


	points = numpy.matrix(mat2[0:2].T)

	ones = numpy.zeros([ maxSize[1]*maxSize[0],1])+1
	points = numpy.hstack([points, ones])
	points = numpy.matrix(points).T


	points = transform*points

	values = mat2[2:5].T

	xi = numpy.zeros([newSize[0]*newSize[1],2])
	count = 0
	for x in range(newSize[0]):
		for y in range(newSize[1]):
			xi[count] = numpy.array([x,y])
			count+=1

	points = points[0:2]

	data = griddata(points.T, values, xi, method='linear', fill_value=0)#numpy.array([0,0,0]))


	imageMat = numpy.zeros([newSize[0], newSize[1],3])

	for p in range(len(xi)):
		imageMat[int(xi[p][0]),int(xi[p][1])] = data[p]

	array = numpy.array(imageMat)
	return array
	

maxSize = array.shape
offset = numpy.matrix([[1,0,-maxSize[0]/2],[0,1,-maxSize[1]/2],[0,0,1]])
theta = -numpy.pi/4

rot = numpy.matrix([[math.cos(theta), -math.sin(theta),0], [math.sin(theta), math.cos(theta),0], [0,0,1]])

unOffset = numpy.matrix([[1,0,maxSize[0]/2],[0,1,maxSize[1]/2],[0,0,1]])

array = applyTransformationMatrix(array, unOffset*rot*offset, numpy.array([200,200]))

scipy.misc.imsave('bunnyout2.png', array)


#print array
