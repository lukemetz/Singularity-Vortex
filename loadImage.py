import scipy
from PIL import Image

im = Image.open("bunny.jpg")
array = scipy.misc.fromimage(im)

array = array*1.5

scipy.misc.imsave('bunnyout.png', array)


print array
