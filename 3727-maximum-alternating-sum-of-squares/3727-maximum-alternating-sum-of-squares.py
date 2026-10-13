class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        X = sorted(a * a for a in nums)
        return sum(X) - sum(X[:len(X) // 2]) * 2
        