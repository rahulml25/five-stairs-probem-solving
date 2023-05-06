from game_types import XorO
from player import Player
from board import Board
import random


class Game:

  def __init__(self) -> None:
    self.askUserInfo()
    self.board = Board(self.players)

  def askUserInfo(self):
    computerName = "computer"
    playerName = input("Enter your name: ")

    while True:
      sign = input("Choose any of 'X' and 'O': ")

      if sign == 'X':
        playerSign = sign
      elif sign == 'O':
        playerSign = sign
      else:
        print(f"Invalid choice: '{sign}'")
        continue

      print(f"You choosed '{playerSign}'", )
      break

    if playerSign == 'X':
      self.players: tuple[Player, Player] = (
        Player(playerName, playerSign), Player(computerName, 'O'))
    else:
      self.players: tuple[Player, Player] = (
        Player(playerName, playerSign), Player(computerName, 'X'))

  def getWinner(self):
    isWin, winnerSign = self.board.isWin()
    if isWin:
      for player in self.players:
        if player.sign == winnerSign:
          return player
    return None

  def run(self):
    while True:
      self.board.draw()
      strPos = (input("Enter the position: "))

      if not strPos.isnumeric():
        print(f"Invalid position '{strPos}'")
        continue

      playerPos = int(strPos) - 1

      if playerPos in self.board.emptyIndexes():
        self.board.matrix[playerPos] = self.players[0].sign
      else:
        print(f"The position {playerPos} is not empty")
        continue

      winner = self.getWinner()
      if winner != None:
        break

      compPos = random.choice(self.board.emptyIndexes())
      self.board.matrix[compPos] = self.players[1].sign

      winner = self.getWinner()
      if winner != None:
        break

    print(f"The winner is: {winner.name}")  # type: ignore

#     |    |
#  0  | 1  | 2
# ----|----|----
#  3  | 4  | 5
# ----|----|----
#  6  | 7  | 8
#     |    |


if __name__ == '__main__':
  try:
    game = Game()
    game.run()

  except KeyboardInterrupt:
    pass
