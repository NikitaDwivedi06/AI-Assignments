
import numpy as np

goalState = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 0]])

goalStateCoords = []
for coords,value in np.ndenumerate(goalState):    #appending coordinates of all values from 0 to 8
        goalStateCoords.append([coords,value])
goalStateCoords.sort(key=lambda x:x[1])

class Node:
    def __init__(self,stateInfo,coordinates):
        self.stateInfo = stateInfo     #the complete state information in a numpy ndarray
        self.parent = None
        self.fValue = 0
        self.hValue = 0
        self.depth  = 0
        self.coordinates = coordinates  #the coods of the blank tile, this is a list of size 2


def generateChildren(parentNode):
    x,y = parentNode.coordinates
    childNodes = []                  #list of child node objects
    parentInfoList = parentNode.stateInfo.ravel()
    for newCoords in [(x-1, y),(x,y - 1),(x,y + 1),(x+1,y)]:
        if(newCoords[0]<3 and newCoords[0]>-1 and newCoords[1]<3 and newCoords[1]>-1 ): #valid move within boundaries
            newStateInfo = np.array(parentInfoList).reshape([3,3])
            #print("Old ",newStateInfo)
            newStateInfo[x,y],newStateInfo[newCoords[0],newCoords[1]] = newStateInfo[newCoords[0],newCoords[1]],newStateInfo[x,y]
            #print("New",newStateInfo)
            childNode = Node(newStateInfo,[newCoords[0],newCoords[1]])
            childNode.parent = parentNode
            childNode.fValue = parentNode.fValue + 1
            childNode.hValue = manhattanHeuristic(newStateInfo)
            childNode.depth = parentNode.depth+1              #For IDDFS
            childNodes.append(childNode)

    return childNodes


def manhattanHeuristic(stateInfo):

    stateInfoList = []
    for coords,value in np.ndenumerate(stateInfo):    #appending coordinates of all values from 0 to 8
        stateInfoList.append([coords,value])
    stateInfoList.sort(key=lambda x:x[1])
    sum = 0
    for i in range(1,9):
        sum = sum + abs(goalStateCoords[i][0][0]-stateInfoList[i][0][0]) + abs(goalStateCoords[i][0][1]-stateInfoList[i][0][1])
    return sum


def printPath(state):
    print(state.stateInfo)
    while(state.parent is not None):
        print(state.parent.stateInfo)
        state = state.parent

def printPathRecursive(state):
    if(state.parent is not None):
        printPathRecursive(state.parent)

    print(state.stateInfo)
