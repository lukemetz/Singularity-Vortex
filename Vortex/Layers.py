import numpy
def add_layers(layer1, layer2):
	out = [None for x in layer1]
	for k in range(len(layer1)):
		out[k] = layer1[k]+layer2[k]
		numpy.clip(out[k],0,255)
	return out

def multiply_layers(layer1, layer2):
	out = [None for x in layer1]
	for k in range(len(layer1)):
		out[k] = (layer1[k]/255.0*layer2[k]/255.0)*255
		numpy.clip(out[k],0,255)
	return out
