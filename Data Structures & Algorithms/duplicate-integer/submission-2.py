class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts={}
        for num in nums:
            if num not in counts:
                counts[num] = 1

            else:
                counts[num] += 1


        for i,count in counts.items():
            if count>1:
                return True


        return False