class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = cnt = 0   #intitalizes res =0 cnt = 0 
        for num in nums: #start loop: nums[0] =1
            cnt = cnt +1 if num else 0 #num 1 , inccrement  cnt to cnt+1
            res = max(res,cnt) #update res = max(res, cnt) = max(0,1)= 1
        return res