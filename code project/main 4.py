# ####################################################
# DE2-COM2 Computing 2
# Individual project
#
# Title: MAIN
# Authors: Liuqing Chen, Feng Shi, Isaac Engel, and
#          Nicolas Rojas
# ####################################################

import utils  # it might be helpful to use 'utils.py' 
# from timeit import default_timer as timer
from copy import deepcopy
class Node(object):
    def __init__(self, data, children = None):
        self.data = data
        self.children = children
        
# the following methods allow to index the .children --> no need to repeat

    def __getitem__(self,index):
        return self.children[index]
    
    def __setitem__(self,index,value):
        self.children[index] = value
        
    # def __repr__(self):
    #     return str(self.data)


# In[262]:


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



# In[ ]:

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
    global n, solution, x, y
    piece_id = current.data
    for pos in paths[piece_id]+[(0,0)]:
        solution[y+pos[1]][x+pos[0]] = (piece_id, n)

def dfs(current, score):
    global found, n, solution, x, y, width, height, target_score
    if found:
        return
    if not 0<x+current.data[0]<width or y+current.data[1]>=height:
        return
    # print(x+current.data[0], y+current.data[1])
    sol_pos_val = solution[y+current.data[1]][x+current.data[0]]
    if type(sol_pos_val) is int:
        if sol_pos_val == 0:
            score-=1
    else:
        if sol_pos_val[0] > 0:
            return
#        print(path)
#         print(x+current.data[0], y+current.data[1])
    if score == -2:
        return
    
    
    if current.children is not None:
        for child in current.children:
            if child.children is None:
                if score == target_score:
                    fit_tetris(child)
                    found = True
                    # print("perfect" ,n, path)
                    # print("partial", n, path)
        #         print(current.data, "score:", score)
            else:
                dfs(child, score)

def Tetris(target):
    global width, height, n, solution, x, y, found, target_score
    solution = target
    width = len(target[0])
    height = len(target)
    n = 1
    found = False
    target_score = 0
    for y in range(height):
        for x in range(width):
            if solution[y][x] == 1:
                found = False
                dfs(tree[0], 0)
                if found:
                    n+=1
    target_score = -1
    for y in range(height):
        for x in range(width):
            if solution[y][x] == 1:
    #             print(x,y)


                found = False
                dfs(tree[0], 0)
                if found:
                    n+=1
                else:
                    solution[y][x] = (0,0)

                # for line in solution:
                #     print(line)
                # print("")
            elif solution[y][x] == 0:
                solution[y][x] = (0,0)
    return solution