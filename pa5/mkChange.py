import sys

coins = []
calls = 0
reads = 0

# read coin values
def readCoins(fnm):
    global coins
    f = open(fnm)
    for line in f:
        l = line.strip().split(" ")
        for c in l:
            coins.append(int(c))
    if db: print("coins:", coins)

def mkChangeDC(n, c):
    """
    Recursive Divide and conquer solution
    
    Args:
        n - The amount to make.
        c - Coin in question, index of the coins array.
    """
    global calls
    calls+=1
    
    if n==0:
        return 1
    elif c == 0:
        if n % coins[c] == 0:
            return 1
        else:
            return 0

    d = 0
    ways = 0
    while d*coins[c] <= n:
        ways += mkChangeDC(n-d*coins[c], c-1)
        d+=1
    return ways

def lookup(table, n, coin):
    global reads
    reads+=1
    if n < 0:
        return 0
    elif coin < 0:
        if n == 0:
            return 1
        else:
            return 0
    else:
        return table[coin][n]

def mkChangeDP(n):
    # Build table
    table = [[0 for c in range(n)] for r in range(len(coins))]
    table[0][0] = 1
    # table[coin][amount]
    for coin in range(len(coins)):
        for amount in range(n):
            takeAmount = lookup(table, amount-coins[coin], coin)
            leaveAmount = lookup(table, amount, coin-1)
            table[coin][amount] = takeAmount + leaveAmount
    return lookup(table, n-1, len(coins)-1)

if __name__ == "__main__":
    db = len(sys.argv)>3
    n = int(sys.argv[1])
    fnm = sys.argv[2]
    readCoins(fnm)
    c = len(coins)-1
    if db:
        import time
    if db:
        start = time.time()
    ways = mkChangeDC(n,c)
    if db:
        end = time.time()
    print("mkChangeDC")
    print("amount:", n, "coins:", coins, "ways:", ways, "calls:", calls)
    if db:
        print("time: {}".format(end-start))
    if db:
        start = time.time()
    ways = mkChangeDP(n+1)
    if db:
        end = time.time()
    print("mkChangeDP")
    print("amount:", n, "coins:", coins, "ways:", ways, "reads:", reads)
    if db:
        print("time: {}".format(end-start))
