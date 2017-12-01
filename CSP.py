import random


class CSPSolver:
	def __init__(self,noOfVertices,noOfColours):
		self.m = noOfColours
		self.size = noOfVertices
		self.colourArray = [-1 for i in range(self.size)]     #stores colour assignments
		self.graph=[[0 for i in range(self.size)] for j in range(self.size)]      
		self.remainingColours = [[0 for i in range(self.size)] for j in range(self.size)]    #stores domain of each variable


	def checkSafeAssignment(self,vertex,colourAssigned):
		for i in range(0,self.size):
			if(self.graph[vertex][i] and self.colourArray[i]==colourAssigned):     #adjacent vertex has the same colour
				return False
		return True




	def findVertexWithMaxDegree(self,verticesArray):    #this is the Degree Heuristic for choosing a new variable for assignment
		maxDegreeVertex = -1    						#vertices vary from 0 to n-1
		currentMaxValue = -1
		for i in range(0,self.size):   
			if(self.colourArray[i]==-1 and sum(self.graph[i])>currentMaxValue and (i in verticesArray)):   #i.e. vertex hasn't been assigned a colour yet and has the highest degree seen so far
				currentMaxValue = sum(self.graph[i])
				maxDegreeVertex = i
		#print("Vertex chosen "+str(maxDegreeVertex)+"\n")
		return maxDegreeVertex

	def findLeastConstrainingValue(self,vertex):
		colour = -1   #No colour finalised yet
		minReductions = 100000
		minReductionsColour = -1         #Find colour which gives minimum no of redutions
	
		for i in range(0,self.m):     #iterate over all colours
			reductions = 0
			#Iterate over all vertices and count number of reductions
			flag = 0
			for j in range(0,self.size):  
				if(self.graph[vertex][j] and (i in self.remainingColours[j]) ):      #that is, adjacent variable's domain has colour i or not
					reductions = reductions + (len(self.remainingColours[j])-1)      #we get the remaining colours by removing the colour i
					                                                     #flag=1 ndicates that a variable's domain is getting reduced to zero
			if(reductions < minReductions and self.checkSafeAssignment(vertex,i) ):  #for each color, see if reductions are minimum
				minReductions = reductions
				minReductionsColour = i

		if(minReductionsColour == -1):      #No safe and valid assignment found
			return -1
		
		return minReductionsColour


	def minimumRemainingValues(self):
		minRemValues = 1000
		minRemValuesVertex = -1
		for vertex in range(0,self.size):
			if(self.colourArray[vertex]==-1): #hasn't been assigned yet
				remValues = len(self.remainingColours[vertex])    #remainingColours is a 2d list
				if(remValues<=minRemValues):
					minRemValues = remValues
					minRemValuesVertex = vertex
	#Now find ALL vertices with minimum remaining values, and apply the degree heuristic
		minRemValuesVertices = []
		for i in range(0,self.size):
			if(len(self.remainingColours[i])==minRemValues):
				minRemValuesVertices.append(i)

		if(len(minRemValuesVertices)>1):    #apply the degree heuristic to break this tie
			return self.findVertexWithMaxDegree(minRemValuesVertices)
		else:
			#print("Vertex chosen "+str(minRemValuesVertex)+"\n")
			return minRemValuesVertex




	def forwardChecking(self,vertex,colourChosen):    #removes the colour chosen for a vertex from the domain of adjacent vertices
		for i in range(0,self.size):
			if(self.graph[vertex][i] and (colourChosen in self.remainingColours[i])):
				self.remainingColours[i].remove(colourChosen)

	def assignColour(self,vertex,colour):
		self.colourArray[vertex] = colour

		for i in range(1,self.size):
			if(self.graph[vertex][i]):
				if (colour in self.remainingColours[i]):
					self.remainingColours[i].remove(colour)


	def Initialisation(self,adjacencyMatrix):
		for i in range(0,self.size):
			for j in range(0,self.size):
				self.graph[i][j] = adjacencyMatrix[i][j]
		colourList = []
		for i in range(0,self.m):
			colourList.append(i)
		for i in range(0,self.size):
			self.colourArray[i] = -1
			self.remainingColours[i] = colourList      #Initially the domains of all vertices are full

def solveCSPGraphColourability():
	#noOfVertices = 4
	
	#noOfColours = 3
	#adjacencyMatrix = [[0,1,1,0],[1,0,1,0],[1,1,0,1],[0,0,1,0]]
	noOfVertices = int(input('Enter number of vertices '))
	noOfColours = int(input('Enter number of colours '))
	
	#Input format is - 0 1 0, 0 0 1, 1 0 0
	adjacencyMatrix = [[0 for i in range(noOfVertices)] for j in range(noOfVertices)]
	i = 0
	j = 0
	matrix = raw_input('Enter adjacency matrix in specified format\n')
	rows = matrix.split(",")

	for r in rows:
		j = 0
		columns = r.split(" ")
		for c in columns:
			adjacencyMatrix[i][j] = int(c)
			j += 1

		i += 1

	object1 = CSPSolver(noOfVertices,noOfColours)
	object1.Initialisation(adjacencyMatrix)
	#Iterate until all vertices have been assigned a valid colour
	while(True):
		vertexForColouring = object1.minimumRemainingValues()
		colourValue = object1.findLeastConstrainingValue(vertexForColouring)
		if(colourValue == -1):
			
			print("Graph is not "+str(noOfColours)+" colourable \n")
			break
		else:
			object1.assignColour(vertexForColouring,colourValue)
			object1.forwardChecking(vertexForColouring,colourValue)
		
		flag = 0
		for i in range(0,noOfVertices):
			if(object1.colourArray[i]==-1):
				flag = 1
		if(flag==0):
			print("Solution found")
			for i in range(0,noOfVertices):
				print("Colour "+str(object1.colourArray[i])+" assigned to vertex "+str(i)+"\n")
			break


solveCSPGraphColourability()
