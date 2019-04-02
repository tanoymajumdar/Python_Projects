# Put your testing code here
# This function will be executed when you run your program on VPL
# This function will not be graded
def main():
    puzzle = (3,1,8,2,4,5,6,0,7)
    print(evaluate(puzzle))
    
#Task 2.1
def evaluate(puzzle):
    sum=0
    for i in range (0, len(puzzle)):
        if(puzzle[i]!=0):
            rowlist= int(puzzle[i]/3)
            rowideal= int(i/3)
            columnlist= puzzle[i]%3
            columnideal=i%3
            sum+=(abs(rowlist-rowideal)+abs(columnlist-columnideal))
    return sum
    
#Task 2.2
def applyMove(puzzletuple, move):
    puzzle = list(puzzletuple)
    if(move=='down'):
        for i in range(0,len(puzzle)):
            if(puzzle[i]==0):
                row = int(i/3)
                column = (i%3)
                if(row!=0):
                    row-=1
                    puzzle[i]= puzzle[row*3+column]
                    puzzle[row*3+column] = 0
                    break
                    
    elif(move=='up'):
        for i in range(0,len(puzzle)):
            if(puzzle[i]==0):
                row = int(i/3)
                column = (i%3)
                if(row!=2):
                    row+=1
                    puzzle[i]= puzzle[row*3+column]
                    puzzle[row*3+column] = 0
                    break
                    
    elif(move=='left'):
        for i in range(0,len(puzzle)):
            if(puzzle[i]==0):
                column = (i%3)
                row = int(i/3)
                if(column!=2):
                    column+=1
                    puzzle[i]= puzzle[row*3+column]
                    puzzle[row*3+column] = 0
                    break
    elif(move=='right'):
        for i in range(0,len(puzzle)):
            if(puzzle[i]==0):
                column = (i%3)
                row = int(i/3)
                if(column!=0):
                    column-=1
                    puzzle[i]= puzzle[row*3+column]
                    puzzle[row*3+column] = 0
                    break
    return(tuple((puzzle)))
                
def astarTSA(initial_state):
    frontier = [initial_state]
    moves=[]
    answer=[]
    pathcost=[0]
    pc=0
    while len(frontier) > 0:
        t=10000000
        for i in range(0,len(frontier)):
            h=evaluate(frontier[i])+pathcost[i]
            if(h<t):
                t=h
                location=i
        z = frontier.pop(location)
        pathcost.pop(location)
        if(pc!=0):
            answer.append(moves.pop(location))        
        if(evaluate(z)!=0):
         pc+=1

         frontier.append(applyMove(z, 'up'))
         frontier.append(applyMove(z, 'down'))
         frontier.append(applyMove(z, 'left'))
         frontier.append(applyMove(z, 'right'))
         pathcost.append(pc)
         pathcost.append(pc)
         pathcost.append(pc)
         pathcost.append(pc)
         moves.append('up')
         moves.append('down')
         moves.append('left')
         moves.append('right')
        else:
            break
    return(answer)
    # choose a leaf node and remove it from frontier
    # if node contains a goal state, return corresponding solution
    # expand the node adding the resulting nodes to the frontier                
                

def printPuzzle(puzzle):
  for i in range(3):
    for j in range(3):
      print(puzzle[i*3+j], end=' ')
    print()










  
