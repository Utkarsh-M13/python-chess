board = []

# Initializes the starting board
def fillBoard(): 
  for i in range(8):
    board.append([])
    for j in range(8):
      
      square= ''
      
      # Assign pieces
      square = assignPiece(i, j)
        
      if (square != ''):
        board[i].append(square)
        continue
      
      # If a square has even row-col sum then white else black
      if ((i + j) % 2 == 0): square = 'X'
      else: square = 'O'
      
      board[i].append(square)
      
# Assigns pieces based on index
def assignPiece(i, j):
  square= ''
  if (i == 0 and j == 0) or (i == 0 and j == 7):
    square = 'R'
  
  if (i == 0 and j == 1) or (i == 0 and j == 6):
    square = 'N'
  
  if (i == 0 and j == 2) or (i == 0 and j == 5):
    square = 'B'
  
  if (i == 0 and j == 3):
    square = 'K'
  
  if (i == 0 and j == 4):
    square = 'Q'
  
  if (i == 7 and j == 0) or (i == 7 and j == 7):
    square = 'r'
  
  if (i == 7 and j == 1) or (i == 7 and j == 6):
    square = 'n'
  
  if (i == 7 and j == 2) or (i == 7 and j == 5):
    square = 'b'
  
  if (i == 7 and j == 3):
    square = 'k'
  
  if (i == 7 and j == 4):
    square = 'q'
  
  if i == 1:
    square = 'P'
  
  if i == 6:
    square = 'p'
  
  return square

# Prints the current state of the board
def printBoard():
  for i in range(8):
    for j in range(8):
      square = board[8 - i - 1][j]
      
      # Print coloured pieces for white and black
      if square == 'O' or square == 'X':
        print(square, end=' ')
      elif square.islower():
        print(f'\033[31m{square.upper()}\033[0m', end=' ')
      elif square.isupper():
        print(f'\033[34m{square}\033[0m', end=' ')
    print()

  


if __name__  == "__main__":
    fillBoard()
    printBoard()