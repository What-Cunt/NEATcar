# NEATcar
'''
Goal of this project is to develop a NEAT algorithm for cars that will drive around
a racetrack. They will be able to fall off and die, and we will reward/keep those that survive
the longest, and those who go the furthest along the track. We would need to weight the values of those
concepts accordingly. We will track whether or not something is off the track by taking a screenshot about every 0.1 seconds
to see whether the car is on a color that is not on the track. If there is another color underneath the car of the
screenshot, we can kill off the car. We will keep track of how long each car stays alive using a timer, and marking it
in a dictionary. We will keep track of how far each car goes by keeping track of the amount of nodes the car hits.
We will create nodes (points) on the track where the more nodes the car touches, the better.
'''
