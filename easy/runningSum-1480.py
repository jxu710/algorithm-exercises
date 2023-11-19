class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sumArr = []
        sum = 0
        for num in nums:
            sum += num
            sumArr.append(sum)
        return sumArr
