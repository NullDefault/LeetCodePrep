"""
~The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221

~1 is read off as "one 1" or 11.
~11 is read off as "two 1s" or 21.
~21 is read off as "one 2, then one 1" or 1211.

~Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
 ~You can do so recursively, in other words from the previous member read off the digits,
  ~counting the number of digits in groups of the same digit.

~Note: Each term of the sequence of integers will be represented as a string.
"""


class IterativeSolution:
    def count_and_say(self, n: int) -> str:
        s = "1"
        if n == 1:
            return s
        for i in range(2, n + 1):
            j = 0
            temp = ""
            curr = ""
            count = 0
            while j < len(s):
                if curr == "":
                    curr = s[j]
                    count = 1
                    j = j + 1
                elif curr == s[j]:
                    count = count + 1
                    j = j + 1
                else:
                    temp = temp + str(count) + curr
                    curr = ""
                    count = 0
            temp = temp + str(count) + curr
            s = temp
        return s


class RecursiveSolution:
    def count_and_say(self, n: int) -> str:
        if n == 1:
            return '1'
        else:
            last_say = self.count_and_say(n - 1)
            # print(last_say)
            counter, this_str = 1, ''
            for i in range(1, len(last_say)):
                if last_say[i] == last_say[i - 1]:
                    counter += 1
                else:
                    this_str += str(counter) + last_say[i - 1]
                    counter = 1
                # print(counter, n, this_str)
            return this_str + str(counter) + last_say[-1]
