#!/usr/bin/env python
# coding: utf-8

# class Solution:
#     # @return a tuple, (index1, index2)
#     def twoSum(self, num, target):
#         diff = [target - i for i in num]
#         TwoSum = [[num.index(i)+1, diff.index(i)+1] for i in diff if i in num]
#         t = TwoSum[0]
#         t.sort()
#         return tuple(t)


                
        # diff = [target - i for i in num]
        # TwoSum = [[num.index(i)+1, diff.index(i)+1] for i in diff if i in num]
        # t = TwoSum[0]
        # t.sort()
        # return tuple(t)

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        for i in num:
            diff = target - i
            if diff == i:
                index1 = num.index(i)
                num.remove(i)
                if diff in num:
                    return (index1+1, num.index(diff)+2)
            else:
                if diff in num:
                # print num.index(diff)
                # print num.index(i)
                    if num.index(diff) < num.index(i):
                        return (num.index(diff)+1, num.index(i)+1)
                    elif num.index(diff) > num.index(i):
                        return (num.index(i)+1, num.index(diff)+1)
        
    
s = Solution()
print s.twoSum([0,4,3,0], 0)
