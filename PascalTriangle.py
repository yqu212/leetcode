# coding: utf-8
#!/usr/bin/env python

import math

class Solution:
    def getRow(self, rowIndex):
        return [math.factorial(rowIndex)/(math.factorial(rowIndex-i)*math.factorial(i)) for i in range(0,rowIndex+1)]

s = Solution()
print(s.getRow(3))
