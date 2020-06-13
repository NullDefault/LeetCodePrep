"""
~Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

~For example, two is written as II in Roman numeral, just two one's added together.
~Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

~Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
    ~Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
        ~The same principle applies to the number nine, which is written as IX.
            ~There are six instances where subtraction is used:

                I can be placed before V (5) and X (10) to make 4 and 9.
                X can be placed before L (50) and C (100) to make 40 and 90.
                C can be placed before D (500) and M (1000) to make 400 and 900.

~Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
"""


class MySolution:
    def roman_to_int(self, s: str) -> int:
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        n = len(s)
        if n == 0:
            return 0
        elif n == 1:
            return d[s]
        else:
            shipback = 0
            i = 0
            while i < n:
                char = s[i]
                next_char = s[i+1] if i+1 < n else None
                if char == 'I':
                    if next_char == 'V' or next_char == 'X':
                        shipback = shipback + (d[next_char] - d[char])
                        i = i + 1  # skip the next char
                    else:
                        shipback = shipback + d[char]
                elif char == 'X':
                    if next_char == 'L' or next_char == 'C':
                        shipback = shipback + (d[next_char] - d[char])
                        i = i + 1  # skip the next char
                    else:
                        shipback = shipback + d[char]
                elif char == 'C':
                    if next_char == 'D' or next_char == 'M':
                        shipback = shipback + (d[next_char] - d[char])
                        i = i + 1  # skip the next char
                    else:
                        shipback = shipback + d[char]
                else:
                    shipback = shipback + d[char]
                i = i + 1
            return shipback


class CleanSolution:
    def roman_to_int(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev = 0
        s1 = s[::-1]
        for i in range(len(s1)):
            curr = d[s1[i]]
            if prev > curr:
                result -= curr
            else:
                result += curr
                prev = curr
        return result


class MySolutionRewritten:  # Although this is cleaner i think my original solution was marginally faster
    def roman_to_int(self, s: str) -> int:
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        n = len(s)
        if n == 0:
            return 0
        elif n == 1:
            return d[s]
        else:
            shipback = 0
            prev = 0
            reversed_s = s[::-1]
            for c in reversed_s:
                curr = d[c]
                if prev > curr:
                    shipback -= curr
                else:
                    shipback += curr
                    prev = curr
            return shipback
