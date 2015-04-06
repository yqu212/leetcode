# coding: utf-8
#!/usr/bin/env python

class Solution:
    # @return a string
    def countAndSay(self, n):
        curSeq = '1'
        nth = 2
        tmpSeq = ''
        if n == 1:
            return '1'
        else:
            while nth <= n:
                currentNumber = ''
                count = 0
                for i in curSeq:
                    if i != currentNumber:
                        if currentNumber != '':
                            tmpSeq += str(count) + currentNumber
                        currentNumber = i
                        count = 1
                    else:
                        count = count + 1
                tmpSeq += str(count) + currentNumber
                curSeq = tmpSeq
                tmpSeq = ''
                nth = nth + 1
            return curSeq

s = Solution()
print s.countAndSay(5)

