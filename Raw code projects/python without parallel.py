result = []
n = 4
#board = [[0,0,1,0],[0,1,0,0],[0,0,0,1],[1,0,0,0]]
board = [[0 for j in range(n)] for i in range(n)]

#backtracking algortihm:
'''1) Start in the leftmost column
2) If all queens are placed
    return true
3) Try all rows in the current column.  Do following
   for every tried row.
    a) If the queen can be placed safely in this row
       then mark this [row, column] as part of the 
       solution and recursively check if placing  
       queen here leads to a solution.
    b) If placing queen in [row, column] leads to a
       solution then return true.
    c) If placing queen doesn't lead to a solution 
       then unmark this [row, column] (Backtrack) 
       and go to step (a) to try other rows.
3) If all rows have been tried and nothing worked, 
   return false to trigger backtracking.'''

def CheckRow(all):
    curBoard = board
    x = all[0]
    y = all[1]

    for i in range(n):
        if(y != i):
            if(curBoard[x][i] == 1):
                return False
    return True

def CheckCol(all):
    curBoard = board
    x = all[0]
    y = all[1]
    
    for i in range(n):
        if(x!=i):
            if(curBoard[i][y]==1):
                print(i,y)
                return False
    return True

def CheckDiag(all):
    curBoard = board
    x = all[0]
    y = all[1]

    x1 = x
    x2 = x
    y1 = y
    y2 = y
    for i in range(n):
        x1+=1
        x2-=1
        y1+=1
        y2-=1
        if(x1<n and y1<n):
            if (curBoard[x1][y1]==1):
                return False
        if(x2>=0 and y1<n):
            if (curBoard[x2][y1]==1):
                return False
        if(x1<n and y2>=0):
            if (curBoard[x1][y2]==1):
                return False
        if(x2>=0 and y2>=0):
            if (curBoard[x2][y2]==1):
                return False
    return True

def Solve(board, col, n):

    if (col == n):
        v = []
        for i in board:
          for j in range(len(i)):
            if i[j] == 1:
              v.append(j+1)
        result.append(v)
        return True
    res = False

    for i in range(n):
        c1 = CheckRow([i, col])
        c2 = CheckCol([i, col])
        c3 = CheckDiag([i, col])
        if(c1 and c2 and c3):
            board[i][col] = 1
            res = Solve(board, col + 1, n) or res
            board[i][col] = 0
    return res
        
Solve(board, 0, n)
print(f"Result:{result}")
