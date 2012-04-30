import Vortex

#orig = Vortex.load_image('edgeDetection.png')
#a = Vortex.sobelEdgeDetection(orig)
#Vortex.save_image(a, 'edgeOut.jpg')


#orig = Vortex.load_image('churchin.jpg')
#a = Vortex.sobelEdgeDetection(orig)
#Vortex.save_image(a, 'churchout.jpg')



orig = Vortex.load_image('churchin.jpg')
#a = Vortex.(orig)
a = Vortex.gaussiangBlur(orig, sigma=3, kernelSize=15)
Vortex.save_image(a, 'churchoutblur.jpg')
a = Vortex.sobelEdgeDetection(a)
Vortex.save_image(a, 'churchoutbluredge.jpg')

#a = Vortex.invert(a)
#a = Vortex.add_layers(orig,a)

#Vortex.changeHue(orig, 30)
