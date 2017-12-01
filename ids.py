import numpy as np
import sys
from Utilities import Node,generateChildren,printPathRecursive

goalState = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 0]])
#Input format is - 1 2 3 4 0 5 7 8 6
inp = str(raw_input('Enter initial state\n'))
inpList = inp.split(" ")
inpList = list(map(int,inpList))

initialState = np.reshape(inpList,[-1,3])
print(initialState)
print(goalState)
for i in range(0,3):
    for j in range(0,3):
        if(initialState[i][j]==0):
            xCoord,yCoord = i,j
#expandedListTotal = []

def depthLimitedSearch(initialState,limit):
    expandedNodes = []
    currentNode = Node(initialState,[xCoord,yCoord])
    path = []

    def recursiveDLS(currentNode,limit,path):
        cutoff_occured = False
        #expandedListTotal.append(currentNode)

        if(np.array_equal(currentNode.stateInfo,goalState)):

             print('Goal node found')
             print('Depth of goal node = ',currentNode.depth)
             #print('Number of nodes expanded are ',count)
             print('The path followed is - ')
             printPathRecursive(currentNode)

             return 'Success'
        elif limit == 0:        #We have expanded till the current allowed limit
             return 'cutoff'
        else:

             for child in generateChildren(currentNode):
                    #print("CHILD - ",child.stateInfo)
                    result = recursiveDLS(child,limit-1,path)    #We have expanded one level, so reduce the limit

                    if result == 'cutoff':
                        cutoff_occured = True
                    elif result != 'failure':
                        return result

        if cutoff_occured:
            return 'cutoff'
        else:
            return 'failure'

    return recursiveDLS(currentNode,limit,path)


def IterativeDeepeningSearch():
    for depth in range(0,10000):
        print("Depth cutoff = ",depth)
        result = depthLimitedSearch(initialState,depth)
        if result is not 'cutoff':
            return result

res = IterativeDeepeningSearch()
