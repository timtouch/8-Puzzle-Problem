
'''
    For reference
    [ 0 1 2
      3 4 5
      6 7 8 ]

'''


def eightPuzzle (initialState, finalState):
    print("We are here ", initialState)
    print("We want to get to here ", finalState)

    print("Moved up ", moveUp(initialState))
    print("Current State", initialState)



def moveUp(currentState):
    emptySpace = currentState.index(0)
    print("Location of empty space is ", emptySpace)
    currentState[emptySpace], currentState[emptySpace - 3] = currentState[emptySpace - 3], currentState[emptySpace]
    return currentState

def moveDown(currentState):
    emptySpace = currentState.index(0)
    print("Location of empty space is ", emptySpace)
    currentState[emptySpace], currentState[emptySpace + 3] = currentState[emptySpace + 3], currentState[emptySpace]
    return currentState

def moveLeft(currentState):
    emptySpace = currentState.index(0)
    print("Location of empty space is ", emptySpace)
    currentState[emptySpace], currentState[emptySpace - 1] = currentState[emptySpace - 1], currentState[emptySpace]
    return currentState

def moveRight(currentState):
    emptySpace = currentState.index(0)
    print("Location of empty space is ", emptySpace)
    currentState[emptySpace], currentState[emptySpace + 1] = currentState[emptySpace + 1], currentState[emptySpace]
    return currentState
    

initialState = [ 2, 8, 3,
                 1, 6, 4,
                 7, 0, 5 ]

finalState = [ 1, 2, 3,
               8, 0, 4,
               7, 6, 5 ]

eightPuzzle(initialState, finalState)

print (moveUp(initialState))
