# Testing the Hopfield Network
# Import the class
import numpy as np
from Hopfield import Hopfield

def mat2vec(a):
	c = len(a[0,:])
	r = len(a[:,0])
	n = np.zeros(r*c)
	for i in range(c):
		for j in range(r):
			n[i*r+j] = a[i,j]
	return n

# Create the network ~~~~~~~
my_network = Hopfield()

# Process Data Here ~~~~~~~ Whatever you want
I = -1*np.ones([17,17])
L = I
L[:,0] = 1.0
L[16,:] = 1.0
I[0,:] = 1.0
I[16,:] = 1.0
I[:,8] = 1.0
H = I.transpose()

# Use the network!
# my_network.learn(Whatever you wanna learn! :)

Iprime = I
Iprime[1,1:10] = 1.0

I = mat2vec(I)
L = mat2vec(L)
H = mat2vec(H)
Iprime = mat2vec(Iprime)

my_network.train(I)
print('Done training I')
#my_network.train(H)
#print('Done Training H')
my_network.train(L)
print('Done Training L')

for i in range(1):
	Iprime = my_network.recover(Iprime, 1)
	print(Iprime.reshape((17,17)))