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
        self.sizex = 99
        self.sizey = 99
        self.moves = 0
        # ======================================================================
        # YOUR CODE ENDS
        # ======================================================================

    def getAction( self, stench, breeze, glitter, bump, scream ):
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
                
        if (glitter):
                self.gold = True
                return Agent.Action.GRAB
        if (breeze):
            if (self.x, self.y) == (1,1):
                return Agent.Action.CLIMB
        self.moves += 1
        if (self.gold) or self.moves >= 150 or (self.moves >=35 and len(self.safepit) <= 5):
            if (self.x,self.y) == (1,1):
                return Agent.Action.CLIMB
            if not self.todo:
                self.todo = self.calculateWayBack(self.x,self.y)
        if (self.x,self.y) in self.todo:
            self.todo.remove(self.x,self.y)
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
            
        if (bump):
            if self.look == "R":
                self.sizex = self.x
                self.x = self.x-1
                self.look = "U"
                self.lastx = self.x
                self.lasty = self.y
                return Agent.Action.TURN_LEFT
            if self.look == "U":
                self.sizey = self.y
                self.y = self.y-1
                self.look = "L"
                self.lastx = self.x
                self.lasty = self.y
                return Agent.Action.TURN_LEFT
            if self.look == "L":
                self.x = self.x+1
                self.look = "D"
                self.lastx = self.x
                self.lasty = self.y
                return Agent.Action.TURN_LEFT
            if self.look =="D":
                self.y = self.y+1
                self.look = "R"
                self.lastx = self.x
                self.lasty = self.y
                return Agent.Action.TURN_LEFT
        if (scream):
            self.wumpus = True
            
        if (self.wumpus):
            stench = False
            self.potentialwumpus = []
            
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
            
        if (stench):
            self.potentialwumpus.append((self.x+1,self.y))
            self.potentialwumpus.append((self.x,self.y+1))
            self.potentialwumpus.append((self.x-1,self.y))
            self.potentialwumpus.append((self.x,self.y-1))
            self.potentialwumpus = list(set(self.potentialwumpus))
            if (self.arrow):
                self.arrow = False
                if self.look == "R":
                    self.potentialwumpus.remove((self.x+1,self.y))
                if self.look == "L":
                    self.potentialwumpus.remove((self.x-1,self.y))
                if self.look == "U":
                    self.potentialwumpus.remove((self.x,self.y+1))
                if self.look == "D":
                    self.potentialwumpus.remove((self.x,self.y-1))
                self.removePits()
                return Agent.Action.SHOOT
            
        if (breeze):
            if (self.x,self.y) == (1,1):
                return Agent.Action.CLIMB
            else:
                self.addPits()
        elif not stench:
            self.safePits()

        self.removePits()
        #Only move in safe spots and not visited unless we circled around
        if self.look == "R":
            if (self.ret): #if we are allowed to back to self.visited
                if (self.x+1,self.y) in self.safepit:
                    self.setCord()          
                    return Agent.Action.FORWARD
                else:
                    self.look = "U"
                    self.lastx = self.x
                    self.lasty = self.y
                    return Agent.Action.TURN_LEFT
            elif ((self.x+1,self.y) in self.safepit and (self.x+1,self.y) not in self.visited): #if we aren't
                self.setCord()
                return Agent.Action.FORWARD
            else:
                self.look = "U"
                self.lastx = self.x
                self.lasty = self.y
                return Agent.Action.TURN_LEFT
        if self.look == "L":
            if (self.ret): #if we are allowed to back to self.visited
                if (self.x-1,self.y) in self.safepit:
                    self.setCord()          
                    return Agent.Action.FORWARD
                else:
                    self.look = "D"
                    self.lastx = self.x
                    self.lasty = self.y
                    return Agent.Action.TURN_LEFT
            elif ((self.x-1,self.y) in self.safepit and (self.x-1,self.y) not in self.visited):
                self.setCord()
                return Agent.Action.FORWARD
            else:
                self.look = "D"
                self.lastx = self.x
                self.lasty = self.y
                return Agent.Action.TURN_LEFT
        if self.look == "U":
            if (self.ret): #if we are allowed to back to self.visited
                if (self.x,self.y+1) in self.safepit:
                    self.setCord()          
                    return Agent.Action.FORWARD
                else:
                    self.look = "L"
                    self.lastx = self.x
                    self.lasty = self.y
                    return Agent.Action.TURN_LEFT
            elif ((self.x,self.y+1) in self.safepit and (self.x,self.y+1) not in self.visited):
                self.setCord()
                return Agent.Action.FORWARD
            else:
                self.look = "L"
                self.lastx = self.x
                self.lasty = self.y
                return Agent.Action.TURN_LEFT
        if self.look =="D":
            if (self.ret): #if we are allowed to back to self.visited
                #print((self.x, self.y-1 in self.safepit))
                if (self.x,(self.y)-1) in self.safepit:
                    self.setCord()          
                    return Agent.Action.FORWARD
                else:
                    self.look = "R"
                    self.lastx = self.x
                    self.lasty = self.y
                    return Agent.Action.TURN_LEFT
            elif ((self.x,(self.y)-1) in self.safepit and (self.x,self.y-1) not in self.visited):
                self.setCord()
                return Agent.Action.FORWARD
            else:
                self.look = "R"
                self.lastx = self.x
                self.lasty = self.y
                return Agent.Action.TURN_LEFT
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

    def calculateWayBack(self,x ,y):
        oldx = x
        oldy = y
        stored = [(x,y)]
        bad = []
        while (x != 1 or y != 1):
            if (x,y-1) in self.safepit and (x,y-1) not in stored and (x,y-1) not in bad:
                y = y-1
                stored.append((x,y))
                if (x == 1 and y == 1):
                    break

            elif (x-1, y) in self.safepit and (x-1,y) not in stored and (x-1, y) not in bad:
                x = x-1
                stored.append((x,y))
                if (x == 1 and y == 1):
                    break

            elif (x+1, y) in self.safepit and (x+1, y) not in stored and (x+1,y) not in bad:
                x = x+1
                stored.append((x,y))
                if (x == 1 and y == 1):
                    break

            elif (x, y+1) in self.safepit and (x, y+1) not in stored and (x,y+1) not in bad:
                y = y+1
                stored.append((x,y))
                if (x == 1 and y == 1):
                    break
            else:
                bad.append(stored.pop()) 
                (x,y) = stored[-1]
        return stored[1:]
    
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
                elif x[0] == self.sizex:
                    self.potentialpit.remove(x)
                elif x[1] == self.sizey:
                    self.potentialpit.remove(x)

        elif name == 'sp':
            for x in alist:
                if x[0] == 0:
                    self.safepit.remove(x)
                elif x[1] == 0:
                    self.safepit.remove(x)
                elif x[0] == self.sizex:
                    self.safepit.remove(x)
                elif x[1] == self.sizey:
                    self.safepit.remove(x)
        elif name == 'wp':
            for x in alist:
                if x[0] == 0:
                    self.potentialwumpus.remove(x)
                elif x[1] == 0:
                    self.potentialwumpus.remove(x)
                elif x[0] == self.sizex:
                    self.potentialwumpus.remove(x)
                elif x[1] == self.sizey:
                    self.potentialwumpus.remove(x)
        else:
            for x in alist:
                if x[0] == 0:
                    self.visited.remove(x)
                elif x[1] == 0:
                    self.visited.remove(x)
                elif x[0] == self.sizex:
                    self.visited.remove(x)
                elif x[1] == self.sizey:
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

