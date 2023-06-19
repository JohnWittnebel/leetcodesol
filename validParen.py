class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Idea: maintain a stack of open parentheses, and when we see a close parenthese
        #       we pop and ensure that the close paren corresponds to the top of the stack

        parenStack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                parenStack.append(char)
                continue
            if (len(parenStack) == 0):
                return False
            latestOpen = parenStack.pop()
            if char == "}" and latestOpen != "{":
                return False
            elif char == ")" and latestOpen != "(":
                return False
            elif char == "]" and latestOpen != "[":
                return False
        if (len(parenStack) > 0):
            return False
        return True
