


class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            print("Capacity can't be negative")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return ("🍪"* self._size)

    def deposit(self, n):

        if n > int(self._capacity) or (int(self._size) + n > int(self._capacity)):
            raise ValueError("Exceeded the capacity of cookie jar")

        self._size = n + int(self._size)
        return self._size
    def withdraw(self, n):
        
        if (self._size < 0) or (self._size < n):
            raise ValueError("Not enough cookie is present")
        self._size = self._size - n
        return self._size


    @property
    def capacity(self):
        return self._capacity



    @property
    def size(self):
        return self._size

smtg = Jar(-1)
"""
print(smtg)
smtg.deposit(11)
smtg.withdraw(11)
print(smtg)
"""


