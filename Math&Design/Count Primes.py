"""
~ Count the number of prime numbers less than a non-negative number, n.
"""


class Solution:
    def count_primes(self, n: int) -> int:
        if n < 2:
            return 0
        primes = [True for i in range(n)]
        primes[0], primes[1] = False, False
        i = 2
        while i * i < n:
            if not primes[i]:
                pass
            j = i * i
            while j < n:
                primes[j] = False
                j = j + i
            i = i + 1

        count = 0
        for k in range(2, n):
            if primes[k]:
                count = count + 1
        return count
