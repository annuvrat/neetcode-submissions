class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts={}
        if len(s)!=len(t):
            return False
        for char in s:
            if char not in counts:
                counts[char]= 1
            else:
                counts[char] +=1

        for char in t:
            if char not in counts or counts[char] == 0:
                return False
            counts[char] -= 1

        return True