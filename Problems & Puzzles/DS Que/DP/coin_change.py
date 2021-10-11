from typing import List

def coinChange(coins: List[int], amount: int):
    max_amt = amount + 1  # as this would be max among all in worst case (i.e 1 coin * amt times)
    dp = [max_amt] * max_amt  # We need to calculate from [0 ... amt]
    dp[0] = 0 # As we know there is no way to get 0 amt via any coin

    for amt in range(1, max_amt):
        for coin in coins:
            if amt >= coin:
                dp[amt] = min(dp[amt], 1 + dp[amt-coin])
    return dp[amount] if dp[amount] != max_amt else 0  # 0 ways if dp[amt] is not changed in iteration


if __name__ == '__main__':
    coins = [2, 5, 10]
    amount = 17
    ans = coinChange(coins, amount)
    print(ans)

