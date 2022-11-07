#!/usr/bin/env python
# coding: utf-8

# # The following three codes are ones needed for the solving of the tetromino problem: main, utils & performance_std

# ## This is utils.py

# ## This is main.py

# ## This is performance_std.py

# # Computing Tetromino project

# ## 1. First we create a tree
# ### This tree has all the diffferent possibilities for tetromino pieces relative to a starting position

# In[261]:


# the following class allows to create a tree of all the relative positions for the pieces
solution = []
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
            Node((0, 1), [
                Node((0, 2), [
                    Node((1, 2), [Node(4)]),
                    Node((-1, 2), [Node(8)]),
                    Node((-1, 1), [Node(14)]),
                ]),
                Node((-1, 1), [
                    Node((-2, 1), [Node(5)]),
                    Node((1, 1), [Node(13)]),
                    Node((-1, 2), [Node(19)]),
                ]),
                Node((1, 1), [
                    Node((2, 1), [Node(11)]),
                    Node((0, 2), [Node(12)]),
                    Node((1, 2), [Node(17)]),
                ]),
            ]),
                
            Node((1, 0), [
                Node((0, 1), [
                    Node((2, 0), [Node(7)]),
                    Node((0, 2), [Node(10)]),
                    Node((-1, 1), [Node(16)]),
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
        ]),
    ])


# In[ ]:





# In[267]:


def get(x,y):
    if x>=width or y>=height or x<0:
        return 0
    else:
        return solution[y][x]

def fit_tetris(path, piece_id):
    for pos in path:
        solution[y+pos.data[1]][x+pos.data[0]] = (piece_id, n)
    
done = False
def dfs(current,path, score):
    global done
    if done:
        return
    if len(path) == 4:
        if score == 0:
            fit_tetris(path, current.data)
            done = True
#         print(current.data, "score:", score)
    else:
        sol_pos_val = get(x+current.data[0], y+current.data[1])
        if len(str(sol_pos_val)) > 1 and sol_pos_val[0] > 0:
            return
        path.append(current)
#        print(path)
#         print(x+current.data[0], y+current.data[1])
        if sol_pos_val == 0:
            score-=1
    
    
    if current.children is not None:
        for child in current.children:
            dfs(child, deepcopy(path), score)


# ## 2. Now that the tree is created, we create init functions for the grid
# ### A. We need to make sure that the algorithm understands that no tetromino piece can be placed outside of the grid's dimensions or on another piece
# ### B. We create a function that traverses the grid horizontally and finds out when there is a non-empty spot (i.e. when there is a 1 instead of a 0)

# In[263]:


from copy import deepcopy


# In[264]:


the_forbidden_pieces = {1,2,3} #Forbidden shapeIDs

# Example target shape, limit_tetris, and perfect_solution
target = [
            [0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 1, 0],
            [0, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 0]
         ]
solution = [
                    [(0, 0),  (0, 0),  (8, 1),  (0, 0),   (0, 0),  (0, 0)],
                    [(0, 0),  (0, 0),  (8, 1),  (0, 0),   (13, 2), (0, 0)],
                    [(0, 0),  (8, 1),  (8, 1),  (13, 2),  (13, 2), (13, 2)],
                    [(0, 0),  (13, 3), (18, 4), (18, 4),  (0, 0),  (0, 0)],
                    [(13, 3), (13, 3), (13, 3), (18, 4),  (18, 4), (0, 0)]
                   ]


# In[265]:


x = 0
y = 0
target = generate_target(6, 6, 0.5, the_forbidden_pieces)[0]
solution = deepcopy(target)

def Tetris2(solution):
    width = len(target[0])
    height = len(target)
    n = 1
    done = False
    for y in range(height):
        for x in range(width):
            if solution[y][x] == 1:
    #             print(x,y)


                done = False
                dfs(tree[0], [], 0)
                if not done:
                    solution[y][x] = (0,0)
                else:
                    n+=1
                for line in solution:
                    print(line)
                print("")
    #             for line in solution:
    #                 print(line)
            elif solution[y][x] == 0:
                solution[y][x] = (0,0)
    return solution
#     print(x)
#     print(solution)
#     visualisation(target, solution,  the_forbidden_pieces)


# In[ ]:





# ## 3. We now traverse the tree and check whether certain pieces fit or not
# ### A. Tree traversal is done by using a DFS --> recursively
# ### B. If more than once piece fits the zone, all the possibilities are entered in a dictionary

# In[266]:


# both these functions do not work: maximum recursion depth reached for some reason


# ## 4. If several pieces can fit the same zone, we implement a greedy algorithm
# ### A. Determine a score for each tetromino piece
# ### B. The piece with the highest score is added to the grid, the others are discarded

# ## 5. Test the algorithm
# ### A. Accuracy is tested
# ### B. Time of execution is tested

# In[275]:


# use the tests given in the code performance_std


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




