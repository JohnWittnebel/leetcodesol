class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool

        if (s == ""):
            if (len(p) % 2 != 0):
                return 0
            for i in range(1,len(p),2):
                if p[i:i+1] != "*":
                    return 0
            return 1"""
        if (s == ""):
            if (len(p) % 2 != 0):
                return 0
            for i in range(1,len(p),2):
                if p[i:i+1] != "*":
                    return 0
            return 1

        if (s == p) or (len(s) == len(p) and len(p) == 1 and p == "."):
            return 1
        elif len(p) <= 1 or len(s) == 0:
            return 0
        elif (p[0] != s[0]) and (p[0] != ".") and (p[1] != "*"):
            return 0
        elif (p[1] != "*") and (s[0] == p[0]):
            return self.isMatch(s[1:], p[1:])
        elif (p[1] != "*") and (p[0] == "."):
            return self.isMatch(s[1:], p[1:])
        elif (p[0] != s[0]):
            return self.isMatch(s,p[2:])
        else:
            return self.isMatch(s[1:], p) or self.isMatch(s,p[2:]) or self.isMatch(s[1:],p[2:])

x = Solution()
print(x.isMatch("mississippi","mis*is*p*."))
print(x.isMatch("","a*b*c*"))
print(x.isMatch("","a*b*c*a"))
