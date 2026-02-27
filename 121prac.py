"""
LC 121 Best time to buy/sell stock
input = [7, 1, 5, 3, 6, 4]
output = day 2 sell day 5

solution 2:
    find all possible min/max ranges
    calc most profitable outcomes 

"""

prices =  [7, 1, 5, 3, 6, 4]

class Solution:
    def maxProfit(self, prices):
        min_price = prices[0]
        max_price = 0
        min_price_index = 0
        max_price_index = 0

        # find min price
        for i in range(len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
                min_price_index = i
        # find max only following after min price  
        for j in range(min_price_index, len(prices)):
            if max_price < prices[j]:
                max_price = prices[j]
                max_price_index = j

        print(f'min price: {min_price}, day: {min_price_index}')
        print(f'max price: {max_price}, day: {max_price_index}')

        def calcProfit(a, b):
            return f'buy day - sell day: = {b} - {a} = {b - a}'
        
        profit = calcProfit(min_price, max_price) 
        return profit

sol = Solution()
print(f'Best days to buy/sell stock: \t{sol.maxProfit(prices)}')