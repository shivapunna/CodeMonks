
def getMinCoins(v, coins):
    cur_min = 0
    global ChangeFlag
    for c in coins:
        if v-c < 0:
            break
        if not ChangeFlag and v-c == 0:
            ChangeFlag = True
        value = 1 + getMinCoins(v-c, coins)

        if not cur_min:
            cur_min = value
        elif value < cur_min:
            cur_min = value

    return cur_min


if __name__ == '__main__':
    ChangeFlag = False
    v = 30;     coins = [9, 6, 5, 1]
    # v = 31;   coins = [25, 10, 5]

    coins.sort()
    coins_min = getMinCoins(v, coins)
    print( coins_min if ChangeFlag else "Change not possible for this")

