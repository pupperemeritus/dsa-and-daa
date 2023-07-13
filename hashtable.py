# from collections import defaultdict


def checkPrime(n):
    """
    Check if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True


def prime(n):
    """
    Returns the nth prime number.

    Args:
        n (int): The position of the prime number to be found.

    Returns:
        int: The nth prime number.
    """
    count = 0
    prime = 1

    while True:
        if checkPrime(prime):
            count += 1
            if count == n:
                return prime
            prime += 1
        else:
            prime += 1


class HashTable:
    def __init__(self, nth_prime):
        self.table = {}
        self.nth_prime = prime(nth_prime)

    def hash(self, index):
        return index % self.nth_prime

    def insert(self, data, index=None):
        if index is None:
            index = data
        hv = self.hash(index)
        if hv not in self.table.keys():
            self.table[hv] = []
        self.table[hv].append(data)

    def delete(self, index, data=None):
        if data is None:
            if len(self.table[self.hash(index)]) >= 2:
                print("Deleting multiple items")
            self.table.pop(self.hash(index))
        else:
            self.table[self.hash(index)].pop(self.table[self.hash(index)].index(data))


if __name__ == "__main__":
    ht = HashTable(10)
    print(prime(10))
    ht.insert("Hello", 43)
    ht.insert("World", 32)
    ht.insert("Deletion checking", 31)
    ht.insert("Deletion checking 2", 32)
    print(ht.table)
    ht.delete(31)
    ht.delete(32, "Deletion checking 2")
    print(ht.table)
