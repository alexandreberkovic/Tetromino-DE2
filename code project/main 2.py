# ####################################################
# DE2-COM2 Computing 2
# Individual project
#
# Title: MAIN
# Authors: Liuqing Chen, Feng Shi, Isaac Engel, and
#          Nicolas Rojas
# ####################################################

import utils  # it might be helpful to use 'utils.py' 
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
        
    def __repr__(self):
        return str(self.data)


# In[262]:


tree =     Node('Home', [
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





# In[267]:


# def get(x,y):
#     global width, height, solution
#     if x>=width or y>=height or x<0:
#         return 0
#     else:
#         return solution[y][x]

def fit_tetris(path, piece_id):
    global n, solution, x, y
    for pos in path:
        solution[y+pos.data[1]][x+pos.data[0]] = (piece_id, n)

def dfs(current,path, score):
    global found, n, solution, x, y, found, found_partial, partial_id, width, height
    if found:
        return
    if len(path) == 4:
        if score == 0:
            fit_tetris(path, current.data)
            found = True
            # print("perfect" ,n, path)
        elif score == -1 and found_partial is None:
            found_partial = path
            partial_id = current.data
            # print("partial", n, path)
#         print(current.data, "score:", score)
    else:
        if x+current.data[0]>=width or y+current.data[1]>=height or x+current.data[0]<0:
            return
        # print(x+current.data[0], y+current.data[1])
        sol_pos_val = solution[y+current.data[1]][x+current.data[0]]
        if len(str(sol_pos_val)) > 1 and sol_pos_val[0] > 0:
            return
        path.append(current)
#        print(path)
#         print(x+current.data[0], y+current.data[1])
        if sol_pos_val == 0:
            score-=1
        if score == -2:
            return
    
    
    if current.children is not None:
        for child in current.children:
            dfs(child, deepcopy(path), score)

def Tetris2(target):
    global width, height, n, solution, x, y, found, found_partial, partial_id
    solution = target
    width = len(target[0])
    height = len(target)
    n = 1
    found = False
    for y in range(height):
        for x in range(width):
            if solution[y][x] == 1:
    #             print(x,y)


                found = False
                found_partial = None
                dfs(tree[0], [], 0)
                if found:
                    n+=1
                elif found_partial is not None:
                    fit_tetris(found_partial, partial_id)
                    n+=1
                else:
                    solution[y][x] = (0,0)

                # for line in solution:
                #     print(line)
                # print("")
            elif solution[y][x] == 0:
                solution[y][x] = (0,0)
    return solution
