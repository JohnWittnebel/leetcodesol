class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # idea: simply use a stack to push words on and once there are no more words we pop them
        myStack = []
        currWord = ""
        for i in range(len(s)):
            if s[i] == " " and len(currWord) > 0:
                myStack.append(currWord)
                currWord = ""
            elif s[i] != " ":
                currWord += s[i]
        if len(currWord) > 0:
            myStack.append(currWord)
        
        retStr = ""
        while len(myStack) != 0:
            nextWord = myStack.pop()
            retStr += nextWord
            retStr += " "
        return retStr[0:len(retStr)-1]


