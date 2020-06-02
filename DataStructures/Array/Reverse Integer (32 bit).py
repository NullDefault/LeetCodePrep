class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_s = str(x)
        negative = False

        if x_s[0] == '-':
            negative = True
            x_s = x_s[1:len(x_s)]

        x_s = x_s[::-1]

        new_x = -int(x_s) if negative else int(x_s)

        if abs(new_x) > 2 ** 31:  # This checks if the new int overflows the 32 bit boundary
            return 0
        else:
            return new_x
