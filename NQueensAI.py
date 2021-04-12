import numpy as np
from copy import deepcopy
from math import exp


class Chess:
    def __init__(self,n):
        self.n = n
        self.board = []
        #trạng thái khởi tạo
        for i in range(n):
            self.board.append(i)

    def checkOneQueenDown(self, i):
        for j in range(i+1,self.n):
            if (self.board[j]==self.board[i]): return False
            if ((self.board[j]-j)==(self.board[i]-i)): return False
            if ((self.board[j]+j)==(self.board[i]+i)): return False
        return True

    #Hàm check trạng thái mục tiêu
    def checkGoal(self):
        for i in range(self.n):
            if self.checkOneQueenDown(i)==False: return False
        return True

    #giải thuật DFS
    def DFS(self, deep):
        if (deep < self.n-1):
            for i in range(0,self.n):
                if self.checkGoal():
                    return 0
                self.board[deep]=(self.board[deep]+1) % self.n
                if self.checkGoal():
                    return 0
                else: 
                    self.DFS(deep+1)
        else: 
            for i in range(0,self.n):
                self.board[deep]=(self.board[deep]+1) % self.n
                if self.checkGoal():
                    return 0
    
    #giải thuật BrFS
    def BrFS(self, last_states, deep):
        for i in range (self.n**deep):
            self.board = last_states[i]
            if self.checkGoal():
                print(deep)
                return 0
        new_states = []
        for i in range (self.n**deep):
            for j in range (self.n):
                last_states[i][j] = (last_states[i][j] + 1) % self.n
                new_states.append(deepcopy(last_states[i]))
                last_states[i][j] = (last_states[i][j] - 1) % self.n
        del last_states
        self.BrFS(new_states, deep+1)
        
    #giải thuật Heuristic: tôi luyện mô phỏng
    def SimulatedAnnealing(self):
        result = False
        last_f = f(self.board, self.n)
        t = 5000
        while t>0:
            t *= 0.99
            new_board = deepcopy(self.board)
            while True:
                index1 = np.random.randint(0, self.n)
                index2 = np.random.randint(0, self.n)
                if index1 != index2:
                    break
            new_board[index1], new_board[index2] = new_board[index2],new_board[index1]
            deltaE = f(new_board, self.n) - last_f
            if deltaE<0 or np.random.rand()<exp(-deltaE/t):
                self.board = deepcopy(new_board)
                last_f = f(self.board, self.n)
            if last_f == 0:
                result = True
                break
        if result == True:
            self.printBoard()
        else:
            print("Khong tim ra loi giai!!")

    def printBoard(self):
        print(self.board)

def fOneQueen(board, i, n):
    fault = 0
    for j in range(i+1,n):
        if (board[j]==board[i]): fault+=1
        if ((board[j]-j)==(board[i]-i)): fault+=1
        if ((board[j]+j)==(board[i]+i)): fault+=1
    return fault
    
def f(board, n):
        result = 0
        for i in range(n):
            result += fOneQueen(board, i, n)
        return result


n = int(input("Nhap n: "))
type_search = int(input("Nhap kieu search ban mong muon\n1 neu DFS\n2 neu BrFS\n3 neu heuristic search :  "))
myChess=Chess(n)
if type_search == 1 and n>3:
    myChess.DFS(0)
    myChess.printBoard()
    del myChess
elif type_search == 2 and n>3:
    myChess.BrFS([myChess.board],0)
    myChess.printBoard()
elif type_search == 3 and n>3:
    myChess.SimulatedAnnealing()
else:
    print("Nhap sai n hoac kieu seach!!!")