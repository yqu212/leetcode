class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        splittedString = s.split(' ')
        print splittedString
        if len(splittedString) < 2:
            return len(splittedString[-1])
        return len(splittedString[-2])

s = Solution()
print s.lengthOfLastWord(' a')