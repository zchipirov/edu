from this import d


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        d = 0
        for x in nums:
            d ^= x
        return d

sol = Solution()
print(sol.singleNumber([2,2,1]))