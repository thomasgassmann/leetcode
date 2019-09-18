class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        results = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in results and results[complement] != i:
                return [results[complement], i]
        
            results[nums[i]] = i
