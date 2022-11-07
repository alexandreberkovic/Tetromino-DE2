# ####################################################
# DE2-COM2 Computing 2
# Individual project
#
# Title: MAIN
# Author: Alexandre Berkovic
# ####################################################

import utils  
from copy import deepcopy

# The Node class allows to create the tree with data and children at each node 
# Two special methods are also implemented to allow for indexing of children in the tree:
#     1. __getitem__ : allows to get the value from the Node class 
#     2. __setitem__: allows to set the given values  

class Node(object):
    def __init__(self, data, children = None):
        self.data = data
        self.children = children
    def __getitem__(self,index):
        return self.children[index]  
    def __setitem__(self,index,value):
        self.children[index] = value

# The tree is built by putting the most common relative coordinates at the top and on the left,
# this reduces the necessary amount of traversals so that if a relative coordinate doesn't fit
# it gets rid of the entire path. Indeed, the order of the tree matters since the first piece 
# found is selected, therefore pieces that go along the border are placed first.

tree = \
     Node('Home', [
        Node((0, 0), [
            Node((1, 0), [
                Node((0, 1), [
                    Node((2, 0), [Node(7)]),
                    Node((-1, 1), [Node(16)]),
                    Node((0, 2), [Node(10)]),
                ]),
                Node((2, 0), [
                    Node((2, 1), [Node(9)]),
                    Node((1, 1), [Node(15)]),
                ]),
                Node((1, 1), [
                    Node((1, 2), [Node(6)]),
                    Node((2, 1), [Node(18)]),
                ]),
            ]),

            Node((0, 1), [
                Node((-1, 1), [
                    Node((-2, 1), [Node(5)]),
                    Node((1, 1), [Node(13)]),
                    Node((-1, 2), [Node(19)]),
                ]),
                Node((1, 1), [
                    Node((0, 2), [Node(12)]),
                    Node((1, 2), [Node(17)]),
                    Node((2, 1), [Node(11)]),
                ]),
                Node((0, 2), [
                    Node((-1, 1), [Node(14)]),
                    Node((1, 2), [Node(4)]),
                    Node((-1, 2), [Node(8)]),
                ]),
            ]),
            
        ]),
    ])


# A dictionnary with the relative paths of the pieces (coordinate (0;0) isn't necessary) is created

paths =  {
    4:[(0, 1), (0, 2), (1, 2)],
    5:[(0, 1), (-1, 1), (-2, 1)],
    6:[(1, 0), (1, 1), (1, 2)],
    7:[(1, 0), (0, 1), (2, 0)],
    8:[(0, 1), (0, 2), (-1, 2)],
    9:[(1, 0), (2, 0), (2, 1)],
    10:[(1, 0), (0, 1), (0, 2)],
    11:[(0, 1), (1, 1), (2, 1)],
    12:[(0, 1), (1, 1), (0, 2)],
    13:[(0, 1), (-1, 1), (1, 1)],
    14:[(0, 1), (0, 2), (-1, 1)],
    15:[(1, 0), (2, 0), (1, 1)],
    16:[(1, 0), (0, 1), (-1, 1)],
    17:[(0, 1), (1, 1), (1, 2)],
    18:[(1, 0), (1, 1), (2, 1)],
    19:[(0, 1), (-1, 1), (-1, 2)],
}


def fit_tetris(current):
    """
    The fit_tetris function is called when a tetromino piece is fitted onto the grid and
    the (0,0) of the solution matrix is replaced by the piece_id and n
    n is the order in which the pieces are fitted
    """
    global n, solution, x, y # global variables are used as numerous functions have to access the data
    piece_id = current.data # the piece_id is the same as the leaf node in the tree
    for pos in paths[piece_id]+[(0,0)]:
        solution[y+pos[1]][x+pos[0]] = (piece_id, n)


def dfs(current, score):
    """
    To traverse the graph, we build a recursive DFS which is the most efficient way to do it
    A score variable is implemented where if a piece's relative coordinate doesn't fit: score -= 1
    A greedy algorithm is implemented (chooses the best solution at a given moment):
        1. The entire matrix is traversed once & only pieces of score = 0 are placed
        2. The matrix is traversed a second time & pieces of score = -1 are places to fill in all 3 square-holes
        3. If a piece has a score of -2, the function gets rid of it and passes onto the next branch of the tree
    """
    global found
    if found: # boolean variable which returns True if a piece is found, to exit the recursive tree rapidly 
        return 
    if not 0<=x+current.data[0]<width or y+current.data[1]>=height: # verifies if the piece fits in the grid
        return
    sol_pos_val = solution[y+current.data[1]][x+current.data[0]] # gives the absolute position of the piece in the grid
    if type(sol_pos_val) is int: # if the position is an integer (i.e. target matrix), implement score varianle
        if sol_pos_val == 0:
            score-=1
    else:
        if sol_pos_val[0] > 0: # if the position is a tuple different from (0,0), a piece is already fitted
            return
    if score < target_score:
        return  
    if current.children is not None: 
        for child in current.children:
            if child.children is None: # occurs when the branch is fully traversed
                if score == target_score:
                    fit_tetris(child)
                    found = True
            else:
                dfs(child, score) # does dfs again if no piece of target_score is found
         

def Tetris(target):
    """
    The Tetris function is the one called by performance_std and does the following:
        1. Traverses the grid vertically and horizontally
        2. When a 1 is found, it calls the function dfs 
        3. It first places all perfect pieces (score = 0)
        4. Then, it places imperfect pieces (score = -1)
    """
    global width, height, n, solution, x, y, found, target_score
    solution = target # modify the given matrix directly to avoid an initialization and save memory
    width = len(target[0])
    height = len(target)
    n = 1
    found = False
    target_score = 0
    for y in range(height): # traverses the grid vertically
        for x in range(width): # traverses the grid horizontally
            if solution[y][x] == 1: # if the position on the grid is non-empty
                found = False
                dfs(tree[0], 0) # call the function to traverse the tree
                if found:
                    n+=1 # is a piece is fitted, the "order" variable is increased by 1
    target_score = -1 # if no piece has a score = 0, the target_score is transformed to -1
    for y in range(height):
        for x in range(width):
            if solution[y][x] == 1:
                found = False
                dfs(tree[0], 0)
                if found:
                    n+=1
                else:
                    solution[y][x] = (0,0) # if no piece has a score of -1, the spot stays empty
            elif solution[y][x] == 0: # all the 0 of the solution matrix (= target matrix) are transformed into tuples
                solution[y][x] = (0,0)
    return solution