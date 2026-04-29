board = []
ROOKDIR = [[1, 0], [-1, 0], [0, 1], [0, -1]]
BISHDIR = [[1, 1], [-1, -1], [1, -1], [-1, 1]]
KNIDIR = [[2, 1], [-2, -1], [2, -1], [-2, 1],[1, 2], [-1, -2], [1, -2], [-1, 2]]
whitePieces = {"r" : [[0,0], [0,7]], "b": [[0,2], [0,5]], "n": [[0,1],[0,6]], "q" : [[0,3]], "k": [[0,4]], "p": [[1,0], [1,1], [1,2], [1,3], [1,4], [1,5], [1,6], [1,7]]}
blackPieces = {"r" : [[7,0], [7,7]], "b": [[7,2], [7,5]], "n": [[7,1],[7,6]], "q" : [[7,3]], "k": [[7,4]], "p": [[6,0], [6,1], [6,2], [6,3], [6,4], [6,5], [6,6], [6,7]]}


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
  
  if (i == 7 and j == 4):
    square = 'k'
  
  if (i == 7 and j == 3):
    square = 'q'
  
  if i == 1:
    square = 'P'
  
  if i == 6:
    square = 'p'
  
  return square

# Helper that calculates the possible moves of a piece
def returnValidMoves(piece, location, white):
  validMoves = []
  piece = piece.lower()
  
  match piece:
    case "r":
      validMoves = returnRookMoves(validMoves, location, white)
    
    case "b":
      validMoves = returnBishopMoves(validMoves, location, white)
        
    case "n":
      validMoves = returnKnightMoves(validMoves, location, white)
    
    case "q":
      validMoves = returnBishopMoves(validMoves, location, white)
      validMoves = returnRookMoves(validMoves, location, white)
      
    case "k":
      for i in range(4):
        row  = location[0] + BISHDIR[i][0]
        col = location[1] + BISHDIR[i][1]
        if (row < 8 and row >= 0 and col < 8 and col >= 0):
          if (board[row][col] != 'X' and board[row][col] != 'O'):
            if (white and board[row][col].islower()):
              validMoves.append([row, col])
            elif ((not white) and board[row][col].isupper()):
              validMoves.append([row, col])
            break
          validMoves.append([row, col])
          row += BISHDIR[i][0]
          col += BISHDIR[i][1]
          
      for i in range(4):
        row  = location[0] + ROOKDIR[i][0]
        col = location[1] + ROOKDIR[i][1]
        if (row < 8 and row >= 0 and col < 8 and col >= 0):
          if (board[row][col] != 'X' and board[row][col] != 'O'):
            if (white and board[row][col].islower()):
              validMoves.append([row, col])
            elif ((not white) and board[row][col].isupper()):
              validMoves.append([row, col])
            break
          validMoves.append([row, col])
          row += ROOKDIR[i][0]
          col += ROOKDIR[i][1]
    
    case "p":
      if (white):
        if (location[0] == 7): return
        row = location[0] + 1
        col = location[1]
        if (board[row][col] == 'X' or board[row][col] == 'O'):
          validMoves.append([row, col])
        
          
        col = location[1] - 1
        if (board[row][col] != 'X' and board[row][col] != 'O' and board[row][col].islower()):
          validMoves.append([row, col])
          
        col = location[1] + 1
        if (board[row][col] != 'X' and board[row][col] != 'O' and board[row][col].islower()):
          validMoves.append([row, col])
          
        if (location[0] == 1 and (board[2][location[1]] == 'X' or board[2][location[1]] == 'O') and (board[3][location[1]] == 'X' or board[3][location[1]] == 'O')):
          validMoves.append([3, location[1]])
          
      else:
        if (location[0] == 0): return
        row = location[0] - 1
        col = location[1]
        
        if (board[row][col] == 'X' or board[row][col] == 'O'):
          validMoves.append([row, col])
          
        col = location[1] - 1
        if (board[row][col] != 'X' and board[row][col] != 'O' and board[row][col].isupper()):
          validMoves.append([row, col])
          
        col = location[1] + 1
        if (board[row][col] != 'X' and board[row][col] != 'O' and board[row][col].isupper()):
          validMoves.append([row, col])
        
        
        if (location[0] == 6 and (board[5][location[1]] == 'X' or board[5][location[1]] == 'O') and (board[4][location[1]] == 'X' or board[4][location[1]] == 'O')):
          validMoves.append([4, location[1]])
  
  return validMoves

