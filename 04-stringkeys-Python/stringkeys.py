"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        s = self.calculate_hash_value(string)
        self.table.insert(s,string)
        return -1


        # Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter 
        # Your code goes here
        
        
    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        # Your code goes here
        c = self.calculate_hash_value(string)
        if(self.table[c]==None or self.table[c]!=string):
            return -1
        else:
            return c

        

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        # Your code goes here
        a = (ord(string[0]) * 100)+ord(string[1]) 
        return a


