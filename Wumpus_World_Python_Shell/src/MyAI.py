#Submitted By: UCInetID: ssmasood ,Name: Shah Masood ,ID: 16608754
#Team Name: KillWumpus
# ======================================================================
# FILE:        MyAI.py
#
# AUTHOR:      Abdullah Younis
#
# DESCRIPTION: This file contains your agent class, which you will
#              implement. You are responsible for implementing the
#              'getAction' function and any helper methods you feel you
#              need.
#
# NOTES:       - If you are having trouble understanding how the shell
#                works, look at the other parts of the code, as well as
#                the documentation.
#
#              - You are only allowed to make changes to this portion of
#                the code. Any changes to other portions of the code will
#                be lost when the tournament runs your code.
# ======================================================================

from Agent import Agent
from collections import defaultdict
class MyAI ( Agent ):

    def __init__ ( self ):
        # ======================================================================
        # YOUR CODE BEGINS
        # ======================================================================
        self.lastx = 1
        self.lasty = 1
        self.x = 1
        self.y = 1
        self.bad = []
        self.safepit = []
        self.safewumpus = []
        self.visited = []
        self.potentialpit = []
        self.potentialwumpus = []
        self.gold = False
        self.look = "R"
        self.todo = []
        self.ret = False
        self.wumpus = False
        self.arrow = True
        self.counter = 0
        self.sizex = 7
        self.sizey = 7
        self.moves = 0
        # ======================================================================
        # YOUR CODE ENDS
        # ======================================================================

    def getAction( self, stench, breeze, glitter, bump, scream ):
        #make safepit == visited, then return
        # ======================================================================
        # YOUR CODE BEGINS
        # ======================================================================
       
        #print("lastx", self.lastx)
        #print("lasty", self.lasty)
        #print("x", self.x)
        #print("y", self.y)
        #print("bad", self.bad)
        #print("safepit", self.safepit)
        #print("safewumpus", self.safewumpus)
        #print("visited", self.visited)
        #print("potentialpit", self.potentialpit)
        #print("potentialwumpus", self.potentialwumpus)
        #print("gold", self.gold)
        ##print("look", self.look)
        #print("todo", self.todo)
        #print("ret", self.ret)
        #print("wumpus", self.wumpus)
        #print("arrow", self.arrow)
        #print("counter",self.counter)
        #print("moves", self.moves)
        #print("sizex", self.sizex)
        #print("sizey", self.sizey)
        if (bump):
            if self.look == "R":
                if self.y == self.sizey:
                    self.sizex = self.x-1
                    self.x = self.x-1
                    self.look = "D"
                    self.lastx = self.x
                    self.lasty = self.y
                    return Agent.Action.TURN_RIGHT
                self.sizex = self.x-1
                self.x = self.x-1
                self.look = "U"
                self.lastx = self.x
                self.lasty = self.y
                return Agent.Action.TURN_LEFT
            if self.look == "U":
                if self.x == 1:
                    self.sizey= self.y-1
                    self.y = self.y-1
                    self.look = "R"
                    self.lastx = self.x
                    self.lasty = self.y
                    return Agent.Action.TURN_RIGHT
                self.sizey = self.y-1
                self.y = self.y-1
                self.look = "L"
                self.lastx = self.x
                self.lasty = self.y
                return Agent.Action.TURN_LEFT
            if self.look == "L":
                if self.y == 1:
                    self.x = self.x+1
                    self.look = "U"
                    self.lastx = self.x
                    self.lasty = self.y
                    return Agent.Action.TURN_RIGHT
                self.x = self.x+1
                self.look = "D"
                self.lastx = self.x
                self.lasty = self.y
                return Agent.Action.TURN_LEFT
            if self.look =="D":
                if self.x == 1:
                    self.y = self.y+1
                    self.look = "R"
                    self.lastx = self.x
                    self.lasty = self.y
                    return Agent.Action.TURN_RIGHT
                self.y = self.y+1
                self.look = "R"
                self.lastx = self.x
                self.lasty = self.y
                return Agent.Action.TURN_LEFT
        if (scream):
            self.wumpus = True

        self.safepit= list(set(self.safepit))
        if (self.wumpus):
            if not breeze:
                self.safePits()
            stench = False
            self.potentialwumpus = []
        self.removePits()
        #if self.todo:
        #    xy = self.todo[0]
        #    if (xy[0],xy[1]) == (self.x,self.y):
        #        self.todo.remove(xy)
        if (glitter):
                self.gold = True
                return Agent.Action.GRAB
        if (breeze):
            if (self.x, self.y) == (1,1):
                return Agent.Action.CLIMB
        self.moves += 1
        if self.gold:# or (set(self.safepit) == set(self.visited) and len(self.safepit) > 1):
            if (self.x,self.y) == (1,1):
                return Agent.Action.CLIMB
            if not self.todo:
                self.todo = self.calculateWayBack(self.x,self.y, 1, 1)
        
        if self.todo:
            xy = self.todo[0]
            if xy == (self.x-1,self.y):
                if self.look == "R":
                    self.look ="U"
                    return Agent.Action.TURN_LEFT
                if self.look == "U":
                    self.look = "L"
                    return Agent.Action.TURN_LEFT
                if self.look == "D":
                    self.look = "L"
                    return Agent.Action.TURN_RIGHT
                else:
                    self.todo.remove(xy)
                    self.setCord()
                    return Agent.Action.FORWARD
            
            if xy == (self.x+1,self.y):
                if self.look == "L":
                    self.look ="D"
                    return Agent.Action.TURN_LEFT
                if self.look == "U":
                    self.look = "R"
                    return Agent.Action.TURN_RIGHT
                if self.look == "D":
                    self.look = "R"
                    return Agent.Action.TURN_LEFT
                else:
                    self.todo.remove(xy)
                    self.setCord()
                    return Agent.Action.FORWARD

            if xy == (self.x,self.y-1):
                if self.look == "R":
                    self.look ="D"
                    return Agent.Action.TURN_RIGHT
                if self.look == "L":
                    self.look = "D"
                    return Agent.Action.TURN_LEFT
                if self.look == "U":
                    self.look = "L"
                    return Agent.Action.TURN_LEFT
                else:
                    self.todo.remove(xy)
                    self.setCord()
                    return Agent.Action.FORWARD

            if xy == (self.x,self.y+1):
                if self.look == "L":
                    self.look ="U"
                    return Agent.Action.TURN_RIGHT
                if self.look == "R":
                    self.look = "U"
                    return Agent.Action.TURN_LEFT
                if self.look == "D":
                    self.look = "R"
                    return Agent.Action.TURN_LEFT
                else:
                    self.todo.remove(xy)
                    self.setCord()
                    return Agent.Action.FORWARD
        

            
        if (self.x, self.y) == (self.lastx, self.lasty):
            self.counter += 1
        else:
            self.counter = 0
        
        if (self.counter >=4 ):
            self.ret = True
        else:
            self.ret = False
            
        if (self.x, self.y) not in self.visited:    
            self.visited.append((self.x, self.y))
                                
        #print("here")
        if (stench and not breeze):
            temp = []
            if self.potentialwumpus:
                #if we found stench before, then intersect with current stench to narrow down
                temp.append((self.x+1,self.y))
                temp.append((self.x,self.y+1))
                temp.append((self.x-1,self.y))
                temp.append((self.x,self.y-1))
                temp = list(set(temp))
                #print(temp)
                self.potentialwumpus = list(set(self.potentialwumpus).intersection(temp))
                #print(list(set(self.potentialwumpus).symmetric_difference(temp)))
                self.safepit += (list(set(self.potentialwumpus).symmetric_difference(temp)))
                #print("here2")
            else:
                self.potentialwumpus.append((self.x+1,self.y))
                self.potentialwumpus.append((self.x,self.y+1))
                self.potentialwumpus.append((self.x-1,self.y))
                self.potentialwumpus.append((self.x,self.y-1))
                self.potentialwumpus = list(set(self.potentialwumpus))
            self.removePits()
            if (self.arrow):
                if (self.x,self.y) == (1,1):
                    self.potentialwumpus.remove((self.x+1,self.y))
                    self.arrow = False
                    return Agent.Action.SHOOT
                if len(self.potentialwumpus) == 1:        
                    if self.look == "R":
                        if self.potentialwumpus[0] == (self.x+1,self.y):
                            self.arrow = False
                            return Agent.Action.SHOOT
                        if self.potentialwumpus[0] == (self.x,self.y+1):
                            self.look = "U"
                            return Agent.Action.TURN_LEFT
                        if self.potentialwumpus[0] == (self.x,self.y-1):
                            self.look = "D"
                            return Agent.Action.TURN_RIGHT
                        
                    if self.look == "L":
                        if self.potentialwumpus[0] == (self.x-1,self.y):
                            self.arrow = False
                            return Agent.Action.SHOOT
                        if self.potentialwumpus[0] == (self.x,self.y+1):
                            self.look = "U"
                            return Agent.Action.TURN_RIGHT
                        if self.potentialwumpus[0] == (self.x,self.y-1):
                            self.look = "D"
                            return Agent.Action.TURN_LEFT
                        
                    if self.look == "U":
                        if self.potentialwumpus[0] == (self.x,self.y+1):
                            self.arrow = False
                            return Agent.Action.SHOOT
                        if self.potentialwumpus[0] == (self.x-1,self.y):
                            self.look = "L"
                            return Agent.Action.TURN_LEFT
                        if self.potentialwumpus[0] == (self.x+1,self.y):
                            self.look = "R"
                            return Agent.Action.TURN_RIGHT
                      
                    if self.look == "D":
                        if self.potentialwumpus[0] == (self.x,self.y-1):
                            self.arrow = False
                            return Agent.Action.SHOOT
                        if self.potentialwumpus[0] == (self.x+1,self.y):
                            self.look = "R"
                            return Agent.Action.TURN_LEFT
                        if self.potentialwumpus[0] == (self.x-1,self.y):
                            self.look = "L"
                            return Agent.Action.TURN_RIGHT
                if (self.x <=4 and self.y <=4) or (set(self.safepit) == set(self.visited) and len(self.safepit) > 1) :   
                    if self.look == "L" and self.x == 1: #if im facing a wall default to looking up
                        if self.y == self.sizey: #if im at a corner
                            self.look = "D"
                            return Agent.Action.TURN_LEFT
                        self.look = "U"
                        return Agent.Action.TURN_RIGHT
                    if self.look == "R" and self.x == self.sizex: 
                        if self.y == self.sizey:
                            self.look = "D"
                            return Agent.Action.TURN_RIGHT
                        self.look = "U"
                        return Agent.Action.TURN_LEFT
                    if self.look == "U" and self.y == self.sizey:
                        if self.x == self.sizex:
                            self.look ="L"
                            return Agent.Action.TURN_LEFT
                        self.look = "R"
                        return Agent.Action.TURN_RIGHT
                    if self.look == "D" and self.y == 1:
                        if self.x == self.sizex:
                            self.look ="L"
                            return Agent.Action.TURN_RIGHT
                        self.look = "R"
                        return Agent.Action.TURN_LEFT
                    if (self.x+1,self.y) in self.potentialwumpus:
                        if self.look == "R":
                            self.potentialwumpus.remove((self.x+1,self.y))
                            self.safepit.append((self.x+1,self.y))
                        self.removePits()
                        self.arrow = False
                        return Agent.Action.SHOOT
                    if (self.x-1, self.y) in self.potentialwumpus:
                        if self.look == "L":
                           self.potentialwumpus.remove((self.x-1,self.y))
                           self.safepit.append((self.x-1,self.y))
                        self.removePits()
                        self.arrow = False
                        return Agent.Action.SHOOT
                    if (self.x, self.y+1) in self.potentialwumpus:
                        if self.look == "U":
                            self.potentialwumpus.remove((self.x,self.y+1))
                            self.safepit.append((self.x, self.y+1))
                        self.removePits()
                        self.arrow = False
                        return Agent.Action.SHOOT
                    if (self.x, self.y-1) in self.potentialwumpus:
                        if self.look == "D":
                            self.potentialwumpus.remove((self.x,self.y-1))
                            self.safepit.append((self.x, self.y-1))
                        self.removePits()
                        self.arrow = False
                        return Agent.Action.SHOOT
           
        if (breeze):
            if (self.x,self.y) == (1,1):
                return Agent.Action.CLIMB
            else:
                self.addPits()
        elif not stench:
            self.safePits()

        self.removePits()
        if set(self.safepit) == set(self.visited) and len(self.safepit) > 1:
            if (self.x,self.y) == (1,1):
                return Agent.Action.CLIMB
            if not self.todo:
                self.todo = self.calculateWayBack(self.x,self.y, 1, 1)
        #if self.ret:
        #    templist = list(set(self.safepit).symmetric_difference(self.visited))
        #        templist.sort()
        #    close = 99
        #    for xy in templist:
        #        if ((xy[0] - self.x)**2 + (xy[1] - self.y)**2)**(0.5) < close:
        #            closexy = xy
        #            close = ((xy[0] - self.x)**2 + (xy[1] - self.y)**2)**(0.5)
        #    self.todo = self.calculateWayBack(self.x, self.y, closexy[0], closexy[1])
        if (self.x,self.y) in self.todo:
            self.todo.remove((self.x,self.y))
        if self.todo:
            xy = self.todo[0]
            if xy == (self.x-1,self.y):
                if self.look == "R":
                    self.look ="U"
                    return Agent.Action.TURN_LEFT
                if self.look == "U":
                    self.look = "L"
                    return Agent.Action.TURN_LEFT
                if self.look == "D":
                    self.look = "L"
                    return Agent.Action.TURN_RIGHT
                else:
                    self.todo.remove(xy)
                    self.setCord()
                    return Agent.Action.FORWARD
            
            if xy == (self.x+1,self.y):
                if self.look == "L":
                    self.look ="D"
                    return Agent.Action.TURN_LEFT
                if self.look == "U":
                    self.look = "R"
                    return Agent.Action.TURN_RIGHT
                if self.look == "D":
                    self.look = "R"
                    return Agent.Action.TURN_LEFT
                else:
                    self.todo.remove(xy)
                    self.setCord()
                    return Agent.Action.FORWARD

            if xy == (self.x,self.y-1):
                if self.look == "R":
                    self.look ="D"
                    return Agent.Action.TURN_RIGHT
                if self.look == "L":
                    self.look = "D"
                    return Agent.Action.TURN_LEFT
                if self.look == "U":
                    self.look = "L"
                    return Agent.Action.TURN_LEFT
                else:
                    self.todo.remove(xy)
                    self.setCord()
                    return Agent.Action.FORWARD

            if xy == (self.x,self.y+1):
                if self.look == "L":
                    self.look ="U"
                    return Agent.Action.TURN_RIGHT
                if self.look == "R":
                    self.look = "U"
                    return Agent.Action.TURN_LEFT
                if self.look == "D":
                    self.look = "R"
                    return Agent.Action.TURN_LEFT
                else:
                    self.todo.remove(xy)
                    self.setCord()
                    return Agent.Action.FORWARD                                 
        #Only move in safe spots and not visited unless we circled around
        #print("here2")
        if self.look == "R":
            if ((self.x+1,self.y) in self.safepit and (self.x+1,self.y) not in self.visited) and self.x+1 <= self.sizex: 
                self.setCord()
                return Agent.Action.FORWARD
            else:
                templist = list(set(self.safepit).symmetric_difference(self.visited))
                templist.sort()
                close = 99
                far = 0.0
                for xy in templist:
                    if ((xy[0] - self.x)**2 + (xy[1] - self.y)**2)**(0.5) <= close:
                        if ((xy[0] - self.x)**2 + (xy[1] - self.y)**2)**(0.5) == close:
                            if ((xy[0] - 1)**2 + (xy[1] - 1)**2)**(0.5) >= far:
                                close = ((xy[0] - self.x)**2 + (xy[1] - self.y)**2)**(0.5) 
                                closexy = xy
                                far = ((xy[0] - 1)**2 + (xy[1] - 1)**2)**(0.5)
                        else:
                            closexy = xy
                            close = ((xy[0] - self.x)**2 + (xy[1] - self.y)**2)**(0.5)
                            far = ((xy[0] - 1)**2 + (xy[1] - 1)**2)**(0.5)
                self.todo = self.calculateWayBack(self.x, self.y, closexy[0], closexy[1])
                #self.look = "U"
                #self.lastx = self.x
                #self.lasty = self.y
                #return Agent.Action.TURN_LEFT
        if self.look == "L":
            if ((self.x-1,self.y) in self.safepit and (self.x-1,self.y) not in self.visited) and self.x-1 >= 1:
                self.setCord()
                return Agent.Action.FORWARD
            else:
                templist = list(set(self.safepit).symmetric_difference(self.visited))
                templist.sort()
                close = 99
                far = 0.0
                for xy in templist:
                    if ((xy[0] - self.x)**2 + (xy[1] - self.y)**2)**(0.5) <= close:
                        if ((xy[0] - self.x)**2 + (xy[1] - self.y)**2)**(0.5) == close:
                            if ((xy[0] - 1)**2 + (xy[1] - 1)**2)**(0.5) >= far:
                                close = ((xy[0] - self.x)**2 + (xy[1] - self.y)**2)**(0.5) 
                                closexy = xy
                                far = ((xy[0] - 1)**2 + (xy[1] - 1)**2)**(0.5)
                        else:
                            closexy = xy
                            close = ((xy[0] - self.x)**2 + (xy[1] - self.y)**2)**(0.5)
                            far = ((xy[0] - 1)**2 + (xy[1] - 1)**2)**(0.5)
                self.todo = self.calculateWayBack(self.x, self.y, closexy[0], closexy[1])
        if self.look == "U":
            if ((self.x,self.y+1) in self.safepit and (self.x,self.y+1) not in self.visited) and self.y+1 <= self.sizey:
                self.setCord()
                return Agent.Action.FORWARD
            else:
                templist = list(set(self.safepit).symmetric_difference(self.visited))
                templist.sort()
                close = 99
                far =0.0
                for xy in templist:
                    if ((xy[0] - self.x)**2 + (xy[1] - self.y)**2)**(0.5) <= close:
                        if ((xy[0] - self.x)**2 + (xy[1] - self.y)**2)**(0.5) == close:
                            if ((xy[0] - 1)**2 + (xy[1] - 1)**2)**(0.5) >= far:
                                close = ((xy[0] - self.x)**2 + (xy[1] - self.y)**2)**(0.5) 
                                closexy = xy
                                far = ((xy[0] - 1)**2 + (xy[1] - 1)**2)**(0.5)
                        else:
                            closexy = xy
                            close = ((xy[0] - self.x)**2 + (xy[1] - self.y)**2)**(0.5)
                            far = ((xy[0] - 1)**2 + (xy[1] - 1)**2)**(0.5)
                self.todo = self.calculateWayBack(self.x, self.y, closexy[0], closexy[1])
        if self.look =="D":
            if ((self.x,(self.y)-1) in self.safepit and (self.x,self.y-1) not in self.visited) and self.y-1 >= 1:
                self.setCord()
                return Agent.Action.FORWARD
            else:
                templist = list(set(self.safepit).symmetric_difference(self.visited))
                templist.sort()
                close = 99
                far =0.0 
                for xy in templist:
                    if ((xy[0] - self.x)**2 + (xy[1] - self.y)**2)**(0.5) <= close:
                        if ((xy[0] - self.x)**2 + (xy[1] - self.y)**2)**(0.5) == close:
                            if ((xy[0] - 1)**2 + (xy[1] - 1)**2)**(0.5) >= far:
                                close = ((xy[0] - self.x)**2 + (xy[1] - self.y)**2)**(0.5) 
                                closexy = xy
                                far = ((xy[0] - 1)**2 + (xy[1] - 1)**2)**(0.5)
                        else:
                            closexy = xy
                            close = ((xy[0] - self.x)**2 + (xy[1] - self.y)**2)**(0.5)
                            far = ((xy[0] - 1)**2 + (xy[1] - 1)**2)**(0.5)
                self.todo = self.calculateWayBack(self.x, self.y, closexy[0], closexy[1])

        if self.todo:
            xy = self.todo[0]
            if xy == (self.x-1,self.y):
                if self.look == "R":
                    self.look ="U"
                    return Agent.Action.TURN_LEFT
                if self.look == "U":
                    self.look = "L"
                    return Agent.Action.TURN_LEFT
                if self.look == "D":
                    self.look = "L"
                    return Agent.Action.TURN_RIGHT
                else:
                    self.todo.remove(xy)
                    self.setCord()
                    return Agent.Action.FORWARD
            
            if xy == (self.x+1,self.y):
                if self.look == "L":
                    self.look ="D"
                    return Agent.Action.TURN_LEFT
                if self.look == "U":
                    self.look = "R"
                    return Agent.Action.TURN_RIGHT
                if self.look == "D":
                    self.look = "R"
                    return Agent.Action.TURN_LEFT
                else:
                    self.todo.remove(xy)
                    self.setCord()
                    return Agent.Action.FORWARD

            if xy == (self.x,self.y-1):
                if self.look == "R":
                    self.look ="D"
                    return Agent.Action.TURN_RIGHT
                if self.look == "L":
                    self.look = "D"
                    return Agent.Action.TURN_LEFT
                if self.look == "U":
                    self.look = "L"
                    return Agent.Action.TURN_LEFT
                else:
                    self.todo.remove(xy)
                    self.setCord()
                    return Agent.Action.FORWARD

            if xy == (self.x,self.y+1):
                if self.look == "L":
                    self.look ="U"
                    return Agent.Action.TURN_RIGHT
                if self.look == "R":
                    self.look = "U"
                    return Agent.Action.TURN_LEFT
                if self.look == "D":
                    self.look = "R"
                    return Agent.Action.TURN_LEFT
                else:
                    self.todo.remove(xy)
                    self.setCord()
                    return Agent.Action.FORWARD   
        # ======================================================================
        # YOUR CODE ENDS
        # ======================================================================
    
    # ======================================================================
    # YOUR CODE BEGINS
    # ======================================================================
    def setCord(self):
        self.lastx = self.x
        self.lasty = self.y
        if self.look == "R":
            self.x = self.x+1
            self.y = self.y
        if self.look == "U":
            self.x = self.x
            self.y = self.y+1
        if self.look == "L":
            self.x = self.x-1
            self.y = self.y
        if self.look =="D":
            self.x = self.x
            self.y = self.y-1

    def calculateWayBack(self, x, y, goalx, goaly):
        graph = defaultdict(set)
        start = (x,y)
        goal = (goalx, goaly)
        for i in self.safepit:
                if (i[0]+1, i[1]) in self.safepit:
                        graph[i].add((i[0]+1, i[1]))
                if (i[0]-1, i[1]) in self.safepit:
                        graph[i].add((i[0]-1, i[1]))
                if (i[0], i[1]+1) in self.safepit:
                        graph[i].add((i[0], i[1]+1))
                if (i[0], i[1]-1) in self.safepit:
                        graph[i].add((i[0], i[1]-1))
        explored = []
        queue = [[start]]
        while queue:
        # pop the first path from the queue
                path = queue.pop(0)
        # get the last node from the path
                node = path[-1]
                if node not in explored:
                    neighbours = graph[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
                    for neighbour in neighbours:
                        new_path = list(path)
                        new_path.append(neighbour)
                        queue.append(new_path)
                # return path if neighbour is goal
                        if neighbour == goal:
                            return new_path[1:]
            # mark node as explored
                    explored.append(node)
    
    def addPits(self):
        self.potentialpit.append((self.x+1,self.y))
        self.potentialpit.append((self.x,self.y+1))
        self.potentialpit.append((self.x-1,self.y))
        self.potentialpit.append((self.x,self.y-1))
        self.potentialpit = list(set(self.potentialpit))
        self.removePits()
                    
    def safePits(self):
        self.safepit.append((self.x+1,self.y))
        self.safepit.append((self.x,self.y+1))
        self.safepit.append((self.x-1,self.y))
        self.safepit.append((self.x,self.y-1))
        self.safepit = list(set(self.safepit))
        self.removePits()

    def removeEdges(self, alist, name):
        if name == 'pp':
            for x in alist:
                if x[0] == 0:
                    self.potentialpit.remove(x)
                elif x[1] == 0:
                    self.potentialpit.remove(x)
                elif x[0] == self.sizex+1:
                    self.potentialpit.remove(x)
                elif x[1] == self.sizey+1:
                    self.potentialpit.remove(x)

        elif name == 'sp':
            for x in alist:
                if x[0] == 0:
                    self.safepit.remove(x)
                elif x[1] == 0:
                    self.safepit.remove(x)
                elif x[0] == self.sizex+1:
                    self.safepit.remove(x)
                elif x[1] == self.sizey+1:
                    self.safepit.remove(x)
        elif name == 'wp':
            for x in alist:
                if x[0] == 0:
                    self.potentialwumpus.remove(x)
                elif x[1] == 0:
                    self.potentialwumpus.remove(x)
                elif x[0] == self.sizex+1:
                    self.potentialwumpus.remove(x)
                elif x[1] == self.sizey+1:
                    self.potentialwumpus.remove(x)
        else:
            for x in alist:
                if x[0] == 0:
                    self.visited.remove(x)
                elif x[1] == 0:
                    self.visited.remove(x)
                elif x[0] == self.sizex+1:
                    self.visited.remove(x)
                elif x[1] == self.sizey+1:
                    self.visited.remove(x)

    def removePits(self):               
        for x in self.visited:
            if x not in self.safepit:
                self.safepit.append(x)
        for x in self.safepit:
            if x in self.potentialpit:
                self.potentialpit.remove(x)
            if x in self.potentialwumpus:
                self.potentialwumpus.remove(x)
        self.removeEdges(self.potentialwumpus, 'wp')
        self.removeEdges(self.potentialpit, 'pp')
        self.removeEdges(self.safepit, 'sp')
        self.removeEdges(self.visited, 'v')
    
    # ======================================================================
    # YOUR CODE ENDS
    # ======================================================================

