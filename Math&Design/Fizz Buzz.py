"""
~Write a program that outputs the string representation of numbers from 1 to n.

~But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
    For numbers which are multiples of both three and five output “FizzBuzz”.
"""


class Solution(object):
    def fizz_buzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ship_back = []
        for i in range(0, n):
            true_num = i + 1
            fizz = true_num % 3 == 0
            buzz = true_num % 5 == 0
            if fizz and buzz:
                ship_back.append("FizzBuzz")
            elif fizz:
                ship_back.append("Fizz")
            elif buzz:
                ship_back.append("Buzz")
            else:
                ship_back.append(str(true_num))
        return ship_back
