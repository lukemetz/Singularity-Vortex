import Vortex as v
import scipy.linalg
import numpy
def SVD_compress(matrixlist,k):
	#r=matrixlist[0]
	#r=[[.5,.001],[.01,.1],[.7,.3],[.1,.03]]
	r=matrixlist[0]/255.0
	g=matrixlist[1]/255.0
	b=matrixlist[2]/255.0
	
	import random
	noise = numpy.zeros(r.shape)
	print noise.shape
	for x in range(r.shape[0]):
		for y in range(r.shape[1]):
			noise[x,y] = random.random()*.039

	print noise
	r+= noise;
	b+= noise
	g+= noise;
	#asdfasdf
	def svd_for_one(r):
		r=numpy.matrix(r)
		rt=numpy.matrix(r.T)
		RT=r*rt
		R=rt*r
		print RT
		print R
		print numpy.linalg.det(RT)
		[rvals1,rvects1]=scipy.linalg.eig(R)#At A
		[rvals2,rvects2]=scipy.linalg.eig(RT) #A At

		idx = rvals1.argsort()  
		idx=idx[::-1] 
		rvals1 = rvals1[idx]
		rvects1 = rvects1[:,idx]

		idx = rvals2.argsort() 
		idx=idx[::-1]  
		rvals2 = rvals2[idx]
		rvects2 = rvects2[:,idx]

		temp=numpy.sqrt(rvals1)
		Sig=numpy.diag(temp)
		worked=False
		while not(worked==True):
			try:
				Sig=Sig.reshape(r.shape)
				worked=True
			except:
				#print Sig
				Sig=numpy.append(Sig,0)
		Sig=numpy.matrix(Sig)
		Vt=rvects1.T
		U=rvects2
		Vt=numpy.matrix(Vt)
		U=numpy.matrix(U)

		svd=numpy.zeros(r.shape)
		svd=numpy.matrix(svd)

		i=0
		while i<k and i<Sig.shape[1]:
			#svd=svd+Sig[i,i]*U[i,:]*Vt[:,i]
			svd=svd+Sig[i,i]*U[:,i]*Vt[i,:]
			i=i+1
		print svd.shape
		return svd
   
	r=svd_for_one(r)
	g=svd_for_one(g)
	b=svd_for_one(b)
	r=numpy.real(r)*255
	g=numpy.real(g)*255
	b=numpy.real(b)*255
	r=numpy.clip(r,0,255)
	g=numpy.clip(g,0,255)
	b=numpy.clip(b,0,255)
	print r
		
	return [b,b,b]

matrixlist=v.load_image("smallbunny.jpg")
array=SVD_compress(matrixlist,2)
scipy.misc.imsave('bunnyout2.png', array)
	

