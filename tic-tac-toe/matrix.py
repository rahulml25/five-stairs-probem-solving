class Matrix:

  def __init__(self, rows: int, cols: int) -> None:
    if rows <= 0 or cols <= 0:
      raise ValueError("Matrix with zero rows or columns is not allowed")

    self.cols = cols
    self.rows = rows

    self.__raw = [
      [None for _ in range(cols)]
      for _ in range(rows)
    ]

  def clear(self):
    self.__raw = [
      [None for _ in range(self.cols)]
      for _ in range(self.rows)
    ]

  def __getitem__(self, items: int | tuple[int, int]):
    itemsType = type(items)

    if not (itemsType == int or itemsType == tuple):
      raise TypeError(f"Matrix indices must be integers or tuple, not {itemsType}")

    if itemsType == int:
      idx: int = items  # type: ignore
      if not (-1 < idx < self.cols * self.rows):
        raise IndexError(f"Matrix index out of range")

      return self.__raw[int(idx / self.cols)][idx % self.cols]

    # then it should be tuple
    pos: tuple[int, int] = items  # type: ignore

    if len(pos) != 2:
      raise ValueError(f"Matrix is two dimensional, got {items}")

    row, col = pos

    if not -1 < row < self.rows:
      raise IndexError(f"Matrix row[{row}] index out of range")
    elif not -1 < col < self.cols:
      raise IndexError(f"Matrix column[{col}] index out of range")

    return self.__raw[row][col]

  def __setitem__(self, items: int | tuple[int, int], newValue):
    itemsType = type(items)

    if not (itemsType == int or itemsType == tuple):
      raise TypeError(f"Matrix indices must be integers or tuple, not {itemsType}")

    if itemsType == int:
      idx: int = items  # type: ignore
      if not (-1 < idx < self.cols * self.rows):
        raise IndexError(f"Matrix index out of range")

      self.__raw[int(idx / self.cols)][idx % self.cols] = newValue
      return

    # then it should be tuple
    pos: tuple[int, int] = items  # type: ignore

    if len(pos) != 2:
      raise ValueError(f"Matrix is two dimensional, got {items}")

    row, col = pos
    self.__raw[row][col] = newValue


# Matrix(3, 3)[5]
# Matrix(3, 3)[2, 3]
# Matrix(3, 3)[5:65:5]
# Matrix(3, 3)['a':'z':2]
# Matrix(3, 3)[object()]

# {}[8]

if __name__ == '__main__':
  print(Matrix(3, 4)[2, 3])
