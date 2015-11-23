

class Car:

	max_velocity = 5 #Class variable shared by all instances
	max_acceleration = 2
	range_of_sight = 3

	def __init__(self, startNode,road):
		self.startNode = startNode    # instance variable unique to each instance
		self.currentNode = startNode
		self.position = GetNode(startNode) #1x2 vector
		self.visitedNodes = [startNode] 
		self.velocity = max_velocity*random.random()
		self.acceleration = max_acceleration*random.random()
		self.nextNode = GetNextNode(startNode) #1x2 vector
		self.direction = get_direction(visitedNodes[-1])
		self.road = road

	def update(self,cars,nodes,delta_t):

		acceleration = 0

		if self.velocity < max_velocity:
			acceleration = self.acceleration

		for car in cars: #Loop over all cars, but should exclude the self

			if getDistance(self.position,car.position) <= range_of_sight:
				print "I can see another car"
				acceleration = -self.acceleration

		self.velocity = self.velocity + acceleration*delta_t

		if getDistance(self.position,GetNode(self.nextNode)) < self.velocity*delta_t: #We arrive at the next node
			self.currentNode = self.nextNode
			self.visitedNodes.append(self.currentNode)
			self.nextNode = GetNextNode(currentNode)
			self.direction = get_direction(visitedNodes[-1])
			self.position = GetNode(self.currentNode)

		else:
			distanceTraversed = [x *self.velocity*delta_t for x in self.position ]
			self.position = self.position + distanceTraversed

			#Adjust the acceleration & velocity accordingly
			#Also check that the car doesn't react to itself as another car

	def getDistance(pos1,pos2):
		return sqrt(pow((po1[0]-pos2[0]),2)+pow((pos1[1]-pos2[1]),2))


		
#Methods used but not implemented:
	#get_direction(currentNode) returns current direction
	#GetNode(currentNode) returns current position based on starting (current) node
	#Neighbourhood are other vehicle objects in view of this car
	#GetNextNode returns the node we're heading towards
	#GetNode(node) returns the (x,y) position of node

