# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 12:40:01 2015
2-d maze using recurssion 
@author: Tadeze
"""

#track the starting points
import Queue
class Maze:
    maze=[]
    def __init__(self,size,nblock,inf="2-D maze"):
        self.info=inf
        self.generateMaze(size,nblock)
    def generateMaze(self,size,nblock=None):
        import random
        self.maze=[[0]*size for i in range(size)]
        start=[random.choice(range(size)),random.choice(range(size))]
        end=start    
        self.maze[start[0]][start[1]] = 'S'
        while end==start:
            end=[random.choice(range(size)),random.choice(range(size))]
        self.maze[end[0]][end[1]]='E'    
        nblock=nblock if nblock!=None else int(size*size/4)
        while(nblock>0):
            block=[random.choice(range(size)),random.choice(range(size))]
            if self.maze[block[0]][block[1]]==0:
                self.maze[block[0]][block[1]] ='*'
                nblock-=1
        self.size=(size,size)
    def get_maze(self):
        return self.maze
    def size(self):
        return self.size

    
class Exploremaze:
    visited=[]
    dfs_visited=[]
    bfs_visited=[]    
    def __init__(self,maze):
            self.maze = maze
             
    def exploreMaze(self,x,y):
        #If the maze is out of grid return false
        if x>self.maze.size[0]-1 or y<0 or x<0 or y>self.maze.size[1]-1:
            return False 
        if self.maze.maze[x][y]=='*' or self.maze.maze[x][y]=='#': return False  #we cann't move any more
        
        # if we reach the end        
        if self.maze.maze[x][y]=='E': return True
        isvisited = lambda x,y: (x,y) in self.visited
        if isvisited(x,y): return False
       #self.maze[x][y]="#"
        self.visited.append((x,y))
        if self.exploreMaze(x-1,y): return True
        if self.exploreMaze(x+1,y): return True
        if self.exploreMaze(x,y-1): return True
        if self.exploreMaze(x,y+1): return True
        
        return False
     
    def isMazesolvable(self):
        start=[]
        start=[(self.maze.maze.index(row),row.index(cell)) for row in self.maze.maze for cell in row if cell=='S']
        if len(start)==0:
            return False
        else:
            self.dfs(start[0][0],start[0][1])
            self.bfs(start[0][0],start[0][1])
            self.exploreMaze(start[0][0],start[0][1])
            return True
   #Explore to four direction
    def displayMaze(self,maze):
        for i in range(maze.size[0]):
            for j in range(maze.size[1]):
                print maze.maze[i][j],
            print "\n"
    def displayRout(self,visited):
        import copy
        maze=copy.deepcopy(self.maze)
        for path in visited[1:]:
            maze.maze[path[0]][path[1]]="#"
        self.displayMaze(maze)   
        print len(visited)
    def dfs(self,x,y):
        s=[]
        s.append((x,y))
        while(len(s)>0):
            top=s.pop()
            x,y=top
            if x>=self.maze.size[0] or x<0 or y>= self.maze.size[1] or y<0:continue
                
            if self.maze.maze[x][y]=='*': continue
            
            if top not in self.dfs_visited:
                if self.maze.maze[x][y]=='E': return True
                self.dfs_visited.append(top)
                s.append((x+1,y))
                s.append((x-1,y))
                s.append((x,y+1))
                s.append((x,y-1))
        return False
    
    def bfs(self,x,y):
        q=Queue.Queue()
        q.put((x,y))
        #self.bfs_visited.append((x,y))
        while q.empty()==False:
            top=q.get()
            x,y=top
            if  x>=self.maze.size[0] or x<0 or y>= self.maze.size[1] or y<0:continue
            if self.maze.maze[x][y]=='*': continue
            if top not in self.bfs_visited:
                if self.maze.maze[x][y]=='E': return True
                self.bfs_visited.append(top)
                q.put((x+1,y))
                q.put((x-1,y))
                q.put((x,y+1))
                q.put((x,y-1))   
                        
            
         
         
         
         
if __name__=="__main__":
    maze = Maze(8,336)
   # maze.generateMaze(8,36)
    maze_solver=Exploremaze(maze)
    maze_solver.displayMaze(maze)
    print "Solvable" if maze_solver.isMazesolvable() else "I cann't solve it"
    print"---------Greedy-------------------------------\n"  
    maze_solver.displayRout(maze_solver.visited)
    print"---------DFS-------------------------------\n"     
    maze_solver.displayRout(maze_solver.dfs_visited)
    print"---------BFS-------------------------------\n"     
    maze_solver.displayRout(maze_solver.bfs_visited)
    #maze_solver.displayRout()
    