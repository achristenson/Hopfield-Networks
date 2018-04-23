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