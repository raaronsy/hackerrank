class BITreeSet(object):
    """BITree that stores only 0s and 1s for indices 1-10^5, corresponding to whether an integer
        between 1 and 10^5 is in the tree or not. 0 dummy node kept at index 0 arbitrarily.
        This class must be able to input, delete, lookup, and getsum a value in logN time 
        See methods for exactly how the syntax works"""
    
    def __init__(self, arr, max_num = 10**5):
        """Given an array displaying which values from 1 to max_num are present, create a BITree
           that keeps track of the running sum in logN time."""
        self.max_num = max_num
        self.array = [0 for _ in range(max_num + 1)] #0 to max_num is max_num + 1 numbers total
        for integer in arr:
            if 0 < integer < self.max_num + 1:
                self.incr_value(integer, 1) #increment values at indices INTEGER from 0 to 1
        return
    def get_sum(self, index):
        """Return the sum of all values at and below INDEX
            This determines the number of integers in the set at or below INDEX"""
        if 0 <= index <= self.max_num:
            the_sum = 0
            while(index > 0):
                the_sum += self.array[index]
                index = index - (index&-index) #subtract the rightmost '1' bit from index
            return the_sum
        else:
            print("Index Error")
            return
    def incr_value(self, n, incr):
        """Given INCR to increment, increment value at index N by INCR and update
            the rest of the array accordingly"""
        if (0 < n <= self.max_num):
            while(n < len(self.array)):
                self.array[n] += incr
                n = n + (n&-n) #add the rightmost "set-bit" to n
        return

    def get(self, n):
        """Return the value (incremental value, not sum value) at index N"""
        if (0 < n <= self.max_num):
            return self.get_sum(n) - self.get_sum(n - 1)
        else:
            print("Index Error")
        return
    def set_value(self, n, value):
        """Set value at index n to VALUE; update accordingly"""
        if (0 < n <= self.max_num):
            difference = value - self.get(n)
            self.incr_value(n, difference)
        else:
            print("Index Error")
        return
####ABSTRACTION BARRIER - SET FUNCTIONALITY####
    def count_range(self, n0, n1):
        """Determine the number of items in the set between N0 and N1 inclusive"""
        if (n1 >= n0):
            if (n1 > self.max_num):
                n1 = self.max_num
            if (n0 < 1):
                n0 = 1
            return self.get_sum(n1) - self.get_sum(n0 - 1)
        else:
            print("Index Error")
            return

    def add(self, n):
        """Given an integer n s.t. 1<= n <= 10**5, change the at index n to 1 and update array 
            accordingly, adding the number to the set"""
        self.set_value(n, 1)
        return
    def remove(self, n):
        """Given an integer n as in input(), change the number at index n to 0
            Actually the same as set().discard() since it throws no error"""
        self.set_value(n, 0)
        return
        
    def contains(self, n):
        """Return True if number N is in the set"""
        return self.count_range(n, n) == 1