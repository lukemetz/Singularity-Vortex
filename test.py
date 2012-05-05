import Vortex
import numpy
import math


orig= Vortex.load_image('bunny.jpg')
zerovec= numpy.zeros(orig[0].shape)
orig[2] = zerovec
orig[0] = zerovec
Vortex.save_image(orig, 'bunnygreen.png')

#orig = Vortex.load_image('edgeDetection.png')
#a = Vortex.sobelEdgeDetection(orig)
#Vortex.save_image(a, 'edgeOut.jpg')


#orig = Vortex.load_image('churchin.jpg')
#a = Vortex.sobelEdgeDetection(orig)
#Vortex.save_image(a, 'churchout.jpg')



orig = Vortex.load_image('churchin.jpg')
a = Vortex.gaussiangBlur(orig, sigma=2, kernelSize=15)
a = Vortex.sobelEdgeDetection(a)
Vortex.save_image(a, 'churchoutbluredge.jpg')
a = Vortex.gaussiangBlur(orig, sigma=4, kernelSize=15)
a = Vortex.sobelEdgeDetection(a)
Vortex.save_image(a, 'churchoutblur2edge.jpg')

#a = Vortex.sobelEdgeDetection(a)
#Vortex.save_image(a, 'churchoutbluredge.jpg')

<<<<<<< HEAD
'''
orig = Vortex.load_image('bunnycute.jpg')
=======
'''orig = Vortex.load_image('bunnycute.jpg')
>>>>>>> 664674ce306a9e322a5ded035aca9b2c1210cb9c
print orig
maxSize = orig[0].shape
offset = numpy.matrix([[1,0,-maxSize[0]/2],[0,1,-maxSize[1]/2],[0,0,1]])
theta = -numpy.pi/4

rot = numpy.matrix([[math.cos(theta), -math.sin(theta),0], [math.sin(theta), math.cos(theta),0], [0,0,1]])
#rot = 1
unOffset = numpy.matrix([[1,0,maxSize[0]/2],[0,1,maxSize[1]/2],[0,0,1]])

a = Vortex.apply_transformation_matrix(orig, unOffset*rot*offset)

<<<<<<< HEAD
Vortex.save_image(a, 'bunnycuteRot.jpg')
'''
=======
Vortex.save_image(a, 'bunnycuteRot.jpg')'''

>>>>>>> 664674ce306a9e322a5ded035aca9b2c1210cb9c
#a = Vortex.invert(a)
#a = Vortex.add_layers(orig,a)

#Vortex.changeHue(orig, 30)
