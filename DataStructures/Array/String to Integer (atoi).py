"""
~Implement atoi which converts a string to an integer.

~The function first discards as many whitespace characters as necessary until the first non-whitespace
character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by
as many numerical digits as possible, and interprets them as a numerical value.

~The string can contain additional characters after those that form the integral number,
which are ignored and have no effect on the behavior of this function.

~If the first sequence of non-whitespace characters in str is not a valid integral number,
or if no such sequence exists because either str is empty or it contains only whitespace characters,
no conversion is performed.

~If no valid conversion could be performed, a zero value is returned.

~Note:
    Only the space character ' ' is considered as whitespace character.
    Assume we are dealing with an environment which could only store integers within
    the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of
    representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned
"""


class Solution:
    def my_atoi(self, s: str) -> int:
        max_int = 2147483647
        n = len(s)

        first_non_space = None
        for i in range(0, n):
            c = s[i]
            if c != ' ':
                first_non_space = i
                break

        if first_non_space is None:
            return 0

        sign_check = s[first_non_space] == '-', s[first_non_space] == '+'
        new_s = []
        for j in range(first_non_space + 1 if (sign_check[0] or sign_check[1]) else first_non_space, n):

            c = s[j]
            if c.isnumeric():
                new_s.append(int(s[j]))
            else:
                break

        digit = 10 ** (len(new_s) - 1)
        ship_back = 0

        for e in new_s:
            ship_back = ship_back + e * digit
            digit = digit // 10

        if ship_back > max_int:
            # min and max int values are not the same number for some reason lmfao
            ship_back = max_int + 1 if sign_check[0] else max_int

        return -1 * ship_back if sign_check[0] else ship_back
