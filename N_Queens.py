class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [[0] * n for _ in range(n)]
        self.solutions = []

    def is_safe(self, row, col):
        # Check if there is a queen in the same column
        for i in range(row):
            if self.board[i][col] == 1:
                return False

        # Check upper left diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        # Check upper right diagonal
        for i, j in zip(range(row, -1, -1), range(col, self.n)):
            if self.board[i][j] == 1:
                return False

        return True

    def solve(self, row):
        if row == self.n:
            self.solutions.append([row[:] for row in self.board])
            return

        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = 1
                self.solve(row + 1)
                self.board[row][col] = 0

    def display_solutions(self):
        for solution in self.solutions:
            for row in solution:
                print(" ".join("Q" if cell == 1 else "-" for cell in row))
            print()

# Example usage
n = 4
n_queens = NQueens(n)
n_queens.solve(0)
n_queens.display_solutions()

# class Queens:
#     def __init__(self,n):
#         self.n = n
#         self.board = [[0]*n for i in range(n)]
#         self.solu = []

#     def is_safe(self,row,col):
#         for i in range(row):
#             if self.board[i][col] ==1:
#                 return False
            
#         for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
#             if self.board[i][j] == 1:
#                 return False
        
#         for i,j in zip(range(row,-1,-1), range(col,self.n)):
#             if self.board[i][j] == 1:
#                 return False
            
#         return True

#     def solve(self,row):
#         if self.n ==row:
#             self.solu.append([row[:] for row in self.board])
#             return
        
#         for col in range(self.n):
#             if self.is_safe(row,col):
#                 self.board[row][col] = 1
#                 self.solve(row+1)
#                 self.board[row][col] = 0

#     def display(self):
#         for solu in self.solu:
#             for row in solu:
#                 print(" ".join("Q" if cell ==1 else "-" for cell in row))
#             print()

# n = 4
# nq = Queens(n)
# nq.solve(0)
# nq.display()