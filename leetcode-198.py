'''
https://leetcode.com/problems/house-robber/description/

Time Complexity: O(n)
Space Complexity: O(n)
improvedSpace Complexity: O(1)
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums ) == 1 or len(nums) == 2:
            return max(nums)

        
        # x = [0] * len(nums)
        # x[0], x[1] = nums[0], max(nums[0], nums[1])
        a = nums[0]
        b= max(nums[0],nums[1])
        current = 0
        for i in range(2, len(nums)):
            # x[i] = max(x[i-1], x[i-2] + nums[i])

            current = max(b, a+nums[i])
            a = b
            b = current
            print(a,b)
        

        return b