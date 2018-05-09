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
I = -1*np.ones([21,21])
I[0,:] = 1
I[20,:] = 1
I[:,10] = 1
H = I.transpose()

# Use the network!
# my_network.learn(Whatever you wanna learn! :)

Iprime = I
Iprime[1,1:10] = 1

I = mat2vec(I)
H = mat2vec(H)
Iprime = mat2vec(Iprime)

my_network.train(I)
print('Done training I')
my_network.train(H)
# my_network.train(L)
print('Done Training')
print(my_network.recover(Iprime, 100).reshape((21,21)))