money = 18134
f = open("C:/Users/student/Desktop/BA5A_Input.txt", "r")
coinsStr = (f.readline()).split(",")
f.close()

coins = len(coinsStr)*[0]

for i in range(len(coinsStr)):
    coins[i] = int(coinsStr[i])

def MinimumChange(money, coins):
    minnumcoins = (money + 1) * [0]
    for m in range(1, money + 1):
        minnumcoins[m] = m + 1  # basically the same as Inf since coins can't be <= 0
        for coin in coins:
            if m >= coin:
                if minnumcoins[m - coin] + 1 < minnumcoins[m]:
                    minnumcoins[m] = minnumcoins[m - coin] + 1
    return minnumcoins[money]

print(MinimumChange(money, coins))