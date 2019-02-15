#!/bin/python
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import wget
import os
import mat4py as matL
import time
from PIL import Image

start = time.time()
datos=np.random.random_integers(199, size=(1,6))
datos=datos[0]

url='http://www.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/BSR/BSR_bsds500.tgz'
file = wget.download(url)

os.system('tar -x -f BSR_bsds500.tgz')

files=os.listdir('./BSR/BSDS500/data/images/test/')

cont = 0
f, axarr = plt.subplots (2,6)
os.system('mkdir dataNew')
for dato in datos :
	file=files[dato]
	name = './BSR/BSDS500/data/images/test/' + file
	anot = './BSR/BSDS500/data/groundTruth/test/'+file[:-3]+'mat'
	im = Image.open(name)
	w, h = im.size
	im.thumbnail((256, 256), Image.ANTIALIAS)
	axarr[0,cont].imshow(im)
	cont = cont + 1
	truth = matL.loadmat(anot)
	truth = np.array(truth)
	#truth = Image.fromarray(truth, 'RGB')
	#print(type(truth))
	# No logré convertir las anotaciones para imprimirlas como imagen, ni guardarlas  :(
	#axarr[1,cont].imshow(truth)
	saveRoute ='./dataNew/'+file
	im.save(saveRoute)
plt.show()
os.system('rm -rf ./BSR')
end = time.time()
print (end - start)
