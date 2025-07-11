class Solution(object):
    def twoSum(self, nums, target):
        hash_map = {}

        for i, num in  enumerate(nums):
            complement = target - num
            
            if complement in hash_map:
                return [hash_map[complement], i]
            hash_map[num] = i

 #Time complexity : O(N)
 #Space complexity : O(N)
