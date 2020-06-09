"""
~Shuffle a set of numbers without duplicates.
"""


class Solution:

    def __init__(self, nums: List[int]):
        self.original = list(nums)
        self.array = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        n = len(self.array) - 1
        for i in range(0, n):
            random_index = randint(i, n)
            self.array[i], self.array[random_index] = self.array[random_index], self.array[i]
        return self.array

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
