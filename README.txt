EE 127: Information Theory - Final Project
The Capacity of Hopfield Neural Networks
By: Alexander Christenson, Holden Fried, Kenny Yau

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Brief Primer on Hopfield Networks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In 1982 J.J. Hopfield wrote his seminal paper "Neural networks and 
physical systems with emergent collective computational abilities."
This paper was considered highly important at the time of publication.
It helped spur an increase in artificial intelligence research and has
recieved nearly 20,000 citations since publication.

His original paper draws comparisons between the computational
properties of biological organisms and the construction of computers.
These come primarily by comparing the function of a neuron in a brain
with the function of a transistor in a computer, and the paper
presents a mathematical model primarily based on neurobiology, but
with the potential to be easily applied to integrated circuits.

The main goal of the system is to provide content-addressable memory
described by an appropriate phase space flow of the state of the
system. A content-addressable memory simply means that given incomplete
information about an item, a memory item can be found assuming that the
incomplete information is sufficient. For the system to be work it
needs to be able to deal with errors, and retrieve the desired memory
item from a small section of the input.

At the time hardware based content addressable memory systems were
relatively simple due to the difficulty in integrating error checking
leading to a majority of the error checking being done in software.

The error correction is done through mapping the time evolution of the
system to a set of coordinates to represent the instantaneous
condition of the system (this applies to both continuous and discrete).
From this mapping equations of motion of the system describe the flow
of the state space.

The processing for the system is done in a distributed manner. The
neurons are what the processing devices or nodes of the network are
referred to in the paper.

Each neuron i has a binary 0 or 1 state V_i corresponding to if the
neuron is either not firing (off) or firing at maximum strength (on).
What we will do in our implementation of the paper for the purpose of
analyzing the network capacity is maintain the quantization without
rounding. The strength of the connections between the neurons is
defined by the weights T_{ij} (for no connection T_{ij} = 0).

The state of the neuron is determined by an algorithm, as follows:

Each neuron i is assigned a fixed threshold U_i. Each neuron i
readjusts its state randomly in time but with a mean attempt rate W
setting,

V_i = 1 if sum(T_{ij}V_j) over all j != i > U_i
V_i = 0 if sum(T_{ij}V_j) over all j != i < U_i

This algorithm makes each neuron randomly and asynchronously fire
independent of what its state is relative to the threshold.

This algorithm differs from the previously used ones because it
enables the response of one neuron to affect itself indirectly, as
referred to in the paper as the backcoupling of the system. Modeled
as A <-> B <-> C <-> A for a network of neurons A, B, C.

The information in the system is stored in the weight matrix
defining the connections between the neurons. If we want to remember
a set of states V^s, s = 1...n, the connections between the neurons
are defined as:

T_{ij} = sum((2*V^s_i-1)(2*V^s_j-1)) over all states s
T_{ii} = 0

From the definition

sum(T_{ij}V^{s'}_j) over all j
= sum((2*V^s_i-1)[sum(V^{s'}_j(2V^s_j-1)) over all j]) over all s
is defined as H^{s'}_j

In this situation the mean of the summation in the square brackets
is zero for s != s', and otherwise is N/2.

From this:

sum(T_{ij}V^{s'}_j) over all j
= <H^{s'}_i>
appx equals (2V^{s'}_i - 1)N/2

This model contrasts with the previously used models in the sense
that it uses its strong nonlinearity to make choices, produce
categories, and regenerate information. This means that where
previous models would produce nonsensical outputs when the
stimulus on the network is a linear combination of two stimuli with
known outputs that is a combination of the two outputs, this model
chooses the more probable output.

The biological representation of firing between neurons has previously
been linearized in the network, however, now a step function about a
threshold is now used.

The network of cells described in the original paper have the ability
to perform abstract calculations, and the inputs should be
appropriately encoded, meaning that the data needs to be pre processed
before the hopfield memory network can be used to store its 
information.

The way the associative memory works is through making an energy
approximation through the network to be able to map the closest stimula
with a corresponding and probably correct output. The energy function
is defined as:

E = - sum(sum(T_{ij}V_iV_j))/2 over all j, all != j

The change in energy due to the changing neuron states is:

D(E) = - D(V_i) sum(T_{ij}V_j) over all j != i'

The algorithm for changing the state of the neuron forces the energy
function to be monotonically decreasing, and state changes will
continue until the energy function reaches a local stable minimum.
It is possible for the system to have many locally stable states.

This algorithm does not always converge to the correct stable
equilibria. The space flow can be affected by nominally assigned
memories implying that the network can create artificial associated
combinations of the memory that form stable equilibria in the phase
flow of the system. The system responds to an ambiguous stimulation
by making a statistical choice between memory states.

