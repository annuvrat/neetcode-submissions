class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i in range(len(nums)):
            needed  =  target -nums[i]


            if needed in result:
             return [result[needed],i]

            result[nums[i]]  = i



        return []
