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
  for i in range(len(board)):
    print(dboard_1)
    print(dboard_2)
    print(dboard_n + str(board[i][0]) + nmark +
          dboard_n + str(board[i][1]) + nmark +
          dboard_n + str(board[i][2]) + nmark +
          dboard_n)
    print(dboard_2)
  print(dboard_1)
    

def enter_move(board):
  # The function accepts the board's current status, asks the user about their move, 
  # checks the input, and updates the board according to the user's decision.
  #print('*****Player move*****')
  pmove = None
  
  try:
    pmove = int(input('Enter your move: '))
    
    if pmove < 1 or pmove > 9:
      print('Enter a number between 1 and 9')
      pmove = None
      enter_move(board)
      
  except ValueError:
    print('Enter a number between 1 and 9')
    pmove = None
    enter_move(board)
    
  while pmove != None:
    flist = make_list_of_free_fields(board)
    
    for i in range(len(flist)):
      c1 = flist[i][0]
      c2 = flist[i][1]
      
      if board[c1][c2] == pmove:
        board[c1][c2] = pmark
        return display_board(board)
      
      elif i == len(flist) - 1:
        print('Enter a different number between 1 and 9')
        pmove = None
        enter_move(board)        
  else:
    return

def make_list_of_free_fields(board):
  # The function browses the board and builds a list of all the free squares; 
  # the list consists of tuples, while each tuple is a pair of row and column numbers.
  tlist = []
  
  for row in range(len(board)):
    
    for col in range(len(board[row])):
      
      if type(board[row][col]) == int:
        t = (row, col)
        tlist.append(t)
      
  return tlist

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    v = None

    while v == None:
      for row in board:
        if row.count(sign) == 3:
          print('horizontal')
          print(sign, 'WON!')
          v = True          
          return v
        
      if (
        board[0][0] == sign and board[1][0] == sign and board[2][0] == sign or
        board[0][1] == sign and board[1][1] == sign and board[2][1] == sign or
        board[0][2] == sign and board[1][2] == sign and board[2][2] == sign
        ):
        print('vertical')
        print(sign, 'WON!')
        v = True
      elif (
        board[0][0] == sign and board[1][1] == sign and board[2][2] == sign or
        board[2][0] == sign and board[1][1] == sign and board[0][2] == sign
        ):
        print('diagonal')
        print(sign, 'WON!')
        v = True
      else:
        v = False

    return v

def draw_move(board):
  # The function draws the computer's move and updates the board.
  #print('*****Computer move*****')
  cmove = randrange(1, 10)
  flist = make_list_of_free_fields(board)

  if (1, 1) in flist:
    board[1][1] = cmark
    return display_board(board)
  elif len(flist) == 1:
    print('FINAL MOVE')
    c1 = flist[0][0]
    c2 = flist[0][1]
    board[c1][c2] = cmark
    return display_board(board)

  # print('Computer chooses:', cmove)
  for i in range(len(flist)):
    c1 = flist[i][0]
    c2 = flist[i][1]
    
    if board[c1][c2] == cmove:
      board[c1][c2] = cmark
      return display_board(board)
    
    elif i == len(flist) - 1:
      draw_move(board)
      
rounds = 0
winner = False

while winner == False:
  rounds += 1
  print('ROUND#', rounds)
  draw_move(board)
  if rounds >= 3:
    winner = victory_for(board, cmark)
    print('computer', winner)
  if winner == False:
    enter_move(board)
    if rounds >= 3:
      winner = victory_for(board, pmark)
      print('player', winner)
