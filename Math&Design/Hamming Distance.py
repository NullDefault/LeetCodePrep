"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.
"""


class Solution:
    # I dont know how bits work yet so like WTF does this do?
    def hamming_distance(self, x: int, y: int) -> int:
        ans = 0
        for i in range(31, -1, -1):
            b1 = x >> i & 1
            b2 = y >> i & 1
            ans += not(b1 == b2)

        return ans
