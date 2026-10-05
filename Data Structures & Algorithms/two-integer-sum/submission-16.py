class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i,num in enumerate(nums):
            needed  =  target -num


            if needed in result:
             return [result[needed],i]

            result[num]  = i



        return []
