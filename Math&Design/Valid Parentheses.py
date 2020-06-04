class PersonalSolution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True

        d = {'{': '}',
             '(': ')',
             '[': ']'}

        if s[0] in d.values():
            return False

        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:  # c is closing bracket
                try:
                    last_bracket = stack.pop()
                except:
                    return False  # This returns if we pop an empty stack

                if d[last_bracket] != c:
                    return False

        return True if len(stack) == 0 else False


class CleanSolutionFromLC:
    class Solution:
        def isValid(self, s: str) -> bool:

            stack = []
            left = "([{"
            right = ")]}"

            if s == "":
                return True

            elif len(s) % 2 != 0 or s[0] == ")" or s[0] == "]" or s[0] == "}":
                return False

            for i in range(len(s)):
                if s[i] in left:
                    stack.append(s[i])
                elif s[i] in right:
                    if s[i] == ")":
                        if stack.pop() != left[0]:
                            return False
                    elif s[i] == "]":
                        if stack.pop() != left[1]:
                            return False
                    elif s[i] == "}":
                        if stack.pop() != left[2]:
                            return False
            if stack:
                return False
            return True