def returnBishopMoves(validMoves, location, white):
  for i in range(4):
    row  = location[0] + BISHDIR[i][0]
    col = location[1] + BISHDIR[i][1]
    while (row < 8 and row >= 0 and col < 8 and col >= 0):
      if (board[row][col] != 'X' and board[row][col] != 'O'):
        if (white and board[row][col].islower()):
          validMoves.append([row, col])
        elif ((not white) and board[row][col].isupper()):
          validMoves.append([row, col])
        break
      validMoves.append([row, col])
      row += BISHDIR[i][0]
      col += BISHDIR[i][1]
  
  return validMoves

def returnRookMoves(validMoves, location, white):
  for i in range(4):
          row  = location[0] + ROOKDIR[i][0]
          col = location[1] + ROOKDIR[i][1]
          while (row < 8 and row >= 0 and col < 8 and col >= 0):
            if (board[row][col] != 'X' and board[row][col] != 'O'):
              if (white and board[row][col].islower()):
                validMoves.append([row, col])
              elif ((not white) and board[row][col].isupper()):
                validMoves.append([row, col])
              break
            validMoves.append([row, col])
            row += ROOKDIR[i][0]
            col += ROOKDIR[i][1]
  
  return validMoves

def returnKnightMoves(validMoves, location, white):
  for i in range(8):
        row  = location[0] + KNIDIR[i][0]
        col = location[1] + KNIDIR[i][1]
        if (row < 8 and row >= 0 and col < 8 and col >= 0):
          if (board[row][col] != 'X' and board[row][col] != 'O'):
            if (white and board[row][col].islower()):
              validMoves.append([row, col])
            elif ((not white) and board[row][col].isupper()):
              validMoves.append([row, col])
            break
          validMoves.append([row, col])
          row += KNIDIR[i][0]
          col += KNIDIR[i][1]
  
  return validMoves

# Performs a move action
def movePiece(white):
  move  = getMove(white)
  curRow, curCol, movRow, movCol = move["curLoc"][0], move["curLoc"][1], move["movLoc"][0], move["movLoc"][1]
  takenPiece = board[movRow][movCol]
  board[movRow][movCol] = board[curRow][curCol]
  board[curRow][curCol] = 'X' if ((curRow + curCol) % 2 == 0) else 'O'
  movStr = createMoveNotation(move["piece"], curRow, curCol, move["movLoc"][0], move["movLoc"][1], white)
  
  if white:
    for piece in whitePieces[move["piece"]]:
      if piece[0] == curRow and  piece[1] == curCol:
        piece[0] = movRow
        piece[1] = movCol
  else:
    for piece in blackPieces[move["piece"]]:
      if piece[0] == curRow and  piece[1] == curCol:
        piece[0] = movRow
        piece[1] = movCol
        
  if not (takenPiece == "X" or takenPiece == "O"):
    if takenPiece.isupper():
      for index, piece in enumerate(whitePieces[move["piece"]]):
        if piece[0] == curRow and  piece[1] == curCol:
          whitePieces[move["piece"]].pop(index)
    
    else:
      for index, piece in enumerate(blackPieces[move["piece"]]):
        if piece[0] == curRow and  piece[1] == curCol:
          blackPieces[move["piece"]].pop(index)
    
  print(f"{"White" if white else "Black"} played {movStr}")
  return
    
    
