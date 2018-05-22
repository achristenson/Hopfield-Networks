# Testing the Hopfield Network
# Import the class
import numpy as np
from Hopfield import Hopfield

# Create the network ~~~~~~~
my_network = Hopfield()

# Process Data Here ~~~~~~~ Whatever you want
I = -1*np.ones([17,17])
L = -1*np.ones([17,17])
L[:,0] = 1.0
L[16,:] = 1.0
I[0,:] = 1.0
I[16,:] = 1.0
I[:,8] = 1.0
H = np.copy(I.transpose())

# Use the network!
# my_network.learn(Whatever you wanna learn! :)

Iprime = np.copy(I)
Iprime[1,1:10] = 1.0

I = I.flatten()
L = L.flatten()
H = H.flatten()
Iprime = Iprime.flatten()

my_network.train(I)
my_network.train(H)
#my_network.train(L)

for i in range(1):
	Iprime = my_network.recover(Iprime, 1000)
	print(Iprime.reshape((17,17)))