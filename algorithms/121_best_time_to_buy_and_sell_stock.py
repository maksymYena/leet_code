from typing import List

"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf') # init the min price
        max_profit = 0 # init the max profit
        for price in prices: # go through each price in the array
            print(f"current price to compare {price}")
            if price < min_price: # if we found the less price that we have
                min_price = price # update the min price
                print(f"we found the less price that we have, new price = {min_price}")
            elif price - min_price > max_profit: # calculate potential profit
                max_profit = price - min_price # update max profit value
                print(f"max profile is calculated as {max_profit} = {price} - {min_price}")
        return max_profit

clazz = Solution()
print(clazz.maxProfit(prices=[3,2,6,5,0,3]))  # Ожидаемый результат: 4 (покупка по 2, продажа по 6)
