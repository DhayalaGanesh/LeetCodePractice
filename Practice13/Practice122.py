#122. Best Time to Buy and Sell Stock II
#Medium

#5241

#2172

#Add to List

#Share
#You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

#On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

#Find and return the maximum profit you can achieve.

 

#Example 1:

#Input: prices = [7,1,5,3,6,4]
#Output: 7
#Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
#Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
#Total profit is 4 + 3 = 7.
#Example 2:

#Input: prices = [1,2,3,4,5]
#Output: 4
#Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
#Total profit is 4.
#Example 3:

#Input: prices = [7,6,4,3,1]
#Output: 0
#Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
 

#Constraints:

#1 <= prices.length <= 3 * 104
#0 <= prices[i] <= 104
from typing import List
def maxProfit(prices: List[int]) -> int:
    def maximumOfTwo(a: int, b: int):
        if(a>b): return a
        return b
    def maximumProfitInList(prices: List[int], startIndex: int, maxPrice: int, minPrice: int):
        if(maxPrice < prices[startIndex]):
            maxPrice = prices[startIndex]
        elif (minPrice > prices[startIndex]):
            if(startIndex + 1 < len(prices)):
                return maximumOfTwo((maxPrice - minPrice), (maxPrice - minPrice) + maximumProfitInList(prices, startIndex + 1, prices[startIndex], prices[startIndex]))
        else:
            if(startIndex + 1 < len(prices)):
                return maximumOfTwo((maxPrice - minPrice), (maxPrice - minPrice) + maximumProfitInList(prices, startIndex + 1, prices[startIndex], prices[startIndex]))
        if(startIndex+1 >= len(prices)):
            return maxPrice - minPrice
        return maximumOfTwo((maxPrice - minPrice), maximumProfitInList(prices, startIndex + 1, maxPrice, minPrice))
    if(len(prices) == 0 or len(prices) == 1): return 0
    return maximumProfitInList(prices, 1, prices[0], prices[0])
print(maxProfit([1,2,3,4,5]))
print(maxProfit([7,6,4,3,1]))
print(maxProfit([1, 7, 2, 3, 6, 7, 6, 7]))

def maxProfitOptimal(prices: List[int]) -> int:
    def maximumOfTwo(a: int, b: int):
        if(a>b): return a
        return b
    def maximumProfitOptimal(prices: List[int]):
        minPrice = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if(minPrice>prices[i]):
                minPrice = prices[i]
            else:
                profit = profit + (prices[i]-minPrice)
                minPrice = prices[i]
        return profit
        
    if(len(prices) == 0 or len(prices) == 1): return 0
    return maximumProfitOptimal(prices)

print(maxProfitOptimal([1,2,3,4,5]))
print(maxProfitOptimal([7,6,4,3,1]))
print(maxProfitOptimal([1, 7, 2, 3, 6, 7, 6, 7]))