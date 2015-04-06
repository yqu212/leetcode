class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        import re
        if re.search(r' *([a-zA-Z]+) *\Z',s) is None:
            return 0
        else:
            return len(re.search(r' *([a-zA-Z]+) *\Z',s).group(1))

        
s = Solution()
print s.lengthOfLastWord('')