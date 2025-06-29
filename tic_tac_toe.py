'''
# the computer should play the game using 'X's

# the user should play the game using 'O's

# first move belongs to the computer - it always puts the first 'x' in the middle of the board

# all squares are numbered row by row starting with 1

# the user inputs move by entering the number of the square. the number must be valid
# must be an integer greater than 0 and less than 10
# cannot point to a field that's been occupied

# the program checks if the game is over. there are four possible verdicts
# 1. the game should continue
# 2. the game ends with a tie
# 3. you win
# 4. the computer wins

# the computer responds with it's move and the check is repeated

# a random choice made by the computer is good enough for the game
'''
# Requirements

# the board should be stored as a three-element list, while each element is another three-element list
# (the inner lists represent rows) so that all of the squares may be accessed using the following syntax
'''
  board[row][column]
'''

# each of the inner list's elements can contain 'O', 'X' or a digit representing the square's number

# the boards appearance should be exactly the same as the example
'''
+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Enter your move: 1
'''

# implement the functions defined in the editor

# drawing a random integer number can be done by utilizing a Python function called randrange()
'''
from random import randrange

for i in range(10):
  print(randrange(8))
'''
from random import randrange

cmark = 'X'
pmark = 'O'
nmark = '   '

board = [
          [1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]
        ]

dboard_1 = '+-------+-------+-------+'
dboard_2 = '|       |       |       |'
dboard_n = '|   '

def display_board(board):
  # The function accepts one parameter containing the board's current status
  # and prints it out to the console.
  print(board)
  for i in range(3):
    print(dboard_1)
    print(dboard_2)
    print(dboard_n + str(board[i][0]) + nmark + dboard_n + str(board[i][1]) + nmark + dboard_n + str(board[i][2]) + nmark + dboard_n)
    print(dboard_2)
  print(dboard_1)
    

def enter_move(board):
  # The function accepts the board's current status, asks the user about their move, 
  # checks the input, and updates the board according to the user's decision.
  pmove = None
  try:
    pmove = int(input('Enter a move: '))
    if pmove < 1 or pmove > 9:
      print('Enter an number between 1 and 9')
      enter_move(board)
  except ValueError:
    print('Enter an number between 1 and 9')
    enter_move(board)
    
  for i in range(3):
    if pmove in board[i]:
      index = board[i].index(pmove)
      board[i][index] = pmark
'''
def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


def draw_move(board):
    # The function draws the computer's move and updates the board.
'''
enter_move(board)
display_board(board)
enter_move(board)
display_board(board)
enter_move(board)
display_board(board)
