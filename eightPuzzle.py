
'''
    For index reference
    [ 0 1 2
      3 4 5
      6 7 8 ]

'''


def eightPuzzle (initialState, finalState):
    result = dfs(initialState, finalState, 10)

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
    def __init__(self, state, parent, operator, depth, cost):
        self.state = state
        self.parent = parent
        self.operator = operator
        self.depth = depth
        self.cost = cost

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

# This is a very bfs way of doing things
def expandNode(node, nodes):
    # Returns a list of expanded nodes
    expNodes = []
    expNodes.append(Node(movement(node.state, 'u'), node, "u", node.depth + 1, 0))
    expNodes.append(Node(movement(node.state, 'd'), node, "d", node.depth + 1, 0))
    expNodes.append(Node(movement(node.state, 'l'), node, "l", node.depth + 1, 0))
    expNodes.append(Node(movement(node.state, 'r'), node, "r", node.depth + 1, 0))

    
    # Impossible nodes (those that return None) are not saved
    expNodes = [node for node in expNodes if node.state != None]
    return expNodes
    
def dfs(initialState, finalState, depth):

    maxDepth = depth
    nodes =[]

    # Initialize moveset
    nodes.append(Node(initialState, None, None, 0, 0))
    while True:
        # Tried all solutions to set max depth and no solution was found
        if len(nodes) == 0:
            return None

        
        node = nodes.pop(0)

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

        # Check if we reach max depth of search
        if node.depth < maxDepth:
            expNodes = expandNode(node, nodes)
            expNodes.extend(nodes)
            nodes = expNodes
    

initialState = [ 2, 8, 3,
                 1, 6, 4,
                 7, 0, 5 ]

finalState = [ 1, 2, 3,
               8, 0, 4,
               7, 6, 5 ]
eightPuzzle(initialState, finalState)
