
'''
    For index reference
    [ 0 1 2
      3 4 5
      6 7 8 ]

'''

class Node:
    def __init__(self, state, parent, operator, depth, cost):
        self.state = state
        self.parent = parent
        self.operator = operator
        self.depth = depth
        self.cost = cost

def eightPuzzle (initialState, finalState):
    displayBoard(initialState)
    displayBoard(finalState)

    displayBoard(movement(initialState,'u'))
    displayBoard(initialState)

def displayBoard (boardState):
    print(' {} {} {} \n {} {} {} \n {} {} {} \n'.format(boardState[0], boardState[1], boardState[2], boardState[3], boardState[4], boardState[5], boardState[6], boardState[7], boardState[8]))  

'''
    Takes in a board state and a direction and moves the empty space in that direction if possible.
    The directions can be one of four states:
       'u' - up
       'd' - down
       'l' - left
       'r' - right
'''
def movement(state, direction):
    emptySpace = state.index(0)
    if direction == 'u' and emptySpace > 2:
        state[emptySpace], state[emptySpace - 3] = state[emptySpace - 3], state[emptySpace]
    if direction == 'd' and emptySpace < 6:
        state[emptySpace], state[emptySpace + 3] = state[emptySpace + 3], state[emptySpace]
    if direction == 'l' and mptySpace % 3 != 0:
        state[emptySpace], state[emptySpace - 1] = state[emptySpace - 1], state[emptySpace]
    if direction == 'r' and emptySpace % 3 != 2:
        state[emptySpace], state[emptySpace + 1] = state[emptySpace + 1], state[emptySpace]
    return state


    

initialState = [ 2, 8, 3,
                 1, 6, 4,
                 7, 0, 5 ]

finalState = [ 1, 2, 3,
               8, 0, 4,
               7, 6, 5 ]
eightPuzzle(initialState, finalState)
