"""3023"""
def main():
    """calc"""
    num = int(input())
    press = 0
    symbol = num
    if num == 1:
        print(1)
    else:
        for _ in range(num):
            button = len(str(num))
            press += button
            num -= 1
        print(press + symbol)
main()
