class Board:
    """\
    class to represent a Conway's Game of Life board\
    """ 
    def __init__(self, square): 
        self.size = 0
        self.cells = []
        self.size = square 
        for idx in range(0, self.size): 
            y = []
            for jdx in range(0, self.size):
                y.append(Cell(idx, jdx))
            self.cells.append(y)

    def seed(self, coords):
        self.cells[coords[0]][coords[1]].is_alive = True

    def state(self):
        """\
        check the state of the current_board\
        """
        ret = ""
        ret += "-" * (1 + self.size)
        ret += "\n"

        for col in self.cells: 
            for cell in col: 
                if cell.x == 0 or cell.x == self.size - 1:
                    ret += "|"
                if cell.is_alive: 
                    ret += "x"
                else:
                    ret += " "
            ret += "\n"

        ret += "-" * (1 + self.size)
        return ret 

    def _check_adjacent(self, cell):
        """\
        checks the 8 cells directly adjacent to the cell passed in, returning
        count of adjacent live cells.\
        """

        def wrap(index):
            """\
            Allows toroidal implementation by giving a wrapped value for input \
            index\
            """
            return index % self.size

        ret = -1    # discard checked cell's status
        for j in range(-1, 2):
            for i in range(-1, 2):
                ret += self.cells[wrap(cell.x + i)][wrap(cell.y + j)].is_alive
        return ret

    def alive_next(self, cell): 
        """\
        determines a cell's new state based on adjacent_living cells.\
        """
        adjacent_living = self._check_adjacent(cell)

        if adjacent_living < 2 or adjacent_living > 3: 
            return False
        elif cell.is_alive or adjacent_living == 3:
            return True
        else:
            return False


class Cell:
    """\
    class to represent a Conway's Game of Life cell\
    """
    x = 0
    y = 0
    is_alive = False 

    def __init__(self, y, x):
        self.x = x
        self.y = y


def tick(tick_board): 
    """\
    iterate board by one generation\
    """
    i = 0
    new_board = Board(tick_board.size)
    for col in tick_board.cells:
        for cell in col: 
                new_board.cells[cell.x][cell.y].is_alive = tick_board.alive_next(cell)
                i += new_board.cells[cell.x][cell.y].is_alive

    #print "old board:"
    #print tick_board.state()
    print "new board:"
    print new_board.state()
    print i
    return new_board  

    
game_board = Board(10)
game_board.seed([0, 1])
game_board.seed([3, 1])
game_board.seed([2, 2])
game_board.seed([1, 1])
game_board.seed([3, 2])
game_board.seed([2, 1])
game_board.seed([4, 1])
game_board.seed([0, 0])
game_board.seed([2, 1])
game_board.seed([4, 0])
game_board.seed([4, 2])
game_board.seed([4, 3])
game_board.seed([4, 1])
game_board.seed([3, 4])
game_board.seed([2, 4])

print game_board.state()
for i in range(0, 20):
    game_board = tick(game_board)
