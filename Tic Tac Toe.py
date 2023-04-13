import random
import os

# Clean the terminal
os.system('cls' if os.name == 'nt' else 'clear')

print('--------------------------------')
print("Hello!   Welcome to Tic Tac Toe game in which two players seek in alternate turns to \ncomplete a row, a column, or a diagonal with either three 'O's or three 'X's drawn in \nthe spaces of a grid of nine squares; noughts and crosses.\n\nDecide together who of you is a Player1 and who is Player2.")
print('--------------------------------')

#=========================================================================================================================================

# Returns which player is 'X' and which is 'O'
def player_draw(who_starts):
  p = player_x_or_o(input(f"Player{who_starts}, do you want to be 'X' or 'O'?: ").upper())
  if who_starts == 1:
    return p
  elif who_starts == 2:
    return 'X' if p == 'O' else 'O'
    
# Player chooses by input whether he wants to be 'X or 'O'
def player_x_or_o(x_or_o):
  while x_or_o not in ['X', 'O']:
    x_or_o = input(f"Player{who_starts}, please pick a marker 'X' or 'O': ").upper()
  return x_or_o

#====================================================================
# Main game, player choose the position he want to mark by selecting a number from 1 to 9 until one player wins or draw AND asks for restart the game
def game(who_choose, player1, player2):
  game_board = """   |   |   
   |   |   
   |   |   """   
  players_choices = []
  who_win = ''
  while True:
    p = input(f"Player{who_choose}, choose the position you want to mark by selecting a number from '1' to '9': ")
    while p not in [str(x) for x in range(1,10)] or p in players_choices:
     p = input(f"Player{who_choose}, you have to choose a number (that has not been used before) from '1' to '9': ")
    players_choices.append(p)
    if who_choose == 1:
      game_board = update_game_board(int(p), game_board, player1)
      who_win = check_if_win(game_board)
      if who_win == True:
        who_win = who_choose
        break
      elif who_win == 'DRAW':
        break
      else:
        who_choose = 2
        continue
    elif who_choose == 2:
      game_board = update_game_board(int(p), game_board, player2)
      who_win = check_if_win(game_board)
      if who_win == True:
        who_win = who_choose
        break
      elif who_win == 'DRAW':
        break
      else:
        who_choose = 1
        continue
  if who_win == 'DRAW':
    print(f'\n# ITS A {who_win}! #\n')
  else:
    print(f'\n *^*^*^*^ Player{who_win} WINS! *^*^*^*^*^\n')   
  restart_question = ''
  while restart_question not in ['Y', 'N']:
    restart_question = input("Do you want to play again? Enter 'Y' or 'N': ").upper()
  if restart_question == 'Y':
    return True
  elif restart_question == 'N':
    return False 
#====================================================================

# Updates the player's mark at the position he entered, clean terminal and print updated game board  
def update_game_board(p, game_board, players_mark):
  if p == 1:
    game_board = game_board[:1] + players_mark + game_board[2:]
  elif p == 2:
    game_board = game_board[:5] + players_mark + game_board[6:]
  elif p == 3:
    game_board = game_board[:9] + players_mark + game_board[10:]
  elif p == 4:
    game_board = game_board[:13] + players_mark + game_board[14:]
  elif p == 5:
    game_board = game_board[:17] + players_mark + game_board[18:]
  elif p == 6:
    game_board = game_board[:21] + players_mark + game_board[22:]
  elif p == 7:
    game_board = game_board[:25] + players_mark + game_board[26:]
  elif p == 8:
    game_board = game_board[:29] + players_mark + game_board[30:]
  elif p == 9:
    game_board = game_board[:33] + players_mark + game_board[34:]
  os.system('cls' if os.name == 'nt' else 'clear')
  print('--------------------------------')
  print(game_board)
  return game_board

# Checks if any of the players has won OR if there is a draw
def check_if_win(game_board):
  row1 = game_board[1] + game_board[5] + game_board[9]
  row2 = game_board[13] + game_board[17] + game_board[21]
  row3 = game_board[25] + game_board[29] + game_board[33]
  col1 = game_board[1] + game_board[13] + game_board[25]
  col2 = game_board[5] + game_board[17] + game_board[29]
  col3 = game_board[9] + game_board[21] + game_board[33]
  x1 = game_board[1] + game_board[17] + game_board[33]
  x2 = game_board[25] + game_board[17] + game_board[9]
  if row1.count('X') == 3 or row1.count('O') == 3:
    return True
  elif row2.count('X') == 3 or row2.count('O') == 3:
    return True
  elif row3.count('X') == 3 or row3.count('O') == 3:
    return True
  elif col1.count('X') == 3 or col1.count('O') == 3:
    return True
  elif col2.count('X') == 3 or col2.count('O') == 3:
    return True
  elif col3.count('X') == 3 or col3.count('O') == 3:
    return True
  elif x1.count('X') == 3 or x1.count('O') == 3:
    return True
  elif x2.count('X') == 3 or x2.count('O') == 3:
    return True
  elif ' ' not in [game_board[1], game_board[5], game_board[9], game_board[13], game_board[17], game_board[21], game_board[25], game_board[29], game_board[33]]:
    return 'DRAW'
  else:
    return False
  
#=========================================================================================================================================

who_starts = random.randint(1,2)

player1 = player_draw(who_starts)
player2 = 'X' if player1 == 'O' else 'O'

os.system('cls' if os.name == 'nt' else 'clear')
print('--------------------------------')
print("""Here is a board with marked positions from 1 to 9:
 1 | 2 | 3 
 4 | 5 | 6 
 7 | 8 | 9
 """) 

# The loop runs as long as players want to play
while game(who_starts, player1, player2) == True:
  who_starts = random.randint(1,2)
  os.system('cls' if os.name == 'nt' else 'clear')
  print('--------------------------------')
  print("""   |   |   
   |   |   
   |   |   """)

print('Thank you for playing! :)\n')