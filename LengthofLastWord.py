class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        count = 0

        for i in s[::-1]:
            if i==' ':
                return count
            else:
                count = count + 1

s = Solution()
print s.lengthOfLastWord('')