class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            val = target - nums[i]
            for j in range(len(nums)):
                if(i != j):
                    if val == nums[j]:
                        return [i,j]
