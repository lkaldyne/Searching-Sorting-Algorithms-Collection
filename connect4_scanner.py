''' 
The following code uses preprocessing and scanning techniques to
check for winners in Connect-4. Board can be of any dimensions,
and zeros can be replaced with any character or int. This code was
made with the intention of being added to the back end of an upcoming
Connect-4 project.
'''  

board = [[0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,1,0,0,0,0,0],
         [0,0,1,0,0,0,0],
         [0,0,0,1,0,0,0],
         [0,0,0,0,1,0,0]]

def generateHorizontal(l,w,c):
    results = [[]] * ((w - c + 1) * l)
    resultAppendSpot = 0
    for i in range(w - c + 1):
         for j in range(l):
            groupedResults = [[j,x] for x in range(i,i+c)]
            results[resultAppendSpot] = groupedResults
            resultAppendSpot += 1
    return results 
            
def generateVertical(l,w,c):
    results = [[]] * ((l - c + 1) * w)
    resultAppendSpot = 0
    for i in range(l - c + 1):
         for j in range(w):
            groupedResults = [[x,j] for x in range(i,i+c)]
            results[resultAppendSpot] = groupedResults
            resultAppendSpot += 1
    return results 

def generateDiag(l,w,c):
    results = []
    for y in range(c-1,l):
         for x in range(w - c + 1):
            groupedResults = [[]] * c
            groundIncr = 0
            for x1 in range(x,x+c):
                groupedResults[groundIncr] = [y-groundIncr,x1]
                groundIncr += 1
            results.append(groupedResults)
    
    for y in range(l-c,0,-1):
         for x in range(w - c + 1):
            groupedResults = [[]] * c
            groundIncr = 0
            for x1 in range(x,x+c):
                groupedResults[groundIncr] = [y+groundIncr,x1]
                groundIncr += 1
            results.append(groupedResults)
    return results 

def generateCombinations(l,w,c):
    return generateHorizontal(l,w,c) + generateVertical(l,w,c) + generateDiag(l,w,c)

def checkForWinner(combinations):
    for option in combinations:
        perfectMatch = True
        comparator = board[option[0][0]][option[0][1]]
        if comparator != 0:
            for i in range(1,len(option)):
                if board[option[i][0]][option[i][1]] != comparator:
                    perfectMatch = False
                    break
            if perfectMatch:
                print "Player %s wins!" %(comparator)
                return True
    return False
    
# All winning coordinate sets are generated for the desired connect4 board size
# This is a preprocessing phase and only needs to be done once, 
# results can be stored and used indefinitely afterwards.
# Typical connect4 boards have dimensions of 6 x 7
allOptions = generateCombinations(6,7,4)

#Checks for winners using generated coordinate sets
checkForWinner(allOptions)