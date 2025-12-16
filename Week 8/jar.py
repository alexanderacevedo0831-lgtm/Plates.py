class Jar:
    # Initialize the jar with the given capacity,
    # If capacity is not non-negative int, __init__ should raise ValueError
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity
        self._size = 0

    # Return a string with n cookies �, where n is the number of cookies in the jar
    # For example, if the jar has 3 cookies, __str__ should return "���"
    def __str__(self):
        return "🍪" * self._size

    # Deposit should add n cookies to the cookie jar
    # If adding many would exceed the cookie jar’s capacity, deposit should raise ValueError
    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Deposit must be a non-negative integer")
        if self._size + n > self._capacity:
            raise ValueError("Deposit exceeds jar capacity")
        self._size += n

    # Withdraw should remove n cookies from the cookie jar
    # If there aren't that mnay cookies in the jar, withdraw should raise ValueError
    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Withdraw must be a non-negative integer")
        if self._size < n:
            raise ValueError("Not enough cookies in the jar")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    # Size should return the number of cookies actually in the cookie jar, intially 0
    @property
    def size(self):
        return self._size