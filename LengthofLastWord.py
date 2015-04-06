class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        count = 0
        if len(s) == 0:
            return count

        i = -1
        while True:
            print i
            if s[i]==' ':
                return count
            else:
                count = count + 1
                if -i == len(s):
                    return count
                i = i - 1

s = Solution()
print s.lengthOfLastWord('a ')