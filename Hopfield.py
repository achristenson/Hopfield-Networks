# Code for a discrete Hopfield Network

# Importing the required functions for the network
import numpy as np    # Numpy package for vector math
import random 			 # Random package for asynchronous firing

# For now we can define the Hopfield network as its own class
class Hopfield:
	# Initialize the network with the required parameters
	def __init__(self):
		self.hasRun = False		# Create a matrix for storing the weights of neuron connections
		self.W = None			# Initialize weight matrix
		self.E = 0				# Store the energy of the network
		self.theta = 0.5		# Create a bias, theta
		

	# Training function to add data to the weights
	# Can take single set of training data
	def train(self, x):
		self.update_Weights(x)		# Update the weight matrix
		self.update_Energy(x)		# Update network energy

	# Updates the weight matrix
	def update_Weights(self,x):
		# Using vector math, compute the input specific weights - outer product between input vector and its transpose
		w = np.outer(x,x.T)
		w = w-np.identity(len(x)) 			# Force self weights to 0
		# Determines if the weight matrix has already been created, if not initialize, else add to existing weights
		if self.hasRun == False:
			self.hasRun = True
			self.W = w
		else:
			self.W = self.W + w


	# Calculate and update Hopfield Energy, only works with vector inputs
	def update_Energy(self,x):
		E = -1*x.transpose()*self.W@x/2
		self.E += E

	# Function which takes in an estimate and returns an approximation from memory
	def recover(self, x, iters):
		for n in range(iters):
			i = np.random.randint(len(self.W[0]),size=1)	# Choose a random neuron to fire off
			xp = np.dot(x.transpose(),self.W[:,i])			# Use a dummy to get the product
			if xp >= 0:
				x[i] = 1
			else:
				x[i] = -1
		return x