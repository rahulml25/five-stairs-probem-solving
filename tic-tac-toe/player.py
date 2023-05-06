from game_types import XorO


class Player:

  def __init__(self, name: str, sign: XorO) -> None:
    self.name = name
    self.sign = sign
