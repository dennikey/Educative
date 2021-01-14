# Given: Array of numbers representing daily stock prices (each index is a day and each value is the price)
# Problem: Maximize the profit by buying on the day before selling

# Solution: Go through the entire array and track the minimum price so that it can be compared to the traversed value
# Time: O(n) and Space: O(1)
def buy_and_sell_once(prices):
    max_profit = 0.0
    min_price = float('inf')
    for price in prices:
        min_price = min(min_price, price)
        compare_profit = price - min_price
        max_profit = max(max_profit, compare_profit)
    return max_profit

A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
print(buy_and_sell_once(A))