import Vortex
import numpy
import math
'''

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
'''

#a = Vortex.sobelEdgeDetection(a)
#Vortex.save_image(a, 'churchoutbluredge.jpg')
'''
orig = Vortex.load_image('bunnycute.jpg')

print orig
maxSize = orig[0].shape
offset = numpy.matrix([[1,0,-maxSize[0]/2],[0,1,-maxSize[1]/2],[0,0,1]])
theta = -numpy.pi/4
#rot = numpy.matrix([[1,0,0], [.4,1,0], [0,0,1]])
rot = numpy.matrix([[math.cos(theta), -math.sin(theta),0], [math.sin(theta), math.cos(theta),0], [0,0,1]])
#rot = 1
unOffset = numpy.matrix([[1,0,maxSize[0]/2],[0,1,maxSize[1]/2],[0,0,1]])

a = Vortex.apply_transformation_matrix(orig, unOffset*rot*offset)

Vortex.save_image(a, 'bunnycuteRot.jpg')
'''
'''
a = Vortex.load_image('parrot.jpg')
a = Vortex.color_balance(a,'red',90)
a = Vortex.color_balance(a,'blue',-90)
a = Vortex.color_balance(a,'green',-90)

Vortex.save_image(a, 'parrotout1.jpg')

a = Vortex.load_image('parrot.jpg')
a = Vortex.color_balance(a,'all',-100)

Vortex.save_image(a, 'parrotout2.jpg')

'''


orig = Vortex.load_image('churchin.jpg')
a = Vortex.laplaceEdgeDetection(orig)
Vortex.save_image(a, 'churchoutlaplace.jpg')

#a = Vortex.invert(a)
#a = Vortex.add_layers(orig,a)

#Vortex.changeHue(orig, 30)
