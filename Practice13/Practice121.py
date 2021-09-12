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

def maximumProfitInListRev(prices: List[int]):
    length = len(prices)
    profit= [0]*length
    max_Price = prices[length-1]
    for i in range(length-2, -1, -1):
        if(max_Price < prices[i]):
            max_Price = prices[i]
        profit[i] = maximumOfTwo(profit[i+1], max_Price - prices[i])

    return profit[0]


def maxProfit(prices: List[int]) -> int:
    if(len(prices) == 0 or len(prices) == 1): return 0
    return maximumProfitInList(prices, 1, prices[0], prices[0])

def maximumProfitRev(prices: List[int]) -> int:
    if(len(prices) == 0 or len(prices) == 1): return 0
    return maximumProfitInListRev(prices)


print(maxProfit([2, 3, 10, 6, 4, 8, 1]))
print(maxProfit([7, 9, 5, 6, 3, 2]))
print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))


print(maximumProfitRev([2, 3, 10, 6, 4, 8, 1]))
print(maximumProfitRev([7, 9, 5, 6, 3, 2]))
print(maximumProfitRev([7,1,5,3,6,4]))
print(maximumProfitRev([7,6,4,3,1]))
