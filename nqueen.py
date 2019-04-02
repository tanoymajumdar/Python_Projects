# Put your testing code here
# This function will be executed when you run your program on VPL
# This function will not be graded

def main():
    queen=[0,1,2,3,4,5,6,7]
    print(solve(queen, 5000))
    

#Task 1.1
def countAttack(queen):
    count = 0
    i = 0
    while(i<len(queen)-1):
        j = i+1
        while(j<len(queen)):
            if(queen[i] == queen[j]):
                count=count+1
            if(abs(queen[i] - queen[j]) == (j-i)):
                count=count+1
            j=j+1
        i= i+1
    return(count)
    

#Task 1.2
def getNext(queen):
    bestQueen = list(queen)
    length = len(queen)
    mincost = len(queen)*len(queen)
    result=queen
    for i in range(0,len(queen)):
        tempQueen = list(queen)
        for j in range(0, len(bestQueen)):
            if(bestQueen[i] == j):
                continue
          
            else:
                tempQueen[i] = j
                if(countAttack(tuple(tempQueen)) < mincost):
                    mincost = countAttack(tuple(tempQueen))
                    result = tuple(tempQueen)
    return result
  
#Task 1.3
def solve(queen, n):
    solution = queen
    arr=[]
    arr.append(solution)
    count=0
    while(countAttack(solution)!=0 and count<n):
        count+=1
        arr.append(getNext(solution))
        solution = getNext(solution)
    return(arr)
def printBoard(queen):
    for n in queen:
        print("- "*n+"Q"+" -"*(len(queen)-n-1))