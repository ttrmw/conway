class board:
    """\
    class to represent a Conway's Game of Life board\
    """ 
    size = 0
    cells = []
    
    def __init__(self, square): 
        self.size = square 
        for idx in range(0, self.size): 
            x = []
            for jdx in range(0, self.size):
                x.append(Cell(idx, jdx))
            self.cells.append(x)
 ###
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

    def tick(self): 
        """\
        iterate board by one generation\
        """
        new_board = board(self.size)
        print new_board.state()

        for col in self.cells:
            for cell in col: 
                    new_board.cells[cell.x][cell.y].is_alive = self.alive_next(
                        cell)
                    
        #check & iterate state of all cells on board.

        self = new_board

    def _check_adjacent(self, cell):
        """\
        checks the 8 cells directly adjacent to the cell passed in, returning 
        count of adjacent live cells.\
        """
        print cell.x , ", ", cell.y
        print self.state()
        ret = 0
        #board instance needs to be referenced here for things to be done.
        ret += self.cells[cell.x + 1][cell.y].is_alive
        ret += self.cells[cell.x - 1][cell.y].is_alive
        ret += self.cells[cell.x + 1][cell.y + 1].is_alive
        ret += self.cells[cell.x - 1][cell.y + 1].is_alive
        ret += self.cells[cell.x + 1][cell.y - 1].is_alive
        ret += self.cells[cell.x - 1][cell.y - 1].is_alive
        ret += self.cells[cell.x][cell.y + 1].is_alive
        ret += self.cells[cell.x][cell.y - 1].is_alive
        #idx % len(board.cells(coord))
        return ret

    def alive_next(self, cell): 
        """\
        determines a cell's new state based on adjacent_living cells.\
        """
        adjacent_living = self._check_adjacent(cell)
        if adjacent_living < 2 or adjacent_living > 3: 
            return False
        else: 
            return True


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


   

    
x = board(3)