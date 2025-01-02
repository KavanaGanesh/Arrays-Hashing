# Algorithm: 3 conditions to consider and check
# case1:validations of rows
    # create a set - that helps to store non duplicate values fo each rows
    # loop through each element in the sudoko (i,j) - 2 dimensional
    # represent the item in the board
    # if the item in set return False else item!='.' ->add the item to set
# case2:validations of columns
    # create a set - that helps to store non duplicate values fo each column
    # loop through each element in the sudoko (i,j) - 2 dimensional
    # represent the item in the board
    # if the item in set return False else item!='.' ->add the item to set
# case3:validations of subgrid -  tottally 9 subgrids
    # make a 2 dimensional subgrid [(start of each subgrid i.e i,j values)] as a list
    # create a set - that helps to store non duplicate values fo each subgrid
    # loop through each subgrid for rows
        # loop through each subgrid for columns
        # create an item for the board-> item = board[row][columns]
        # if the item in set return False else item!='.' ->add the item to set

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #validation of rows

        for i in range(9):
            s = set() # for each row you will need a new set 
            # set helps to store non - duplicate value 
            for j in range(9):
                item = board[i][j]
                if item in s:
                    return False
                elif item!='.':
                    s.add(item)

        for i in range(9):
            s = set() # for each row you will need a new set 
            # set helps to solves the duplicate value
            for j in range(9):
                item = board[j][i]
            if item in s:
                return False
            elif item!='.':
                s.add(item)

        # validation of subgrids:
        # zero indexing in python (x,y - like a start for a 2 dimensional)
        sub_grid = [(0,0),(0,3),(0,6),
                    (3,0),(3,3),(3,6),
                    (6,0),(6,3),(6,6)]
        for i,j in sub_grid:
            s = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    item = board[row][col]
                    if item in s:
                        return False
                    if item!='.':
                        s.add(item)

        return True
    
# case1: True
# board = \
# [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","8",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]

# case2:False
board = \
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
print(Solution().isValidSudoku(board))