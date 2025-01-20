def greedy_coin(value):
    coins = [1,5,10,20,50,100,200,500]
    n = len(coins)-1
    results = []

    while n>=0:
        while value >= coins[n]:
            value -= coins[n]
            results.append(coins[n])
        n -= 1
    return(results)