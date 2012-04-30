def rgbToHvs(r,g,b):
	r = float(r)/255.0
	g = float(g)/255.0
	b = float(b)/255.0
	zmin = min( min(r, g), b );
	zmax = max( max(r, g), b );
	v = zmax;

	delta = zmax - zmin;

	if( zmax != 0 ):
		s = delta / zmax;
	else:
		#// r = g = b = 0		// s = 0, v is undefined
		s = 0;
		h = -1;
		return (h,s,v);

	if( r == zmax ):
		h = ( g - b ) / delta;		#// between yellow & magenta
	elif( g == max ):
		h = 2 + ( b - r ) / delta;	#// between cyan & yellow
	else:
		h = 4 + ( r - g ) / delta;	#// between magenta & cyan

	h *= 60;				#// degrees
	if( h < 0 ):
		h += 360;

	return (h,s,v)

#print rgbToHvs(215,100,120);

def changeHue(array, shift):

	for x in range(array[0].shape[0]):
		for y in range(array[0].shape[0]):
			#print array[0][x][y]
			pass
