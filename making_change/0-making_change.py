#!/usr/bin/python3
"""Make change: fewest number of coins needed to meet a total"""


def makeChange(coins, total):
    """Return the fewest number of coins needed to meet total,
    0 if total is 0 or less, or -1 if total cannot be met"""
    if total <= 0:
        return 0
    coins = [c for c in set(coins) if 0 < c <= total]
    if not coins:
        return -1
    inf = total + 1
    dp = [0] + [inf] * total
    for coin in coins:
        for amount in range(coin, total + 1):
            if dp[amount - coin] + 1 < dp[amount]:
                dp[amount] = dp[amount - coin] + 1
    return dp[total] if dp[total] != inf else -1
