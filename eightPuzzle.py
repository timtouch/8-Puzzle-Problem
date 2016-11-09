
'''
    eightPuzzle.py

    Author: Timothy Touch
    Class: CECS 328
    Description:      The eight puzzle is a variant of n-puzzles where we have an n x n matrix of sequential numbers
                  with an empty space.  The puzzle is usually shuffled and then solved by sliding around the
                  number pieces.  In this program, we take an initial state and a final state that we want to reach.
                  The depth is used to limit how deep to search, limiting search time.
                      The final result is a display of the moves and order of steps to take to solve the puzzle.
    
    
    For index reference
    [ 0 1 2
      3 4 5
      6 7 8 ]

'''


def eightPuzzle (initialState, finalState):
    result = dfs(initialState, finalState, 100)

    if result == None:
        print("There is no solution")
    elif result == [None]:
        print("The Beginning is the End")
    else:
        count = 0
        print("Initial State")
        displayBoard(initialState)
        for step in result:
            count += 1
            print( "Step #", count)
            displayBoard(step)
        print (len(result), "moves")
    
class Node:
    def __init__(self, state, parent, depth):
        self.state = state
        self.parent = parent
        self.depth = depth

'''
    Format display of a board state
'''
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
    # Shallow copy state
    currentState = list(state)
    emptySpace = currentState.index(0)
    
    if direction == 'u' and emptySpace > 2:
        currentState[emptySpace], currentState[emptySpace - 3] = currentState[emptySpace - 3], currentState[emptySpace]
    elif direction == 'd' and emptySpace < 6:
        currentState[emptySpace], currentState[emptySpace + 3] = currentState[emptySpace + 3], currentState[emptySpace]
    elif direction == 'l' and emptySpace % 3 != 0:
        currentState[emptySpace], currentState[emptySpace - 1] = currentState[emptySpace - 1], currentState[emptySpace]
    elif direction == 'r' and emptySpace % 3 != 2:
        currentState[emptySpace], currentState[emptySpace + 1] = currentState[emptySpace + 1], currentState[emptySpace]
    else:
        return None
    return currentState

'''
    Returns a list of available moves from the state of a given node
'''
def expandNode(node):
    # Returns a list of expanded nodes, basically an adjacency vertex
    expNodes = []
    expNodes.append(Node(movement(node.state, 'u'), node, node.depth + 1))
    expNodes.append(Node(movement(node.state, 'd'), node, node.depth + 1))
    expNodes.append(Node(movement(node.state, 'l'), node, node.depth + 1))
    expNodes.append(Node(movement(node.state, 'r'), node, node.depth + 1))

    
    # Impossible nodes (those that return None) are not saved
    expNodes = [node for node in expNodes if node.state != None]
    return expNodes


'''
    Uses depth first search to find steps to solve puzzle
    
    initialState - The initial board state
    finalState - The goal we are trying to reach
    depth - Essentially the max amount of moves we are limited to making
        Allowing larger depth may take longer times and smaller depth may be insufficient
        to getting a solution
'''
def dfs(initialState, finalState, depth):

    maxDepth = depth
    nodes =[]
    visited = []
    
    nodes.append(Node(initialState, None, 0))
    while True:
        # Tried all solutions to set max depth and no solution was found
        if len(nodes) == 0:
            return None
        
        node = nodes.pop()
        # If we reach the final state, return the steps to get there
        if node.state  == finalState:
            moves = []
            temp = node
            while True:
                moves.insert(0, temp.state)
                if temp.depth <= 1:
                    break
                temp = temp.parent
            return moves
        
        # If we have already visited the node, skip it
        if node.state in visited:
            continue
        visited.append(node.state)
        # Check if we reach max depth of search
        # If not, add adjacency nodes to search
        if node.depth < maxDepth:
            expNodes = expandNode(node)
            nodes.extend(expNodes)
    

initialState = [ 2, 8, 3,
                 1, 6, 4,
                 7, 0, 5 ]

finalState = [ 1, 2, 3,
               8, 0, 4,
               7, 6, 5 ]

eightPuzzle(initialState, finalState)
