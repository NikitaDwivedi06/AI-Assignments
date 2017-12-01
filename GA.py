from random import randint
import random
from datetime import datetime
import time

#returns fitness value of a particular individual
def fitnessValueFunction(individual):
	
	'''
	listOfTuples = []
	for i in range(1,8):
		listOfTuples.append((individual[i],i))
	'''
	collisions = 0
	
	for i in range(0,8):
		for j in range(i+1,8):
			if(abs(individual[i]-individual[j]) == abs(i-j)):   #Diagonal collision
				collisions = collisions + 1
			if(individual[i]==individual[j]):            #Row collision
				collisions = collisions + 1

	return 28 - (collisions)                            #28 is the perfect fitness value


def reproduce(parent1,parent2):
	n = len(parent1)
	crossoverPoint = randint(0,n-1)
	child1 = parent1[0:crossoverPoint+1] + parent2[crossoverPoint+1:8]      #7 is the max index
	child2 = parent2[0:crossoverPoint+1] + parent1[crossoverPoint+1:8]
	#print("IN FUNCTION CHILD AND CROSSOVER "+str(child)+" "+str(crossoverPoint))
	return child1,child2

def mutate(individual):
	mutationProbability = 0.0005
	n = random.random()
	if(n<mutationProbability):
		x1 = randint(0,7)
		x2 = randint(0,7)
		individual[x1],individual[x2] = individual[x2],individual[x1]    #exchange queen positions
		#print("MUTATED")
	return individual

def getInitialPopulation():
	k = 10         #size of initial population
	listOfInitialPopulation = []    #stores k lists
	for i in range(0,k):
		listOfQueens = random.sample(range(8),8)      #returns a unique list of '8' numbers in the range 0-7
		listOfInitialPopulation.append(listOfQueens)
	return listOfInitialPopulation


def RandomSelection(population,fitnessFunction):
	#Calculate fitness values for the entire population
	dict1 = {}      #stores individual and its fitness function value
	totalFitnessValue = 0
	for individual in population:
		x = fitnessFunction(individual)
		individualString = " ".join(str(x) for x in individual)        #Conversion to string is required for this to be treated as a dict key
		dict1[individualString] = x
		totalFitnessValue = totalFitnessValue + x
	
	
	sortedPopulation = sorted(dict1.items(), key=lambda x: x[1],reverse=True)     #sort on basis of values(i.e. the fitness function values)
	
	sortedPopulationList = []            										  #stores individuals sorted according to fitness values in decreasing order
	for i in range(0,len(sortedPopulation)):
		#First convert each individual back to a list of integers (They're strings currently)
		list1 = sortedPopulation[i][0].split(" ")

		for i in range(0,len(list1)):
			list1[i] = int(list1[i])
		sortedPopulationList.append(list1)
	#for x in sortedPopulation:
	#	print(x)

	return sortedPopulationList


'''
def bestInPopulation(population,fitnessFunction):
	dict1 = {}
	for individual in population:
		x = fitnessFunction(individual)
		individualString = " ".join(str(x) for x in individual)        #Conversion to string is required for this to be treated as a dict key
		dict1[individualString] = x
		totalFitnessValue = totalFitnessValue + x
	
	
	sortedPopulation = sorted(dict1.items(), key=lambda x: x[1],reverse=True)
	return sortedPopulation[0]
'''

def GeneticAlgorithm(population,fitnessFunction):

	solution = ""
	#allow this loop to run for a certain amount of time
	startTime = datetime.now()
	endTime = time.time() + 15   #current time and 15 seconds
	i=0
	while(True):
		flag=0
		newPopulation = []
		sortedPopulationList = []
		sortedPopulationList = RandomSelection(population,fitnessFunction)
		child1 = []
		child2 = []
		
		for i in range(0,len(sortedPopulationList)-1):
			#Now select two entries for mating at a time
			parent1 = sortedPopulationList[i]
			parent2 = sortedPopulationList[i+1]
			#print("\nParent1: "+str(parent1)+"\n"+"Parent2: "+str(parent2))
			children = reproduce(parent1,parent2)
			child1 = children[0]
			child2 = children[1]
			child1 = mutate(child1)
			child2 = mutate(child2)
			if(fitnessFunction(child1)==28 or fitnessFunction(child2)==28 ):
				flag=1
				solution = child1 if fitnessFunction(child1) == 28 else child2
				
				
			#print("\nChildren: "+str(child1)+" "+str(child2))
			newPopulation.append(child1)
			newPopulation.append(child2)
		population = []
		population = newPopulation
		i = i+1
		if(flag==1):
			#print(solution)
			print("Queen Positions are:")
		
			i = 0
			for s in solution:
				print(str(i+1),str(s+1))
				i = i+1
			break

		
		if(time.time()>endTime):
			return i
			break


initialPopulation = getInitialPopulation()

s = GeneticAlgorithm(initialPopulation,fitnessValueFunction)

