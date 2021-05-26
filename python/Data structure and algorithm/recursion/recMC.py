import time
def recMC(coinValueList, change, knownResults):
    minCoins = change
    if change in coinValueList:   # 递归基本技术条件
        knownResults[change] = 1  # 记录最优解
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]  # 查表成功，直接用最优解
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change - i, knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                # 找到最优解，记录到表中
                knownResults[change] = minCoins
    return minCoins


def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    #  从1分开始到change逐个计算最少硬币数
    for cents in range(1, change + 1):
        # 1. 初始化一个最大值
        coinCount = cents
        newCoin = 1  # 初始化新加硬币
        # 2. 减去每个硬币，向后查最少硬币数，同时记录总的最少数
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
                newCoin = j # 对应最小数量，所减的硬币
        # 3. 得到当前最少硬币数， 记录到表中
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    return minCoins[change]


def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin


momo = [0] * 64
print(time.perf_counter())
print(recMC([1, 5, 10, 21, 25], 63, momo))
print(time.perf_counter())
print(momo)

amnt = 63
clist = [1, 5, 10, 21, 25]
coinUsed = [0] * (amnt + 1)
coinCount = [0] * (amnt + 1)

print("Making change for", amnt, "requires")
print(dpMakeChange(clist, amnt, coinCount, coinUsed), "coins")
print("They are")
printCoins(coinUsed, amnt)
print("The uesd list is as follows:")
print(coinUsed)