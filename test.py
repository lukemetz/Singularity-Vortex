import Vortex

a = Vortex.load_image('muffin.jpg')
a = Vortex.greyscale(a)
Vortex.save_image(a, 'muffinout.jpg')