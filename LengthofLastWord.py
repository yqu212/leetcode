class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        import re
        tmp = re.search(r' *([a-zA-Z]+) *\Z',s)
        if tmp is None:
            return 0
        else:
            return len(tmp.group(1))

        
s = Solution()
print s.lengthOfLastWord('')