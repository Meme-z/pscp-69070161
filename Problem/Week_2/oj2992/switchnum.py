"""2992"""
def main():
    """numxrevnum"""
    num =  int(input())
    symbol = input()
    revnum = int(str(num)[::-1])
    ans = 0
    if symbol == "+":
        ans = num + revnum
    elif symbol == "*":
        ans = num * revnum
    print(f"{num} {symbol} {revnum} = {ans}")
main()
