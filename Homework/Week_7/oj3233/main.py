"""wow"""
def main():
    """idk"""
    win = input()
    buy = input()
    prize = 0
    if win[0] == buy[0]:
        if win == buy:
            prize = 1000000
        elif win[-3:] == buy[-3:]:
            prize = 2000
        elif win[-2:] == buy[-2:]:
            prize = 1000
        elif win[1:] != buy[1:]:
            prize = 20
    else:
        if win[2:] == buy[2:]:
            prize = 100000
        elif win[-3:] == buy[-3:]:
            prize = 200
        elif win[-2:] == buy[-2:]:
            prize = 100
        else:
            prize = 0
    print(prize)
main()
