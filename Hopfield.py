# Code for a discrete Hopfield Network

# Importing the required functions for the network
import numpy as numpy    # Numpy package for vector math
import random 			 # Random package for asynchronous firing

# For now we can define the Hopfield network as its own class
class Hopfield:
	# Initialize the network with the required parameters
	def __init__(self):
		# Create a matrix for storing the weights of neuron connections
		self.W = np.matrix()

		# Create a vector for neuron states
		self.V = np.array()

		# Store the energy of the network
		self.E = 0

	# Training function to add data to the weights
	# Can take single set of training data as vector or multiple sets as matrix
	def train(self, x):
		temp_W = x.dot(x.transpose())	# Gets weights via matrix math from data input
		np.fill_diagonal(temp_W,0)		# Removes self weights from calculation
		self.update_Energy(x)			# Update network energy
		self.W = self.W + temp_W		# Updates the hopfield networks weight matrix

	# Calculate and update Hopfield Energy, only works with vector inputs
	def update_Energy(self,x):
		E = -1*np.dot(x.transpose(),np.dot(W,x))/2
		self.E += E

	# Function which takes in an estimate and returns an approximation from memory
	def recover(self, x, iters):
		for n in range(iters):
			i = random.randint(len(x))			# Choose a random neuron to fire off
			xp = x.transpose.dot(self.W[:,i])	# Use a dummy to get the product
			x[i] = xp.sign()					# Modify the neuron and repeat
		return x