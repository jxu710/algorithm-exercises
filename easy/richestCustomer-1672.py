class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth_array = []
        for account in accounts:
            wealth = sum(account)
            wealth_array.append(wealth)

            richest = max(wealth_array)
        return richest
