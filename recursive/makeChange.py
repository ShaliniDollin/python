def makeChange(coinList,change,minCoins,coinsUsed):
	for cent in range(change+1):
		coinCount = cent
		newCoin = 1
		for j in [c for c in coinList if c <= cent]: 
			if minCoins[cent-j] + 1 < coinCount:
				coinCount = minCoins[cent-j] + 1
				newCoin = j
		minCoins[cent] = coinCount
		coinsUsed[cent] = newCoin
	return minCoins[change]

def printCoins(coinsUsed,change):
	coin = change
	while coin > 0:
		thisCoin = coinsUsed[coin]
		print(thisCoin)
		coin = coin - thisCoin


coinUsed = {}
minCoins = {}
print(makeChange([1,5,10,21,25],63,minCoins,coinUsed))
printCoins(coinUsed,63)		 
