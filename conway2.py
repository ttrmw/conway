class board:
    """\
    class to represent a Conway's Game of Life board\
    """ 
    def __init__(self, square): 
        self.size = 0
        self.cells = []
        self.size = square 
        for idx in range(0, self.size): 
            x = []
            for jdx in range(0, self.size):
                x.append(Cell(idx, jdx))
            self.cells.append(x)

    def seed(self, coords):
        self.cells[coords[1]][coords[0]].is_alive = True 

 
    def state(self):
        """\
        check the state of the current_board\
        """
        ret = ""
        for col in self.cells: 
            for cell in col: 
                ret += "".join(("(", str(cell.y), ",", str(cell.x), ")", ": ", 
                       str(cell.is_alive), "  "))
            ret += "\n"
        return ret 

    def _check_adjacent(self, cell):

        def wrap(index):
            """\
            Allows toroidal implementation by giving a wrapped value for input \
            index\
            """

            return index % self.size

        """\
        checks the 8 cells directly adjacent to the cell passed in, returning 
        count of adjacent live cells.\
        """
        
        ret = 0
        #board instance needs to be referenced here for things to be done.
        ret += self.cells[wrap(cell.x + 1)][wrap(cell.y)].is_alive
        ret += self.cells[wrap(cell.x - 1)][wrap(cell.y)].is_alive
        ret += self.cells[wrap(cell.x + 1)][wrap(cell.y + 1)].is_alive
        ret += self.cells[wrap(cell.x - 1)][wrap(cell.y + 1)].is_alive
        ret += self.cells[wrap(cell.x + 1)][wrap(cell.y - 1)].is_alive
        ret += self.cells[wrap(cell.x - 1)][wrap(cell.y - 1)].is_alive
        ret += self.cells[wrap(cell.x)][wrap(cell.y + 1)].is_alive
        ret += self.cells[wrap(cell.x)][wrap(cell.y - 1)].is_alive
        #idx % len(board.cells(coord))
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

    def __init__(self, x, y):
        self.x = x
        self.y = y


def tick(tick_board): 
    """\
    iterate board by one generation\
    """
    new_board = board(tick_board.size)
    for col in tick_board.cells:
        for cell in col: 
                new_board.cells[cell.x][cell.y].is_alive = tick_board.alive_next(cell)
                    
    #check & iterate state of all cells on board.
    print "old board:"
    print tick_board.state() 
    print "new board:"
    print new_board.state()
    return new_board  

    
x = board(10)
x.seed([0,1])
x.seed([3,1])
x.seed([2,2])