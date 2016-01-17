import tkinter as tk

class Sudoku_Table(tk.Frame):
    """
    Table with 9 large squares in a 0-indexed 3x3 array
    """
    def __init__(self, *args, **kwargs):
        """Initialize 9 large_squares, 3 wide rows, and 3 wide columns"""
        super(Sudoku_Table, self).__init__(*args, **kwargs)
        self.large_squares = [[large_square(self, bd = 3, relief = tk.GROOVE) 
                               for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                lgsqr = self.large_squares[i][j]
                lgsqr.grid(row = i, column = j)

        self.wide_rows = self.large_squares
        self.wide_cols = [[row[i] for row in self.wide_rows] for i in range(3)]

    
    def wide_row(self, x):
        """get the 0-indexed wide row n, a list of large_squares"""
        return self.wide_rows[x]
    def wide_col(self, y):
        """get the 0-indexed wide column n, a list of large_squares"""
        return self.wide_cols[y]
    def l_square(self, x, y):
        """Get large_square at x,y from a 0-indexed 3x3 array of large squares"""
        return self.large_squares[x][y]

    ########## ABSTRACTION BARRIER ##########

    def all_large_squares(self):
        """return a 9-membered list containing all large squares"""
        return [self.l_square(i,j) for i in range(3) for j in range(3)]

    def row(self, x):
        """Get 0-indexed row n, a list of small_squares"""
        wrow_num = x//3
        row_num = x%3
        r = []
        for square in self.wide_row(row_num):
            r.extend(square.row(row_num))
        return r
    def col(self, y):
        """Get 0-indexed column n, a list of small_squares"""
        wcol_num = y//3
        col_num = y%3
        r = []
        for square in self.wide_col(col_num):
            r.extend(square.row(col_num))
        return r
    def s_square(self, x, y):
        """Get small_square at x,y on a 0-indexed 9x9 array of small_squares"""
        wrow_num = x//3
        wcol_num = y//3
        row_num = x%3
        col_num = y%3
        return self.l_square(wrow_num, wcol_num).s_square(row_num, col_num)
    
    ########## ABSTRACTION BARRER ##########

    def set_visibility(self, b = False):
        """make all helper numbers visible or invisible"""
        for lg_sqr in self.all_large_squares():
            lg_sqr.set_visibility(b)
        
class large_square(tk.Frame):
    """
    a large square contains a 3x3 (row x column) array of small_squares
        calling the constructor requires another 2D array and the indices of the top left small_square
    attributes:
    small_squares - a 3x3 array of small_squares
    rows - a list 3-size lists representing rows
    columns - a list of 3-size lists representing columns
    """
    def __init__(self, *args, **kwargs):
        """Initialize 3x3 array of small_squares, 3 columns, and 3 rows"""
        super(large_square, self).__init__(*args, **kwargs)
        self.small_squares = [[small_square(self, height = 60, width = 60,
                                             bd = 0.5, relief = tk.GROOVE) 
                                                    for _ in range(3)]
                                                            for _ in range(3)]
        for i in range(3):
            for j in range(3):
                smsqr = self.small_squares[i][j]
                smsqr.grid(row = i, column = j)

        self.columns = [[row[i] for row in self.small_squares] for i in range(3)]
        self.rows = self.small_squares
    

    def s_square(self, x, y):
        """get the small square at this large_square's 0,0-indexed location mxn"""
        return self.small_squares[x][y]
    def row(self, x):
        """get this big_square's 0-indexed row x"""
        return self.rows[x]
    def col(self, y):
        """get this big_square's 0-indexed column y"""
        return self.columns[y]
    ########## ABSTRACTION BARRER ##########

    def all_squares(self):
        """return 9-member list of all small_squares in this square"""
        return [self.s_square(i,j) for i in range(3) for j in range (3)]

    def set_visibility(self, b = False):
        for sml_sqr in self.all_squares():
            sml_sqr.set_visibility(b)


class small_square(tk.Canvas):
    """
    a square in a sudoku table

    attributes:
    boolean filled - whether the square has a number in it
    int number - the number a filled square has (0 if unfilled)
    3x3array helper_squares - subsquares containing a possible number for this square
    boolean-property show_nums - whether square should show the numbers in the helper_squares
        (ONLY TRUE IF self.filled IS FALSE)
    """
    squareID = 0 # Testing purposes only
    def __init__(self, *args, **kwargs):

        super(small_square, self).__init__(*args, **kwargs)
        self.filled = False;
        self.number = 0;
        # self.poss_nums = [1,2,3,4,5,6,7,8,9]
        self._show_nums = False
        num_id = self.create_text(30,30, state = tk.HIDDEN,
                                text = "0", font = ('Times', '24', 'bold'))
        ssquare_frame = tk.Frame()
        frame_id = self.create_window(31,31, window = ssquare_frame)
        self.helper_squares = [[helper_square(ssquare_frame, 3*i + j+1) for j in range(3)] 
                                                                    for i in range(3)]

        for i in range(3):
            for j in range(3):
                hlpsqr = self.helper_squares[i][j]
                hlpsqr.grid(row = i, column = j)
                # hlpsqr.grid()

        #testing purposes only
        self.ID = small_square.squareID 
        small_square.squareID += 1 

    @property
    def show_nums(self):
        """Boolean property that determines whether a square's possible numbers
            should be shown"""
        return self._show_nums and not self.filled
    @show_nums.setter
    def show_nums(self, value):
        self._show_nums = value
    @show_nums.deleter
    def show_nums(self):
        del self._show_nums

    #Testing only
    def __str__(self):
        return str(self.ID)

    def h_square(self, n):
        """return the helper_square associated with 1-9 integer N"""
        row = (n-1)//3
        col = (n-1)%3
        return self.helper_squares[row][col]
    def all_squares(self):
        """a 9-membered list of all helper_squares in this square"""
        return [self.h_square(i) for i in range(1, 10)]

    def set_visibility(self, b = False):
        self.show_nums = b
        for hsqr in self.all_squares():
            hsqr.set_visibility(b)
    
    def set_number(self, num):
        return

class helper_square(tk.Frame):
    """a Frame within a small_square that 
        contains a possible number for that square"""
    def __init__(self, parent, num, **kwargs):
        # self.arg = arg
        super(helper_square, self).__init__(parent, **kwargs)
        self.helper_num = num
        self.is_visible = False
        self.label = tk.Label(self, height = 1, width = 2, text = "")
        
        self.label.grid()

    def set_visibility(self, b):
        if b: self.label.configure(text = self.helper_num)
        else: self.label.configure(text = "")


## Basic Tests ###
# new_table = Sudoku_Table()
# [print(x) for x in new_table.col(1)] 
# print("\\")
# [print(x) for x in new_table.row(4)] # 36-44
# print("\\")
# [print(x) for x in new_table.l_square(0,0).row(0)] #0-2