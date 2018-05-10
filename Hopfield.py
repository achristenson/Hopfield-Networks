# Code for a discrete Hopfield Network

# Importing the required functions for the network
import numpy as np    # Numpy package for vector math
import random 			 # Random package for asynchronous firing

# For now we can define the Hopfield network as its own class
class Hopfield:
	# Initialize the network with the required parameters
	def __init__(self):
		self.hasRun = False		# Create a matrix for storing the weights of neuron connections
		self.W = 0				# Initialize weight matrix
		self.E = 0				# Store the energy of the network
		self.theta = 0.5		# Create a bias, theta
		

	# Training function to add data to the weights
	# Can take single set of training data
	def train(self, x):
		self.update_Weights(x)		# Update the weight matrix
		self.update_Energy(x)		# Update network energy

	# Updates the weight matrix
	def update_Weights(self,x):
		w = np.zeros([len(x),len(x)]) 		# Initializes weights as 0
		# Iterates each of the elements in the future weight matrix, does computation and saves as dummy
		for j in range(len(x)):
			for i in range(j,len(x)):
				if i==j:
					w[i,j] = 0
				else:
					w[i,j] = x[i]*x[j]
					w[j,i] = w[i,j]

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
			xp = x.transpose()*self.W[:,i]					# Use a dummy to get the product
			x[i] = xp										# Modify the neuron and repeat
		x[x>=0] = 1
		x[x<0] = -1
		return x