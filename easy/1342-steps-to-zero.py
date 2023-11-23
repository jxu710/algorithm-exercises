class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0
        if num == 0:
            return 0

        while num > 2:
            if num % 2 == 0:
                num = num / 2
                step = step + 1
            else:
                num = num - 1
                step = step + 1
        return step + 2