def getMove(white):
  selectedPiece = {}
  allPieces = []
  if (white):
    index = 0
    for key in whitePieces.keys():
      for pieceLoc in whitePieces.get(key):
        if key.lower() == "p":
          print(f"{index + 1}.{convertToNotation(pieceLoc[0], pieceLoc[1])}", end="  ")  
        else:
          print(f"{index + 1}.{key.upper()}{convertToNotation(pieceLoc[0], pieceLoc[1])}", end="  ")
        allPieces.append({"p": key, "loc": pieceLoc})
        index += 1
  else :
    index = 0
    for key in blackPieces.keys():
      for pieceLoc in blackPieces.get(key):
        if key.lower() == "p":
          print(f"{index + 1}.{convertToNotation(pieceLoc[0], pieceLoc[1])}", end="  ")  
        else:
          print(f"{index + 1}.{key.upper()}{convertToNotation(pieceLoc[0], pieceLoc[1])}", end="  ")
        allPieces.append({"p": key, "loc": pieceLoc})
        index += 1

  print()  
  selected = input("Please select your piece:")
  while (not selected.isalnum()) or (int(selected) < 1 or int(selected) > len(allPieces)):
    print("ERROR: Please enter a number from the options")
    selected = input("Please select your piece:")
  selectedPiece = allPieces[int(selected) - 1]

  validMoves = returnValidMoves(selectedPiece["p"], selectedPiece["loc"], white)
  while(len(validMoves) == 0):
    print("ERROR: No valid moves for this piece please select another")
    selected = input("Please select your piece:")
    selectedPiece = allPieces[int(selected) - 1]
    validMoves = returnValidMoves(selectedPiece["p"], selectedPiece["loc"], white)
  
        
  for index, move in enumerate(iter(validMoves)):
    print(f"{index + 1}.{createMoveNotation(selectedPiece["p"].upper() if white else selectedPiece["p"], selectedPiece["loc"][0], selectedPiece["loc"][1], move[0], move[1], white)}", end="  ")
  
  print()
  selected = input("Please select your move:")
  while (not selected.isalnum()) or (int(selected) < 1 or int(selected) > len(validMoves)):
    print("ERROR: Please enter a number from the options")
    selected = input("Please select your move:")
  
  return {"piece": selectedPiece["p"], "curLoc": selectedPiece["loc"], "movLoc": validMoves[int(selected) - 1]}
    
      
# Converts move to string format
def createMoveNotation(piece, curRow, curCol, movRow, movCol, white):
  destString = convertToNotation(movRow, movCol)
  isWhite = white
  takes = False
  if (board[movRow][movCol] != "X" and board[movRow][movCol] != "O"): takes = True
  
  
  if (piece.lower() == "p" and takes):
    return f"{chr(curCol + ord('a'))}x{destString}"
  
  if (piece.lower() == "p"):
    return f"{chr(curCol + ord('a'))}{movRow + 1}"
  
  isAmbiguous = False
  isDoubleAmbiguous = False
  
  for move in returnValidMoves(piece, [movRow, movCol], isWhite):
    if (board[move[0]][move[1]] == "piece" and (not (move[0] == curRow and move[1] == curCol))):
      isAmbiguous = True
      if (move[1] == curCol):
        isDoubleAmbiguous = True
    
    if (isDoubleAmbiguous): break
    
  sourceString = ""
  if isAmbiguous: sourceString = f"{chr(curCol + ord('a'))}"
  if isDoubleAmbiguous: sourceString = f"{sourceString}{curRow + 1}"
    
  return f"{piece.upper()}{sourceString}x{destString}" if takes else f"{piece.upper()}{sourceString}{destString}"
  
  
    


# Converts row col to chess notation:
def convertToNotation(row, col):
  return f'{chr(col + ord('a'))}{row + 1}'
    
    

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
    
    resign = False
    turnWhite = True
  
    while 1:
      print(f"{"White" if turnWhite else "Black"} to move:")
      printBoard()
      movePiece(turnWhite)
      turnWhite = not turnWhite