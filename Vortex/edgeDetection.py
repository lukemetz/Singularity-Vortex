from loadImage import *
import numpy
import scipy
#import scipy.stsci.convolve
from scipy.signal import sepfir2d, convolve, convolve2d
##First dirivative
'''
a= load_image('bunny.jpg')
[r,g,b] = a

summ = None

for c in a:
	r = numpy.matrix(c, dtype=int)
	l = numpy.gradient(r)
	diff = numpy.matrix(l[0]+l[1])/2
	if summ == None:
		summ = diff
	else:
		summ += diff
summ = summ/3

edge= numpy.abs(summ)*10
print edge

save_image(edge, edge, edge)
'''
#Second dir
'''
a= load_image('muffin.jpg')
[r,g,b] = a

summ = None

for c in a:
	r = numpy.matrix(c, dtype=int)
	l = numpy.gradient(r)
	diff = numpy.matrix(l[0]+l[1])/2

	l = numpy.gradient(diff)i
	diff = numpy.matrix(l[0]+l[1], dtype=numpy.float)/2
	if summ == None:
		summ = diff
	else:
		summ += diff

summ = summ/3

edge= -summ*10 #numpy.abs(summ)
print edge
edge = numpy.clip(edge, 0, 255)
save_image(edge, edge, edge)
'''

def gaussiangBlur(array, kernelSize=5, sigma=0.84089642):

	n = kernelSize
	kernelBlur = numpy.zeros([n,n])
	for xx in range(0,n):
		for yy in range(0,n):
			x = xx-n/2
			y = yy-n/2
			kernelBlur[xx,yy] = 1/(numpy.pi*2*sigma)*numpy.exp(-(x**2+y**2)/(2*sigma**2))
	out = []
	#kernelBlur = numpy.array([[1,2,1],[0,0,0],[-1,-2,-1]])
	#print kernelBlur
	for c in array:
		y = convolve(c,kernelBlur, 'same')
		out.append(y)
	return out

def sobelEdgeDetection(array):


	kernelx = numpy.array([[-1,0,1],[-2,0,2],[-1,0,1]])
	kernely = numpy.array([[1,2,1],[0,0,0],[-1,-2,-1]])
	#print kernely
	out = []
	for c in array:
		y = convolve(c,kernely,'same')#, mode='same')
		x = convolve(c,kernelx,'same')#, mode='same')

		arc = numpy.sqrt(x**2+y**2)
		
		numpy.clip(arc,0,255)
		out.append(arc)

	edge = (out[0]+out[1]+out[2])/3
	return [edge, edge, edge]