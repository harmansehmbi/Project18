# n-Queen problem....

# 1. Creating a Chess Board

""""

       1 0 1 0 1 0 1 0
       0 1 0 1 0 1 0 1
       1 0 1 0 1 0 1 0
       0 1 0 1 0 1 0 1
       1 0 1 0 1 0 1 0
       0 1 0 1 0 1 0 1
       1 0 1 0 1 0 1 0
       0 1 0 1 0 1 0 1

"""

import numpy as np

import datetime as dt

chessBoard = np.zeros((8, 8), dtype=int)
print(chessBoard)


stamp1 = dt.datetime.today()


print()

# Slicing And Substitution
chessBoard[1::2, ::2] = 1
chessBoard[::2, 1::2] = 0

stamp2 = dt.datetime.today()
print("Time taken to create stamp2: ", stamp2 - stamp1)

print(chessBoard)

# 2. Ask the User to place 4 Queens on chessBoard
# Where to place 1st Queen : 2,3
# Where to place 2st Queen : 5,4
# Where to place 3st Queen : 1,1
# Where to place 4st Queen : 7,7
# and substitute 9 over there

"""
       1 0 1 0 1 0 1 0
       0 9 0 1 0 1 0 1
       1 0 1 9 1 0 1 0
       0 1 0 1 0 1 0 1
       1 0 1 0 1 0 1 0
       0 1 0 1 9 1 0 1
       1 0 1 0 1 0 1 0
       0 1 0 1 0 1 0 9


"""

# queenPosition = input("Where to place 1st Queen : " )
# chessBoard[][] = ?

print()

queenPosition = input("Where to place 1st Queen : " )
i = int(queenPosition[0])
j = int(queenPosition[2])

chessBoard[i][j] = 9
print(chessBoard)

print()

# 3. Validate if a queen is available in the same row or same column.
# give a message to the user to enter some other position



# 4. Validate if a queen is available in the same diagonal.
# give a message to the user to enter some other position