from matrix import Matrix
from player import Player
import typing


class Board:
  space = ' '

  winningPatterns = [
    # liner - horizontal
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),

    # liner - vertical
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),

    # cross
    (0, 4, 8),
    (2, 4, 6),
  ]

  def __init__(self, players) -> None:
    self.matrix = Matrix(3, 3)
    self.players: tuple[Player] = players

  def emptyIndexes(self):
    indexes: typing.List[int] = []
    for idx in range(self.matrix.rows * self.matrix.cols):
      if self.matrix[idx] == None:
        indexes.append(idx)
    return indexes

  def draw(self):
    idx = 0
    space = self.space

    for y in range(self.matrix.rows):
      for x in range(self.matrix.cols):
        prefix = ''
        suffix = ''

        # prefix
        if y == 0 and x == 0:
          prefix = '     |     |     ' + '\n' + (space * 2)
        else:
          prefix = space * 2

        # suffix
        if x == 0 or x == 1:
          suffix = space * 2 + '|'
        elif x == 2:
          suffix = '\n' + '-----|-----|-----' + '\n'

          if y == 2:
            suffix = '\n' + '     |     |     ' + '\n'

        value = self.matrix[idx]
        if value == None:
          value = idx + 1
        print(f"{prefix}{value}", end=suffix)

        idx += 1

  def isWin(self) -> tuple[bool, str | None]:
    winningSign = None

    for pattern in self.winningPatterns:
      a, b, c = pattern
      if self.matrix[a] == self.matrix[b] == self.matrix[c]:
        winningSign = self.matrix[a]

    if winningSign != None:
      for player in self.players:
        if player.sign == winningSign:
          return (True, winningSign)
    return (False, winningSign)
