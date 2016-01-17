def solve_coin_matrix(mat):
    """Given a matrix with the 0 or 1 coins in each bucket, pick nonzero buckets such that
        (1) every bucket chosen is below and to the right of the previous bucket
        (2) we maximize the number of buckets
        
        Notes: Similar to Rohan's coinbucket problem but with these specs:
            if current bucket is 0, we can move right or down as we please
            if current bucket is 1, we must immediately move diagonally right-down
            
        METHOD: for every bucket, increment its value by the maximum of:
                (1) the upper left corner box if it contained a coin
                (2) the left box if it did NOT contain a coin
                (3) the upper box if it did NOT contain a coin
                All boxes are reachable in this manner regardless of whether it has a coin
                
    """
    def max_adjacent(i, j):
        """Determine the maximum of the ul box if it had a coin, the left if it didnt and up if didnt
            Assume i,j > 0"""
        nonlocal mat
        u_val, l_val, ul_val = 0,0,0
        if not mat[i - 1][j].has_coin():
            u_val = mat[i - 1][j].value() 
        if not mat[i][j - 1].has_coin():
            l_val = mat[i][j - 1].value()
        if mat[i - 1][j - 1].has_coin():
            ul_val = mat[i - 1][j - 1].value() 
        return max(u_val, l_val, ul_val)     
        # if i and not mat[i - 1][j].has_coin():
        #     u_val = mat[i - 1][j].value() 
        # if j and not mat[i][j - 1].has_coin():
        #     l_val = mat[i][j - 1].value()
        # if i and j and mat[i - 1][j - 1].has_coin():
        #     ul_val = mat[i - 1][j - 1].value() 
        # return max(u_val, l_val, ul_val)     
        
    rows = len(mat)
    cols = len(mat[0])
    for j in range(1, cols):
        left = mat[0][j - 1]
        if not (left.has_coin):
            mat[0][j].inc_value(left.value())
    for i in range(1, rows):
        up = mat[i][0]
        if not (up.has_coin()):
            mat[i][0].inc_value(up.value())
    for i in range(1, rows):
        # print(i)
        for j in range(1, cols):
            # print([i, j, rows, cols])
            mat[i][j].inc_value(max_adjacent(i, j))
    return mat[rows - 1][cols - 1].value()

class int_bool(object):
    def __init__(self, val = 0, bl = False):
        self.valu = val
        self.coin = bl #True if had coin, False otherwise
    def value(self):
        return self.valu
    def has_coin(self):
        return self.coin
    def set_value(self, n = 0):
        self.valu = n
    def inc_value(self, n = 0):
        self.valu += n
    def set_bool(self, b = False):
        self.coin = b
    def __str__(self):
        s = "("+ str(self.valu) + ", " + str(self.coin) + ") "
        return s

def string_to_bin_array(s1, s2):
    """Given two strings, create a len(s1) + 1, len(s2) + 1 2D matrix of int_bool objects such that
        matrix[i][j].has_coin() = True iff s1[i] == s2[j]
        matrix[i][j].value() = 1 iff s1[i] == s2[j]
        The extra space is used for later
    """
    matrix = []
    # matrix = [[int_bool() for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
    for i in range(len(s1)):
        matrix.append([])
        for j in range(len(s2)):
            if (s1[i] != s2[j]):
                matrix[i].append(int_bool())
            else:
                matrix[i].append(int_bool(1, True))
        matrix[i].append(int_bool())
    matrix.append([int_bool() for _ in range(len(s2) + 1)])
    return matrix

def solve_problem():
    # print("Solving Problem...")
    f1 = open("input05.txt")
    s1 = f1.readline().strip()
    s2 = f1.readline().strip()
    # print("Making Array")
    m = string_to_bin_array(s1, s2)
    # print("Solving Array")
    len_child = solve_coin_matrix(m)
    print(len_child)
    return
solve_problem()
#for row in m:
#    row_str = ''
#    for col in row:
#        row_str += str(col)
#    print(row_str)
    