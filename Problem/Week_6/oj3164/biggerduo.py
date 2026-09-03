"""bigger"""
def main():
    """funny"""
    big = []
    duo = int(input())
    for _ in range(duo):
        num = []
        for _ in range(2):
            num.append(int(input()))
        num.remove(min(num))
        big.append(num[0])
    if duo == 1:
        print(big[0])
    else:
        print(f"{' + '.join(str(i) for i in big)} = {sum(big)}")
main()
