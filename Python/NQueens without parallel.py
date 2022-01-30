result = []

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

    def CheckRow(curBoard, x, y):
        for i in range(n):
            if(y!=i):
                if(curBoard[x][i]==1):
                    return False
                '''else:
                    curBoard[x][i]=-1'''
        return True
    
    def CheckCol(curBoard, x, y):
        for i in range(n):
            if(x!=i):
                if(curBoard[i][y]==1):
                    print(i,y)
                    return False
                '''else:
                    curBoard[i][y] = -2'''
        return True

    def CheckDiag(curBoard, x,y):

        #print(f"x:{x}, y:{y}")
        x1 = x
        x2 = x
        y1 = y
        y2 = y
        for i in range(n):
            x1+=1
            x2-=1
            y1+=1
            y2-=1
            #print(f"Diag i:{i}")
            if(x1<n and y1<n):
                if (curBoard[x1][y1]==1):
                    return False
                '''else:
                    curBoard[x1][y1] = -3'''
            if(x2>=0 and y1<n):
                if (curBoard[x2][y1]==1):
                    return False
                '''else:
                    curBoard[x2][y1] = -3'''
            if(x1<n and y2>=0):
                if (curBoard[x1][y2]==1):
                    return False
                '''else:
                    curBoard[x1][y2] = -3'''
            if(x2>=0 and y2>=0):
                if (curBoard[x2][y2]==1):
                    return False
                '''else:
                    curBoard[x2][y2] = -3'''
        return True
            
    for i in range(n):
        print(len(board), " ", col)
        c1 = CheckRow(board, i, col)
        c2 = CheckCol(board, i, col)
        c3 = CheckDiag(board, i, col)
        if(c1 and c2 and c3):
            board[i][col] = 1
            res = Solve(board, col + 1, n) or res
            board[i][col] = 0
    return res
        
n = 6
#board = [[0,0,1,0],[0,1,0,0],[0,0,0,1],[1,0,0,0]]
board = [[0 for j in range(n)] for i in range(n)]
Solve(board, 0, n)
print(board)
print(f"Result:{result}")
'''
0 0 1 0
0 1 0 0
0 0 0 1
1 0 0 0
'''
