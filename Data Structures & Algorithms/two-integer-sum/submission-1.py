class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i,num in enumerate(nums):
            val = target - num
            if val in result:
                return [result[val],i]
            result[num] = i
