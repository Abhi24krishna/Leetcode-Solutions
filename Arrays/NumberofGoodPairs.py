"""
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
"""
    def numIdenticalPairs(self, a: List[int]) -> int:
        d={}
        for i in a:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        print(d)
        c=0
        for i in d:
            c+=d[i]*(d[i]-1)//2
        return c
