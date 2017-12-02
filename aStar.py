import numpy as np
from random import shuffle
from Utilities import Node,generateChildren,printPathRecursive

inp = raw_input('Enter initial state\n')
inpList = inp.split(" ")
inpList = list(map(int,inpList))
initialState = np.reshape(inpList,[-1,3])
for i in range(0,3):
    for j in range(0,3):
        if(initialState[i][j]==0):
            xCoord,yCoord = i,j
#print(initialState)
#initialState = np.array([[3,4,5],[1,2,6],[7,8,0]])
initialStateList = initialState.ravel()                 #Convert to 1d list
goalState = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 0]])


def generateRandomState(initialState):

    #randomIntegers = np.random.randint(9,size=(3,3))    (Repeats integers)
    listInts = initialState
    list1 = []
    for row in listInts:
        list1.extend(row)

    shuffle(list1)
    initialState = np.empty([3,3])
    initialState = list1         #new shuffled list
    initialState = np.reshape(initialState,[-1,3])  #reshaping to a 3*3 matrix
    return initialState

def calculateInversionCount(initialStateList):
    inversionCount = 0
    for i in range(0,8):
        for j in range(i+1,9):
            if (initialStateList[i] and initialStateList[j] and initialStateList[i] > initialStateList[j]):
                inversionCount = inversionCount + 1
    return inversionCount










#Check whether the puzzle is solvable
#If no of inversions are even, the puzzle is solvable
invCount = calculateInversionCount(initialStateList)
solvable = (invCount%2)==0
while(solvable is False):
    print('Unsolvable, generating new random state')
    invCount = calculateInversionCount(initialStateList)
    if(invCount%2==0):
        solvable = True
        initialState = generateRandomState(initialState)

#Intialise fringe list, expanded list and root node
rootNode = Node(initialState,[xCoord,yCoord])       #initially blank tile position
fringeList = []
expandedList = []
fringeList.append(rootNode)
currentNode = rootNode       #this is the node which is expanded
goalStateFound = 0
print("Start State is\n"+str(currentNode.stateInfo)+"\n")

while(fringeList):
    if(np.array_equal(currentNode.stateInfo,goalState)):
        #this node is the goal node, we have found the solution
        print('Goal Node Found')
        goalStateFound = 1
        #
        print("Path Cost = "+str(currentNode.fValue))
        print("Number of generated states = "+str(len(expandedList)+len(fringeList)))
        print("The Path is\n")
        printPathRecursive(currentNode)
        break
    else:
        childNodesList = []
        childNodesList = generateChildren(currentNode)
        fringeList.remove(currentNode)
        expandedList.append(currentNode)

        for child in childNodesList:
            flag=0
            print("Child at depth = "+str(child.fValue)+"\n"+str(child.stateInfo))
            print("F, G and H values are "+str(child.fValue+child.hValue)+" "+str(child.fValue)+" "+str(child.hValue)+"\n")
            fringeList.append(child)
            '''
            #if child node already exists, check if new gvalue is better that the existing one
            #'child' is the node in childNodesList

            for nodes in fringeList:
                if(nodes.coordinates == child.coordinates):      #we have found a pre-existing node
                    flag=1
                    oldChild = nodes
                    oldGValue = oldChild.hValue + oldChild.fValue
                    newGValue = child.hValue + child.fValue
                    if(newGValue<oldGValue):    #we have found a new node giving better cost
                        fringeList.remove(oldChild)
                        fringeList.add(child)
            if(flag==0):    #node not found in fringe list
                fringeList.append(child)
                '''

        #Now choose from fringe list the node with minimum (f+h) value as the next current node
        nextCurrentNode = None
        minval = 1000
        for nodes in fringeList:
            gValue = nodes.fValue + nodes.hValue
            if(gValue<minval):
                minval = gValue
                nextCurrentNode = nodes

        currentNode = nextCurrentNode

if not fringeList and goalStateFound == 0 :
    print('Goal State does not exist')
