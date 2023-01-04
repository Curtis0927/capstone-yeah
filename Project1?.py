board = [[" " for _ in range(3)] for _ in range(3)]

def draw_board():
  print("  0 1 2")
  for i in range(3):
    print(f"{i} {board[i][0]}|{board[i][1]}|{board[i][2]}")
    if i != 2:
      print("  -----")

def get_move(player):
  while True:
    print(f"Player {player}, enter your move (row column):")
    row, col = map(int, input().split())
    if row in [0, 1, 2] and col in [0, 1, 2] and board[row][col] == " ":
      board[row][col] = player
      break
    print("Invalid move, try again")

def has_won(player):
  # check rows
  for row in board:
    if row == [player, player, player]:
      return True
  # check columns
  for col in range(3):
    if board[0][col] == player and board[1][col] == player and board[2][col] == player:
      return True
  # check diagonals
  if board[0][0] == player and board[1][1] == player and board[2][2] == player:
    return True
  if board[0][2] == player and board[1][1] == player and board[2][0] == player:
    return True
  return False

def main():
  draw_board()
  while True:
    for player in ["X", "O"]:
      get_move(player)
      draw_board()
      if has_won(player):
        print(f"Player {player} has won!")
        return

main()
#not my code but it's cool