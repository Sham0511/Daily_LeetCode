class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        count = 1
        for i in s:
            total += ((123 - ord(i))* count)
            count +=1
        return total