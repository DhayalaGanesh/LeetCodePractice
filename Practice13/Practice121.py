from typing import List
def maximumOfTwo(a: int, b: int):
    if(a>b): return a
    return b
def maximumProfitInList(prices: List[int], startIndex: int, maxPrice: int, minPrice: int):
    if(maxPrice < prices[startIndex]):
        maxPrice = prices[startIndex]
    elif (minPrice > prices[startIndex]):
        if(startIndex + 1 < len(prices)):
            return maximumOfTwo((maxPrice - minPrice), maximumProfitInList(prices, startIndex + 1, prices[startIndex], prices[startIndex]))
    if(startIndex+1 >= len(prices)):
        return maxPrice - minPrice
    return maximumOfTwo((maxPrice - minPrice), maximumProfitInList(prices, startIndex + 1, maxPrice, minPrice))

def maxProfit(prices: List[int]) -> int:
    if(len(prices) == 0 or len(prices) == 1): return 0
    return maximumProfitInList(prices, 1, prices[0], prices[0])

print(maxProfit([2, 3, 10, 6, 4, 8, 1]))
print(maxProfit([7, 9, 5, 6, 3, 2]))
print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))