#!/usr/bin/env python
# coding: utf-8

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        d = {}
        for index in xrange(len(num)):
            diff = target - num[index]
            if diff in d:
                return (d[diff] + 1, index + 1)
            d[num[index]] = index

s = Solution()
print s.twoSum([0,4,3,0], 0)
