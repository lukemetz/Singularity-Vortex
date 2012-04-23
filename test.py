import Vortex

orig = Vortex.load_image('muffin.jpg')

a = Vortex.gaussiangBlur(orig, kernelSize=17, sigma=3)

a = Vortex.sobelEdgeDetection(a)
a = Vortex.invert(a)
a = Vortex.add_layers(orig,a)
Vortex.save_image(a, 'muffinout.jpg')